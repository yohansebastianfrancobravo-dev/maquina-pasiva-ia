import os
import json
import re
from datetime import date
from pathlib import Path
from groq import Groq

RUTA_PUBLICACIONES = Path("publicaciones.json")
MODELO = "qwen/qwen3.8-27b"


def generar_texto(cliente, instrucciones, max_tokens):
    respuesta = cliente.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres redactor de TECHNOVA, un sitio de tecnología en español. "
                    "Escribe información clara, útil y responsable. "
                    "No inventes características, precios, pruebas, estadísticas, "
                    "marcas, enlaces ni noticias. No prometas ganancias. "
                    "No generes etiquetas HTML ni enlaces comerciales."
                )
            },
            {"role": "user", "content": instrucciones}
        ],
        model=MODELO,
        temperature=0.4,
        max_tokens=max_tokens
    )

    texto = respuesta.choices[0].message.content
    if not texto:
        raise ValueError("La IA devolvió contenido vacío.")

    return texto.strip()


def generar_publicacion():
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError("Falta configurar GROQ_API_KEY.")

    cliente = Groq(api_key=api_key)

    print("[TECHNOVA] Generando tema...")
    titulo = generar_texto(
        cliente,
        (
            "Propón un título breve para un artículo educativo de tecnología. "
            "Puede tratar sobre seguridad digital, cuidado de dispositivos, "
            "uso responsable de aplicaciones o consejos tecnológicos generales. "
            "No promociones productos ni prometas resultados. "
            "Devuelve únicamente el título."
        ),
        60
    )

    titulo = re.sub(r"[\r\n]+", " ", titulo).strip().strip('"')
    titulo = titulo[:120]

    if not titulo:
        raise ValueError("No se pudo generar un título válido.")

    print("[TECHNOVA] Redactando artículo...")
    contenido = generar_texto(
        cliente,
        (
            f"Escribe un artículo educativo en español sobre: {titulo}. "
            "Máximo 180 palabras, con párrafos cortos y consejos prácticos. "
            "No inventes datos, especificaciones, precios ni noticias. "
            "No afirmes que un producto tiene funciones concretas. "
            "No incluyas HTML, enlaces, publicidad ni promesas de dinero. "
            "Devuelve solamente el artículo."
        ),
        350
    )

    contenido = re.sub(r"<[^>]*>", "", contenido).strip()

    if not contenido:
        raise ValueError("El artículo generado está vacío.")

    if not RUTA_PUBLICACIONES.exists():
        publicaciones = []
    else:
        with RUTA_PUBLICACIONES.open("r", encoding="utf-8") as archivo:
            publicaciones = json.load(archivo)

    if not isinstance(publicaciones, list):
        raise ValueError("publicaciones.json debe contener una lista.")

    ids = [
        p.get("id", 0)
        for p in publicaciones
        if isinstance(p.get("id", 0), int)
    ]

    nuevo_id = max(ids, default=0) + 1

    nueva_publicacion = {
        "id": nuevo_id,
        "fecha": date.today().isoformat(),
        "titulo": titulo,
        "contenido": contenido,
        "categoria": "Tecnología",
        "estado": "revision"
    }

    publicaciones.insert(0, nueva_publicacion)

    temporal = RUTA_PUBLICACIONES.with_suffix(".tmp")

    with temporal.open("w", encoding="utf-8") as archivo:
        json.dump(publicaciones, archivo, ensure_ascii=False, indent=2)
        archivo.write("\n")

    os.replace(temporal, RUTA_PUBLICACIONES)

    print("Publicación guardada correctamente.")
    print("ID:", nuevo_id)
    print("Título:", titulo)
    print("Estado: revision")
    print("Total de publicaciones:", len(publicaciones))


if __name__ == "__main__":
    generar_publicacion()

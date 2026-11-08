import os
import json
import re
import random
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
from groq import Groq

RUTA = Path("publicaciones.json")
MODELO = "qwen/qwen3.8-27b"

TEMAS = [
    ("phishing", "Cómo reconocer mensajes de phishing"),
    ("contrasenas", "Cómo crear contraseñas seguras"),
    ("verificacion", "Qué es la verificación en dos pasos"),
    ("copias", "Por qué es importante hacer copias de seguridad"),
    ("wifi", "Consejos para utilizar redes Wi-Fi públicas"),
    ("permisos", "Cómo revisar los permisos de las aplicaciones"),
    ("actualizaciones", "Por qué debes mantener actualizado tu celular"),
    ("almacenamiento", "Cómo organizar el almacenamiento del teléfono"),
    ("bateria", "Hábitos para cuidar la batería del celular"),
    ("codigos_qr", "Precauciones al utilizar códigos QR"),
    ("bluetooth", "Cómo funciona la conexión Bluetooth"),
    ("nube", "Qué es el almacenamiento en la nube"),
    ("inteligencia_artificial", "Cómo funciona la inteligencia artificial"),
    ("errores_ia", "Por qué la inteligencia artificial puede equivocarse"),
    ("huella_digital", "Qué es la huella digital en Internet"),
    ("accesibilidad", "Funciones de accesibilidad en los teléfonos"),
    ("archivos", "Cómo organizar archivos digitales"),
    ("notificaciones", "Cómo administrar las notificaciones del celular"),
    ("navegadores", "Para qué sirven las actualizaciones del navegador"),
    ("estafas", "Señales para identificar posibles estafas digitales")
]

PROHIBIDO = re.compile(
    r"cricut|stickerpix|gana dinero|ganar dinero|ingresos|"
    r"negocio|emprendimiento|monetizar|rentable|"
    r"oferta imperdible|compra ahora|hazte rico",
    re.IGNORECASE
)


def cargar_publicaciones():
    if not RUTA.exists():
        return []

    with RUTA.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if not isinstance(datos, list):
        raise ValueError("publicaciones.json debe contener una lista.")

    return datos


def generar_articulo(cliente, titulo):
    for intento in range(3):
        respuesta = cliente.chat.completions.create(
            model=MODELO,
            temperature=0.35,
            max_tokens=350,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres el redactor educativo de TECHNOVA. "
                        "Escribes en español claro y sencillo. "
                        "No haces publicidad ni vendes productos. "
                        "No inventes estadísticas, noticias, precios "
                        "ni características técnicas. "
                        "No prometas dinero ni resultados garantizados. "
                        "No uses HTML ni enlaces."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Escribe un artículo educativo titulado: {titulo}. "
                        "Extensión: entre 100 y 160 palabras. "
                        "Explica el concepto con claridad y ofrece consejos "
                        "generales y prácticos. No inventes datos. "
                        "Devuelve únicamente el artículo."
                    )
                }
            ]
        )

        contenido = respuesta.choices[0].message.content or ""
        contenido = re.sub(r"<[^>]*>", "", contenido).strip()

        if contenido and not PROHIBIDO.search(contenido):
            return contenido

        print(f"Contenido rechazado. Intento {intento + 2}...")

    raise ValueError("No se pudo generar un artículo válido.")


def generar_publicacion():
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError("Falta configurar GROQ_API_KEY.")

    cliente = Groq(api_key=api_key)
    publicaciones = cargar_publicaciones()

    usados = {
        p.get("tema_id")
        for p in publicaciones
        if isinstance(p, dict)
    }

    disponibles = [
        tema for tema in TEMAS
        if tema[0] not in usados
    ]

    if not disponibles:
        raise RuntimeError("Se agotaron los temas disponibles.")

    tema_id, titulo = random.choice(disponibles)

    print("[TECHNOVA] Tema seleccionado:", titulo)
    print("[TECHNOVA] Generando artículo...")

    contenido = generar_articulo(cliente, titulo)

    ids = [
        p.get("id", 0)
        for p in publicaciones
        if isinstance(p, dict)
        and isinstance(p.get("id", 0), int)
    ]

    nuevo_id = max(ids, default=0) + 1

    nueva = {
        "id": nuevo_id,
        "tema_id": tema_id,
        "fecha": datetime.now(ZoneInfo("America/Bogota")).date().isoformat(),
        "titulo": titulo,
        "contenido": contenido,
        "categoria": "Tecnología",
        "estado": "revision"
    }

    publicaciones.insert(0, nueva)

    temporal = RUTA.with_suffix(".tmp")

    with temporal.open("w", encoding="utf-8") as archivo:
        json.dump(publicaciones, archivo, ensure_ascii=False, indent=2)
        archivo.write("\n")

    os.replace(temporal, RUTA)

    print("[TECHNOVA] Publicación guardada.")
    print("ID:", nuevo_id)
    print("Título:", titulo)
    print("Estado: revision")
    print("Total:", len(publicaciones))


if __name__ == "__main__":
    generar_publicacion()

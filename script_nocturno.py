import os
from groq import Groq

# Configurar el cliente con la API Key guardada de forma segura en GitHub
CLIENTE = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Tu enlace de afiliado real de Amazon para la Cricut StickerPix
MI_ENLACE_AFILIADO = "https://amzn.to"

def generar_pagina_monetizable():
    # Agente 1: Investigador de Tendencias de Software y Gadgets
    prompt_tendencia = (
        "Identifica una herramienta tecnológica, gadget de diseño creativo o app moderna que la gente esté buscando mucho "
        "para mejorar su productividad, manualidades o negocio en casa. Devuelve solo el nombre en una sola línea."
    )
    res_1 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_tendencia}],
        model="qwen/qwen3.8-27b",
        temperature=0.5,
        max_tokens=50
    )
    producto = res_1.choices.message.content.strip()

    # Agente 2: Redactor SEO
    prompt_articulo = (
        f"Escribe una reseña de blog corta y muy persuasiva (máximo 250 palabras) sobre cómo la creación de etiquetas, "
        f"diseño personalizado y herramientas como la impresora todo en uno '{producto}' pueden potenciar un emprendimiento en casa. "
        f"Al final del texto incluye este botón de compra de forma exacta utilizando este código HTML: "
        f"<br><br><a href='{MI_ENLACE_AFILIADO}' style='color:white; background-color:#FF9900; padding:12px 24px; text-decoration:none; border-radius:6px; font-weight:bold; display:inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>🛒 Ver Cricut StickerPix en Amazon</a>"
    )
    res_2 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_articulo}],
        model="qwen/qwen3.8-27b",
        temperature=0.6,
        max_tokens=500
    )
    contenido_html = res_2.choices.message.content

    # Crear la estructura de la página web index.html
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recomendaciones Tecnológicas Inteligentes</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; max-width: 750px; margin: auto; padding: 30px; background-color: #f9f9f9; color: #333; }}
        h1 {{ color: #111; border-bottom: 2px solid #FF9900; padding-bottom: 10px; font-size: 28px; }}
        .post {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-top: 20px; }}
        a:hover {{ background-color: #e68a00 !important; }}
    </style>
</head>
<body>
    <h1>🚀 Recomendación Tecnológica del Día (IA Autónoma)</h1>
    <div class="post">
        {contenido_html}
    </div>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_final)
    print("✅ Página index.html actualizada correctamente.")

if __name__ == "__main__":
    generar_pagina_monetizable()

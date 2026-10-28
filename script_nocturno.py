import os
from groq import Groq

# 1. Configurar el cliente con la API Key guardada de forma segura en GitHub
CLIENTE = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MI_ENLACE_AFILIADO = "https://amzn.to/4Bvi7Uj" # Cambia esto por tu enlace real luego

def generar_pagina_monetizable():
    print("🤖 Iniciando enjambre de agentes en la nube...")
    
    # Agente 1: Investigador de Tendencias de Software
    prompt_tendencia = (
        "Identifica un software, herramienta de inteligencia artificial o app moderna que la gente esté buscando mucho "
        "para mejorar su productividad o negocio. Devuelve solo el nombre en una sola línea."
    )
    res_1 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_tendencia}],
        model="qwen/qwen3.8-27b",
        temperature=0.5,
        max_tokens=50
    )
    producto = res_1.choices[0].message.content.strip()

    # Agente 2: Redactor SEO
    prompt_articulo = (
        f"Escribe una reseña de blog corta y muy persuasiva (máximo 300 palabras) sobre por qué usar {producto} "
        f"cambiará la forma de trabajar de un emprendedor. Al final del texto incluye este enlace exactamente "
        f"como un botón de compra atractivo utilizando HTML: <a href='{MI_ENLACE_AFILIADO}' style='color:blue; font-weight:bold;'>[Probar Herramienta Oficial Aquí]</a>"
    )
    res_2 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_articulo}],
        model="qwen/qwen3.8-27b",
        temperature=0.6,
        max_tokens=500
    )
    contenido_html = res_2.choices[0].message.content

    # Crear la estructura de la página web index.html
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recomendaciones de Software IA - Automatizado</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; }}
        h1 {{ color: #333; }}
        .post {{ background: #f4f4f4; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <h1>🚀 Recomendaciones del Día (IA Autónoma)</h1>
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

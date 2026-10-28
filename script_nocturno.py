import os
from groq import Groq

# 1. Configurar el cliente con la API Key segura de GitHub
CLIENTE = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Tu enlace de afiliado real de Amazon
MI_ENLACE_AFILIADO = "https://amzn.to"

def generar_pagina_monetizable():
    print("🚀 Iniciando infraestructura autónoma en la nube...")
    
    # AGENTE 1: Investigador de Tendencias de Software e IA
    prompt_tendencia = (
        "Identifica un software, herramienta de inteligencia artificial o app moderna que la gente esté buscando mucho "
        "para mejorar su productividad, diseño o negocio. Devuelve solo el nombre en una sola línea corta."
    )
    
    res_1 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_tendencia}],
        model="qwen/qwen3.8-27b",
        temperature=0.5,
        max_tokens=50
    )
    producto = res_1.choices.message.content.strip()

    # AGENTE 2: Redactor SEO
    prompt_articulo = (
        f"Escribe una reseña de blog corta y muy persuasiva (máximo 180 palabras) sobre por qué un emprendedor "
        f"debería usar la herramienta llamada '{producto}' hoy mismo. Haz el texto estructurado con párrafos limpios. "
        f"NO incluyas enlaces ni etiquetas HTML dentro de tu respuesta, solo el texto del artículo."
    )
    
    res_2 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_articulo}],
        model="qwen/qwen3.8-27b",
        temperature=0.6,
        max_tokens=350
    )
    contenido_texto = res_2.choices.message.content

    # Bucle de seguridad: Inyección directa de tu botón de Amazon desde Python
    boton_html = f"<br><br><center><a href='{MI_ENLACE_AFILIADO}' target='_blank' style='display:inline-block; background-color:#ff9900; color:black; padding:15px 30px; font-weight:bold; text-decoration:none; border-radius:5px; font-size:1.1em;'>🛒 [Ver Oferta Especial Aquí]</a></center>"

    # ESTRUCTURA WEB FINAL
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recomendaciones de Software e IA - Sistema Autónomo</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; background-color: #fafafa; }}
        h1 {{ color: #222; border-bottom: 2px solid #333; padding-bottom: 10px; text-align: center; }}
        .post {{ background: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; font-size: 1.1em; }}
        footer {{ text-align: center; margin-top: 40px; font-size: 0.8em; color: #777; }}
    </style>
</head>
<body>
    <h1>🚀 Recomendaciones del Día (IA Autónoma)</h1>
    <p style="text-align:center; color:#666; font-style:italic;">Actualizado automáticamente todos los días a las 3:00 AM.</p>
    <div class="post">
        {contenido_texto}
        {boton_html}
    </div>
    <footer>
        <p>© 2026 Sistema de Ingresos Pasivos Automatizado</p>
    </footer>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_final)
    print("✅ Página index.html actualizada correctamente sin enlaces rotos.")

if __name__ == "__main__":
    generar_pagina_monetizable()
    

import os
from groq import Groq

# 1. Configurar la infraestructura del cliente de Groq con tu API Key segura en GitHub
CLIENTE = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Tu enlace de afiliado real y verificado
MI_ENLACE_AFILIADO = "https://amzn.to"

def generar_pagina_monetizable():
    print("🚀 Iniciando infraestructura autónoma en la nube...")
    
    # ---------------------------------------------------------
    # AGENTE 1: Investigador de Tendencias de Software e IA
    # ---------------------------------------------------------
    prompt_tendencia = (
        "Identifica un software, herramienta de inteligencia artificial o app moderna que la gente esté buscando mucho "
        "para mejorar su productividad, diseño, automatización o negocio. Devuelve solo el nombre en una sola línea corta."
    )
    
    print("[IA] Agente 1 analizando nichos y herramientas de moda...")
    res_1 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_tendencia}],
        model="qwen/qwen3.8-27b",
        temperature=0.5,
        max_tokens=50
    )
    producto = res_1.choices[0].message.content.strip()

    # ---------------------------------------------------------
    # AGENTE 2: Redactor SEO y Monetizador B2B
    # ---------------------------------------------------------
    prompt_articulo = (
        f"Escribe una reseña de blog corta y muy persuasiva (máximo 200 palabras) sobre por qué usar {producto} "
        f"cambiará la forma de trabajar de un emprendedor o creador de contenido. Haz el texto estructurado. "
        f"Al final del texto incluye este enlace exactamente como un botón de compra atractivo utilizando HTML: "
        f"<br><br><a href='{MI_ENLACE_AFILIADO}' target='_blank' style='display:inline-block; background-color:#ff9900; color:black; padding:12px 20px; font-weight:bold; text-decoration:none; border-radius:5px;'>[Ver Herramienta y Oferta Oficial Aquí]</a>"
    )
    
    print("[IA] Agente 2 redactando el post optimizado para la web...")
    res_2 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_articulo}],
        model="qwen/qwen3.8-27b",
        temperature=0.6,
        max_tokens=400  # Límite estricto para evitar el error 429 de tokens
    )
    contenido_html = res_2.choices[0].message.content

    # ---------------------------------------------------------
    # ESTRUCTURA WEB: Crear el archivo index.html para tu página
    # ---------------------------------------------------------
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recomendaciones de Software e IA - Sistema Autónomo</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; background-color: #fafafa; }}
        h1 {{ color: #222; border-bottom: 2px solid #333; padding-bottom: 10px; }}
        .post {{ background: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }}
        footer {{ text-align: center; margin-top: 40px; font-size: 0.8em; color: #777; }}
    </style>
</head>
<body>
    <h1>🚀 Recomendaciones del Día (IA Autónoma)</h1>
    <p style="color:#666; font-style:italic;">Esta página se actualiza automáticamente cada madrugada a las 3:00 AM mediante agentes inteligentes.</p>
    <div class="post">
        {contenido_html}
    </div>
    <footer>
        <p>© 2026 Sistema de Ingresos Pasivos Automatizado con GitHub Actions & Groq API</p>
    </footer>
</body>
</html>"""

    # Guardar los cambios directamente en la raíz de tu repositorio
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_final)
    print("✅ Página index.html actualizada y estructurada con éxito.")

if __name__ == "__main__":
    generar_pagina_monetizable()
    

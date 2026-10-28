import os
import re
from groq import Groq

# Configurar el cliente con la API Key guardada de forma segura en GitHub
CLIENTE = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Tu enlace de afiliado real de Amazon para la Cricut StickerPix
MI_ENLACE_AFILIADO = "https://amzn.to"

def generar_pagina_monetizable():
    # Agente 1: Investigador de Tendencias de Software y Gadgets
    prompt_tendencia = (
        "Identifica una herramienta tecnológica, gadget de diseño creativo, componente de hardware o app moderna "
        "que la gente esté buscando mucho para mejorar su productividad, manualidades o negocio en casa. Devuelve solo el nombre en una sola línea."
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
        f"Escribe una reseña de blog corta y muy persuasiva (máximo 200 palabras) sobre cómo la herramienta o gadget '{producto}' "
        f"puede potenciar un emprendimiento o mejorar la vida diaria. Explica sus beneficios. "
        f"Al final del texto incluye este botón de compra de forma exacta utilizando este código HTML: "
        f"<br><br><a href='{MI_ENLACE_AFILIADO}' style='color:white; background-color:#FF9900; padding:12px 24px; text-decoration:none; border-radius:6px; font-weight:bold; display:inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>🛒 Ver en Amazon</a>"
    )
    res_2 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_articulo}],
        model="qwen/qwen3.8-27b",
        temperature=0.6,
        max_tokens=400
    )
    contenido_html = res_2.choices[0].message.content

    # LOGICA DE MEMORIA: Leer lo que ya existía en la página para no borrarlo
    posts_anteriores = ""
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html_viejo = f.read()
            # Extraer solo los posts anteriores que estaban dentro del contenedor
            match = re.search(r'<!-- INICIO_POSTS -->(.*)<!-- FIN_POSTS -->', html_viejo, re.DOTALL)
            if match:
                posts_anteriores = match.group(1)

    # Crear el nuevo bloque de contenido para el producto de hoy
    nuevo_post = f"""
        <div class="post">
            <h2>🔥 Recomendación del Día: {producto}</h2>
            {contenido_html}
        </div>
    """

    # Unir el post nuevo con los posts de los días anteriores
    todos_los_posts = nuevo_post + posts_anteriores

    # Estructura HTML final con el contenedor de memoria
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mega Portal de Recomendaciones Tecnológicas</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; max-width: 750px; margin: auto; padding: 30px; background-color: #f9f9f9; color: #333; }}
        h1 {{ color: #111; border-bottom: 3px solid #FF9900; padding-bottom: 10px; font-size: 32px; text-align: center; }}
        h2 {{ margin-top: 0; color: #222; font-size: 22px; border-bottom: 1px dashed #ccc; padding-bottom: 5px; }}
        .post {{ background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-top: 25px; }}
        a:hover {{ background-color: #e68a00 !important; }}
    </style>
</head>
<body>
    <h1>🚀 Hub Tecnológico Autónomo</h1>
    <p style="text-align: center; color: #666;">Artículos de tendencia generados diariamente en piloto automático por IA.</p>
    
    <!-- INICIO_POSTS -->{todos_los_posts}<!-- FIN_POSTS -->

</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_final)
    print("✅ ¡Blog acumulativo actualizado con éxito!")

if __name__ == "__main__":
    generar_pagina_monetizable()
    

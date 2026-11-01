import os
import re
from groq import Groq

# Configurar el cliente con la API Key guardada de forma segura en GitHub
CLIENTE = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Tu enlace de afiliado real de Amazon para la Cricut StickerPix
MI_ENLACE_AFILIADO = "https://amzn.to/4Bvi7Uj"

def generar_pagina_monetizable():
    # Agente 1: Especialista en Ideas de Negocio y Manualidades
    prompt_enfoque = (
        "Genera un título llamativo y corto (menos de 10 palabras) para un artículo de blog. "
        "Debe enfocarse en cómo usar la Cricut StickerPix, la impresión de pegatinas o el diseño de etiquetas "
        "para ganar dinero desde casa, crear manualidades personalizadas o emprender. "
        "Devuelve SOLO el título en una sola línea, sin comillas ni textos extra."
    )
    
    print("[IA] Agente 1 generando título creativo...")
    res_1 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_enfoque}],
        model="qwen/qwen3.8-27b",
        temperature=0.7,
        max_tokens=50
    )
    # CORRECCIÓN: Añadido [0] para leer la lista correctamente
    titulo_articulo = res_1.choices[0].message.content.strip()

    # Agente 2: Redactor SEO Avanzado
    prompt_articulo = (
        f"Escribe un artículo de blog persuasivo y profesional basado en este título: '{titulo_articulo}'. "
        f"Explica cómo la máquina todo en uno Cricut StickerPix Print + Cut ayuda a lograr esto gracias a su "
        f"capacidad de imprimir, laminar y cortar de forma portátil. Destaca que es ideal para proyectos caseros. "
        f"Mantén el texto en un máximo de 200 palabras, usa párrafos cortos y añade viñetas de ser necesario. "
        f"Al final del texto, incluye EXACTAMENTE este llamado a la acción utilizando este código HTML: "
        f"<br><br><div style='text-align:center;'><a href='{MI_ENLACE_AFILIADO}' class='btn-amazon'>🛒 Ver Oferta Especial de la Cricut StickerPix</a></div>"
    )
    
    print("[IA] Agente 2 redactando el contenido de la tarjeta...")
    res_2 = CLIENTE.chat.completions.create(
        messages=[{"role": "user", "content": prompt_articulo}],
        model="qwen/qwen3.8-27b",
        temperature=0.6,
        max_tokens=500
    )
    # CORRECCIÓN: Añadido [0] para leer la lista correctamente
    contenido_html = res_2.choices[0].message.content

    # LÓGICA DE MEMORIA: Leer publicaciones de días anteriores para acumularlas
    posts_anteriores = ""
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html_viejo = f.read()
            match = re.search(r'<!-- INICIO_POSTS -->(.*)<!-- FIN_POSTS -->', html_viejo, re.DOTALL)
            if match:
                posts_anteriores = match.group(1)

    # Bloque de la publicación de hoy con diseño de tarjeta pulido
    nuevo_post = f"""
        <article class="post">
            <div class="tag-hoy">NUEVO HOY</div>
            <h2>{titulo_articulo}</h2>
            <div class="contenido">
                {contenido_html}
            </div>
        </article>
    """

    todos_los_posts = nuevo_post + posts_anteriores

    # Plantilla web premium (Moderno, Limpio y optimizado para móviles)
    html_final = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StickerCraft Hub - Emprende desde Casa con IA</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --amazon-orange: #ff9900;
            --amazon-hover: #e68a00;
        }}
        body {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.7;
            max-width: 700px;
            margin: auto;
            padding: 20px;
        }}
        header {{
            text-align: center;
            padding: 40px 0 20px 0;
            border-bottom: 1px solid #334155;
            margin-bottom: 30px;
        }}
        header h1 {{
            font-size: 32px;
            margin: 0;
            background: linear-gradient(to right, #ff9900, #ffc47d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }}
        header p {{
            color: var(--text-muted);
            font-size: 15px;
            margin-top: 8px;
        }}
        .post {{
            background-color: var(--card-bg);
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            margin-bottom: 30px;
            position: relative;
            border: 1px solid #2e3e56;
            transition: transform 0.2s;
        }}
        .post:hover {{
            transform: translateY(-2px);
        }}
        .tag-hoy {{
            position: absolute;
            top: 20px;
            right: 20px;
            background-color: #ef4444;
            color: white;
            font-size: 11px;
            font-weight: bold;
            padding: 4px 10px;
            border-radius: 20px;
            letter-spacing: 0.5px;
        }}
        h2 {{
            font-size: 22px;
            color: var(--text-main);
            margin-top: 0;
            margin-bottom: 15px;
            padding-right: 90px;
            font-weight: 700;
        }}
        .contenido {{
            color: #cbd5e1;
            font-size: 15px;
        }}
        .btn-amazon {{
            display: inline-block;
            background-color: var(--amazon-orange);
            color: #0f172a !important;
            font-weight: 700;
            text-decoration: none;
            padding: 14px 28px;
            border-radius: 8px;
            margin-top: 15px;
            transition: all 0.2s;
            box-shadow: 0 4px 14px rgba(255, 153, 0, 0.4);
            font-size: 15px;
        }}
        .btn-amazon:hover {{
            background-color: var(--amazon-hover);
            transform: scale(1.02);
            box-shadow: 0 6px 20px rgba(255, 153, 0, 0.6);
        }}
    </style>
</head>
<body>

    <header>
        <h1>✨ StickerCraft Hub</h1>
        <p>Tu guía diaria de personalización, stickers y proyectos independientes.</p>
    </header>

    <main>
        <!-- INICIO_POSTS -->{todos_los_posts}<!-- FIN_POSTS -->
    </main>

    <footer style="text-align: center; margin-top: 50px; color: var(--text-muted); font-size: 12px; border-top: 1px solid #334155; padding-top: 20px;">
        Generado de forma autónoma por IA • Enlaces de afiliación de Amazon
    </footer>

</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_final)
    print("✅ Página index.html actualizada con diseño premium.")

if __name__ == "__main__":
    generar_pagina_monetizable()
            

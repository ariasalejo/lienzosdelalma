import os
import glob

# 1. Buscar dónde están las imágenes realmente
carpetas_posibles = ['images', 'img', 'obras']
carpeta_imagenes = None
imagenes_encontradas = []

for carpeta in carpetas_posibles:
    if os.path.isdir(carpeta):
        # Buscar jpg, png, jpeg
        fotos = glob.glob(f"{carpeta}/*.jpg") + glob.glob(f"{carpeta}/*.jpeg") + glob.glob(f"{carpeta}/*.png")
        if fotos:
            carpeta_imagenes = carpeta
            # Limpiar nombres para las rutas (usar / en vez de \ por si acaso)
            imagenes_encontradas = [f.replace('\\', '/') for f in fotos]
            break

# Si no hay fotos, creamos una de muestra
if not imagenes_encontradas:
    print("⚠️ No se encontraron imágenes en 'images', 'img' u 'obras'. Usando imagen por defecto.")
    imagen_principal = "https://via.placeholder.com/600x750/e8e5de/333333?text=Sube+tus+fotos+a+img/"
    imagenes_encontradas = [imagen_principal]
else:
    imagen_principal = imagenes_encontradas[0]
    print(f"✅ Se encontraron {len(imagenes_encontradas)} imágenes en la carpeta '{carpeta_imagenes}'.")

# 2. Generar los items de la galería basados en las fotos reales
galeria_html = ""
for idx, ruta_foto in enumerate(imagenes_encontradas[:8]): # Mostrar hasta 8 en la barra
    nombre_base = os.path.basename(ruta_foto).split('.')[0].replace('-', ' ').title()
    if len(nombre_base) > 15: nombre_base = nombre_base[:15] + "..." # Truncar si es muy largo
    
    clase_activa = "active" if idx == 0 else ""
    galeria_html += f"""
        <article class="gallery-item {clase_activa}" onclick="document.getElementById('active-artwork').src='{ruta_foto}'; document.getElementById('titulo-obra').innerText='{nombre_base}'">
          <div class="thumb-frame" style="background-image: url('{ruta_foto}'); background-size: cover; background-position: center;"></div>
          <p class="thumb-title">{nombre_base}</p>
        </article>"""

# 3. Construir el HTML
html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lienzos del Alma · Bernardo León Mejía Rivera</title>
  <link rel="stylesheet" href="styles.css">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
</head>
<body>
  <header class="navbar">
    <div class="brand">
      <span class="site-title">LIENZOS DEL ALMA</span>
      <span class="artist-name">Bernardo León Mejía Rivera</span>
    </div>
    <nav class="nav-links"><a href="#coleccion" class="nav-btn">Ver Colección ↗</a></nav>
  </header>
  
  <main class="museum-view">
    <section class="piece-header">
      <span class="piece-badge">COLECCIÓN PRINCIPAL</span>
      <h1 class="piece-title" id="titulo-obra">Obra Seleccionada</h1>
      <p class="piece-subtitle">Bernardo León Mejía Rivera</p>
    </section>

    <section class="artwork-display">
      <div class="canvas-container">
        <img id="active-artwork" src="{imagen_principal}" alt="Obra de Bernardo León" onerror="this.src='https://via.placeholder.com/600x750/e8e5de/333333?text=Error+Cargando+Imagen'">
        <button id="btn-zoom" class="zoom-overlay">🔍 Ampliar</button>
      </div>
    </section>

    <section class="curatorial-info">
      <details open class="accordion-item"><summary>01. Sobre la obra</summary><div class="accordion-content"><p>Pieza perteneciente a la colección Lienzos del Alma. Una exploración profunda del color, la textura y el sentir del artista.</p></div></details>
      <details class="accordion-item"><summary>02. Ficha técnica</summary><div class="accordion-content"><dl class="data-grid"><dt>Artista</dt><dd>Bernardo León Mejía Rivera</dd><dt>Colección</dt><dd>Lienzos del Alma</dd></dl></div></details>
    </section>

    <section id="coleccion" class="gallery-slider-section">
      <h2>Obras en esta colección</h2>
      <div class="gallery-scroll">
        {galeria_html}
      </div>
    </section>
  </main>

  <div id="modal-zoom" class="lightbox-modal">
    <button class="close-lightbox" id="btn-close-modal">&times;</button>
    <img id="lightbox-img" src="" alt="Vista ampliada">
  </div>

  <footer class="museum-footer">
    <p>LIENZOS DEL ALMA · Bernardo León Mejía Rivera</p>
    <p>Copacabana · Antioquia · Colombia · © 2026</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>"""

# 4. CSS y JS (sin cambios)
css = """
:root { --bg-museum: #F7F5F0; --text-primary: #1C1C1C; --text-secondary: #656565; --border-light: #E5E2DA; --font-heading: 'Cormorant Garamond', serif; --font-body: 'Inter', sans-serif;}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background-color: var(--bg-museum); color: var(--text-primary); font-family: var(--font-body); }
.navbar { position: sticky; top: 0; z-index: 50; display: flex; justify-content: space-between; padding: 1.2rem 2rem; background: rgba(247, 245, 240, 0.95); border-bottom: 1px solid var(--border-light); }
.brand { display: flex; flex-direction: column; }
.site-title { font-size: 0.8rem; font-weight: 500; letter-spacing: 0.18em; }
.artist-name { font-family: var(--font-heading); color: var(--text-secondary); }
.museum-view { max-width: 680px; margin: 0 auto; padding: 2.5rem 1.2rem; }
.piece-title { font-family: var(--font-heading); font-size: 2.8rem; margin: 0.4rem 0 0.2rem; text-align: center;}
.piece-header {text-align: center; margin-bottom: 2rem;}
.piece-badge { font-size: 0.75rem; letter-spacing: 0.2em; color: var(--text-secondary); }
.piece-subtitle { font-family: var(--font-heading); font-size: 1.1rem; font-style: italic; color: var(--text-secondary); }
.artwork-display { display: flex; justify-content: center; margin-bottom: 3rem; }
.canvas-container { position: relative; width: 100%; max-width: 520px; background: #FFF; padding: 12px; box-shadow: 0 16px 40px rgba(0,0,0,0.07); }
.canvas-container img { width: 100%; display: block; border-radius: 2px;}
.zoom-overlay { position: absolute; bottom: 20px; right: 20px; background: rgba(255,255,255,0.92); border-radius: 20px; padding: 0.4rem 0.9rem; cursor: pointer; border: 1px solid var(--border-light); font-size: 0.75rem;}
.curatorial-info { border-top: 1px solid var(--border-light); margin-bottom: 3rem;}
.accordion-item { border-bottom: 1px solid var(--border-light); padding: 1.1rem 0; }
.accordion-item summary { font-size: 0.85rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer; }
.accordion-content { padding-top: 1rem; font-size: 0.95rem; }
.gallery-slider-section h2 { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 400; margin-bottom: 1.2rem; }
.gallery-scroll { display: flex; gap: 1.2rem; overflow-x: auto; padding-bottom: 1rem; }
.gallery-item { min-width: 130px; flex: 0 0 auto; cursor: pointer; text-align: center; }
.thumb-frame { width: 100%; height: 130px; background-color: #E6E2D8; border-radius: 4px; border: 1px solid var(--border-light); transition: opacity 0.2s;}
.gallery-item:hover .thumb-frame { opacity: 0.8; }
.thumb-title { font-size: 0.8rem; margin-top: 0.5rem; }
.lightbox-modal { display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.92); z-index: 100; align-items: center; justify-content: center; }
.lightbox-modal img { max-width: 95%; max-height: 90vh; }
.close-lightbox { position: absolute; top: 20px; right: 25px; background: none; border: none; color: #FFF; font-size: 2.5rem; cursor: pointer; }
.museum-footer { text-align: center; padding: 2.5rem 1rem; font-size: 0.75rem; color: var(--text-secondary); border-top: 1px solid var(--border-light); margin-top: 4rem;}
"""

js = """
document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('modal-zoom');
  const activeImg = document.getElementById('active-artwork');
  const lightboxImg = document.getElementById('lightbox-img');
  
  function openZoom() { lightboxImg.src = activeImg.src; modal.style.display = 'flex'; }
  function closeZoom() { modal.style.display = 'none'; }

  document.getElementById('btn-zoom').addEventListener('click', openZoom);
  activeImg.addEventListener('click', openZoom);
  document.getElementById('btn-close-modal').addEventListener('click', closeZoom);

  modal.addEventListener('click', (e) => { if (e.target === modal) closeZoom(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && modal.style.display === 'flex') closeZoom(); });
});
"""

with open("index.html", "w", encoding="utf-8") as f: f.write(html)
with open("styles.css", "w", encoding="utf-8") as f: f.write(css)
with open("script.js", "w", encoding="utf-8") as f: f.write(js)

print("✅ index.html, styles.css y script.js generados exitosamente.")

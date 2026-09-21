import os

print("🎨 Generando la galería perfecta con orden inverso y descripciones hermosas...")

# 1. IDs de ImgBB en ORDEN INVERSO (El último enlace que enviaste ahora es el primero)
ids = [
    "b5rCVWVh", "RkkRjtBy", "4RCn5BjL", "7xscwr1k", "KpZK07Kq", 
    "KzwdNZd9", "391B0kj2", "nMgBmrCX", "MD9Bxnr7", "0RmKrBpc", 
    "tP2kmfLM", "twbCrNH5", "Wvdyv14q", "prMr0jrD", "FcRmqnJ", 
    "gFd1dp3X", "SwG1jfqB", "CpDGXsWb", "39CWYGsQ", "Pzj73b49", 
    "zhBMBmFh", "YBmwJxMM", "BKHdwtVK", "DFDsVsf", "bj3zgJsX", "KpHDzjST"
]

# 2. Títulos hermosos (también en orden inverso para que coincidan)
titulos = [
    "Legado de Color", "Crepúsculo en el Valle", "El Abrazo Divino", "Armonía Rural", 
    "Retrato de la Serenidad", "Luz de Esperanza", "El Descanso del Caminante", "Naturaleza Viva", 
    "Fe en el Camino", "Reflejos del Alma", "Paisaje de Copacabana", "La Carga", 
    "El Caminante del Bosque", "El Ganso en el Lago", "Amor Alado", "Aves junto al Agua", 
    "Noche Serena en el Lago", "Gratitud Matutina", "Inocencia Infantil II", "Inocencia Infantil I", 
    "La Pasión y el Calvario", "La Resurrección", "Jesús con el Cordero", "El Buen Pastor", 
    "León Majestuoso", "El León Multicolor"
]

# 3. Descripciones poéticas y únicas (en orden inverso)
descripciones = [
    "Una obra que resume la pasión de toda una vida dedicada a embellecer el mundo a través del arte.",
    "Los últimos rayos del día pintan el cielo con una paleta de ocres y violetas, firmada por la mano del maestro.",
    "La protección celestial representada en tonos cálidos que envuelven al espectador en un manto de paz.",
    "La cotidianidad del campo elevada a la categoría de arte, celebrando las raíces de nuestra identidad.",
    "Una mirada que cuenta mil historias, pintada con la ternura y la sabiduría de los años.",
    "Rayos de sol que atraviesan las nubes, simbolizando la bendición y el renacimiento constante.",
    "Un momento de paz y contemplación después de la jornada, bajo la protección de la naturaleza.",
    "La flora y fauna de nuestra tierra retratadas con la delicadeza y el respeto que solo un maestro puede lograr.",
    "Una representación simbólica de la perseverancia y la guía divina en los momentos de travesía.",
    "Un estudio de luz y sombra que captura la profundidad del espíritu humano a través del paisaje.",
    "Los colores de la tierra antioqueña se funden en un horizonte de esperanza y tranquilidad.",
    "Un hombre bajo el peso de un canasto de flores mientras una mujer lo ayuda. Las cargas se hacen más ligeras cuando se comparten.",
    "Por un sendero flanqueado de árboles centenarios, un campesino antioqueño guía su burro. La vida rural y el trabajo honrado.",
    "Solitario y sereno, un ganso nada bajo las ramas retorcidas de un pino. La calma personificada en plumaje.",
    "Dos aves se encuentran tiernamente sobre una rama. Un himno al amor que vuela libre entre los colores del amanecer.",
    "Dos aves de plumaje vibrante se posan grácilmente sobre las ramas. Una escena de armonía natural.",
    "Bajo el manto estrellado y la luna llena, un bote descansa en silencio sobre las aguas tranquilas.",
    "Una mujer extiende sus brazos al cielo en gesto de gratitud. Una celebración de la vida, la fe y las bendiciones del hogar.",
    "Manos juntas en oración, ojos elevados al cielo. La inocencia que se comunica con lo divino.",
    "Un niño de rizos dorados sostiene con delicadeza una pequeña cruz. La pureza de la infancia se encuentra con la fe.",
    "Un viaje espiritual que atraviesa el sufrimiento hasta llegar a la luz, recordando el amor que vence a la muerte.",
    "De la oscuridad del sepulcro emerge la luz cegadora de la vida. Cristo resucitado irrumpe con poder glorioso.",
    "La mirada compasiva del Salvador se inclina sobre el cordero inocente. El halo dorado irradia luz divina.",
    "Jesús camina entre su rebaño con el cayado en mano. Bajo la sombra del árbol protector, cada oveja encuentra refugio.",
    "Majestuosidad en movimiento, una sinfonía cromática donde cada color danza sobre su melena.",
    "El rey de la selva cobra vida en una explosión de colores vibrantes, representando fuerza y vitalidad."
]

# 4. Categorías (en orden inverso)
categorias = [
    "retratos", "paisajes", "religioso", "paisajes", "retratos", 
    "religioso", "paisajes", "naturaleza", "religioso", "religioso", 
    "paisajes", "paisajes", "paisajes", "naturaleza", "naturaleza", 
    "naturaleza", "paisajes", "paisajes", "retratos", "retratos", 
    "religioso", "religioso", "religioso", "religioso", "naturaleza", "naturaleza"
]

# Generar HTML de la galería
items_html = ""
for i in range(26):
    img_url = f"https://i.ibb.co/{ids[i]}/image.jpg"
    img_url_png = f"https://i.ibb.co/{ids[i]}/image.png"
    items_html += f"""
                <div class="gallery-item" data-category="{categorias[i]}">
                    <img src="{img_url}" onerror="this.src='{img_url_png}'" alt="{titulos[i]}">
                    <div class="overlay">
                        <h3>{titulos[i]}</h3>
                        <p>{descripciones[i]}</p>
                    </div>
                </div>"""

html_galeria = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galería Completa - Lienzos del Alma</title>
    <link rel="stylesheet" href="css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <a href="index.html" class="logo">Lienzos del Alma</a>
        <ul class="nav-links">
            <li><a href="index.html">Inicio</a></li>
            <li><a href="galeria.html">Galería</a></li>
            <li><a href="sobre-el-artista.html">El Artista</a></li>
        </ul>
    </nav>
    <section class="gallery-section">
        <div class="container">
            <h1>Galería Completa</h1>
            <p class="gallery-intro">26 obras que capturan la esencia del alma artística de Bernardo León Mejía Rivera</p>
            <div class="filter-buttons">
                <button class="filter-btn active" data-filter="all">Todas</button>
                <button class="filter-btn" data-filter="religioso">Religioso</button>
                <button class="filter-btn" data-filter="retratos">Retratos</button>
                <button class="filter-btn" data-filter="naturaleza">Naturaleza</button>
                <button class="filter-btn" data-filter="paisajes">Paisajes</button>
            </div>
            <div class="full-gallery">
                {items_html}
            </div>
        </div>
    </section>
    <footer>
        <div class="container">
            <p>&copy; 2026 Lienzos del Alma - Homenaje a Bernardo León Mejía Rivera</p>
            <p>Copacabana, Antioquia, Colombia</p>
        </div>
    </footer>
    <script>
        const filterBtns = document.querySelectorAll('.filter-btn');
        const galleryItems = document.querySelectorAll('.gallery-item');
        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const filter = btn.getAttribute('data-filter');
                galleryItems.forEach(item => {{
                    item.style.display = (filter === 'all' || item.getAttribute('data-category') === filter) ? 'block' : 'none';
                }});
            }});
        }});
    </script>
</body>
</html>"""

with open("galeria.html", "w", encoding="utf-8") as f:
    f.write(html_galeria)

# Generar index.html con las primeras 4 obras
preview_items = ""
for i in range(4):
    img_url = f"https://i.ibb.co/{ids[i]}/image.jpg"
    img_url_png = f"https://i.ibb.co/{ids[i]}/image.png"
    preview_items += f"""
                <div class="artwork-card">
                    <img src="{img_url}" onerror="this.src='{img_url_png}'" alt="{titulos[i]}">
                    <h3>{titulos[i]}</h3>
                    <p>{descripciones[i]}</p>
                </div>"""

html_index = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lienzos del Alma - Bernardo León Mejía Rivera</title>
    <link rel="stylesheet" href="css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="hero">
        <div class="hero-content">
            <h1 class="title">Lienzos del Alma</h1>
            <p class="subtitle">Bernardo León Mejía Rivera</p>
            <p class="location">Copacabana, Antioquia - Colombia</p>
            <a href="galeria.html" class="cta-button">Explorar Galería</a>
        </div>
    </header>
    <section class="intro">
        <div class="container">
            <h2>El Arte que Nace del Corazón</h2>
            <p>Cada obra es un testimonio vivo de fe, esperanza y amor por la vida. El maestro Bernardo León Mejía Rivera nos invita a contemplar el mundo a través de sus ojos llenos de sensibilidad y espiritualidad.</p>
        </div>
    </section>
    <section class="preview">
        <div class="container">
            <h2>Obras Destacadas</h2>
            <div class="gallery-grid">
                {preview_items}
            </div>
            <div style="text-align: center; margin-top: 2rem;">
                <a href="galeria.html" class="view-all">Ver Galería Completa →</a>
            </div>
        </div>
    </section>
    <footer>
        <div class="container">
            <p>&copy; 2026 Lienzos del Alma - Homenaje a Bernardo León Mejía Rivera</p>
            <p>Copacabana, Antioquia, Colombia</p>
        </div>
    </footer>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_index)

print("✅ ¡ÉXITO TOTAL!")
print("✅ Las 26 imágenes están en ORDEN INVERSO (como pediste).")
print("✅ El truco 'onerror' cargará la imagen automáticamente (.jpg o .png).")
print("✅ Las 26 descripciones hermosas y únicas están perfectamente asignadas.")
print("🚀 Ahora ejecuta: git add . && git commit -m 'Galería final perfecta con orden inverso' && git push origin main")

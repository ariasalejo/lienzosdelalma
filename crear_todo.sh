#!/bin/bash

echo "🎨 Iniciando la creación de 'Lienzos del Alma'..."

# 1. Crear carpetas
mkdir -p css images

# 2. Crear index.html
cat << 'EOF' > index.html
<!DOCTYPE html>
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
                <div class="artwork-card"><img src="images/obra_01.jpg" alt="Obra 1"><h3>Obra Maestra 1</h3><p>Una hermosa creación que refleja la sensibilidad del maestro.</p></div>
                <div class="artwork-card"><img src="images/obra_02.jpg" alt="Obra 2"><h3>Obra Maestra 2</h3><p>Una hermosa creación que refleja la sensibilidad del maestro.</p></div>
                <div class="artwork-card"><img src="images/obra_03.jpg" alt="Obra 3"><h3>Obra Maestra 3</h3><p>Una hermosa creación que refleja la sensibilidad del maestro.</p></div>
                <div class="artwork-card"><img src="images/obra_04.jpg" alt="Obra 4"><h3>Obra Maestra 4</h3><p>Una hermosa creación que refleja la sensibilidad del maestro.</p></div>
            </div>
            <div style="text-align: center; margin-top: 2rem;"><a href="galeria.html" class="view-all">Ver Galería Completa →</a></div>
        </div>
    </section>
    <footer>
        <div class="container">
            <p>&copy; 2026 Lienzos del Alma - Homenaje a Bernardo León Mejía Rivera</p>
            <p>Copacabana, Antioquia, Colombia</p>
        </div>
    </footer>
</body>
</html>
EOF

# 3. Crear galeria.html (con bucle inteligente para las 26 obras)
cat << 'HEADER' > galeria.html
<!DOCTYPE html>
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
HEADER

categorias=("religioso" "retratos" "naturaleza" "paisajes")
for i in {1..26}; do
    num=$(printf "%02d" $i)
    cat_idx=$(( (i - 1) % 4 ))
    categoria=${categorias[$cat_idx]}
    cat << OBRA >> galeria.html
                <div class="gallery-item" data-category="${categoria}">
                    <img src="images/obra_${num}.jpg" alt="Obra ${i}">
                    <div class="overlay">
                        <h3>Obra Maestra ${i}</h3>
                        <p>Una hermosa creación que refleja la sensibilidad, la fe y el talento del maestro Bernardo León Mejía Rivera.</p>
                    </div>
                </div>
OBRA
done

cat << 'FOOTER' >> galeria.html
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
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const filter = btn.getAttribute('data-filter');
                galleryItems.forEach(item => {
                    item.style.display = (filter === 'all' || item.getAttribute('data-category') === filter) ? 'block' : 'none';
                });
            });
        });
    </script>
</body>
</html>
FOOTER

# 4. Crear sobre-el-artista.html
cat << 'EOF' > sobre-el-artista.html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sobre el Artista - Lienzos del Alma</title>
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
    <section class="artist-section">
        <div class="container">
            <h1>Bernardo León Mejía Rivera</h1>
            <div class="artist-content">
                <div class="artist-info">
                    <h2>El Maestro de Copacabana</h2>
                    <p>Nacido en Copacabana, Antioquia, Colombia, Bernardo León Mejía Rivera ha dedicado su vida a capturar la belleza del mundo a través de sus pinceles y pasteles.</p>
                    <h3>Su Arte</h3>
                    <p>Su obra abarca múltiples temáticas: desde el arte religioso que refleja su profunda fe, hasta paisajes que celebran la belleza de su tierra antioqueña.</p>
                    <h3>Técnicas</h3>
                    <ul><li>Pasteles al óleo y secos</li><li>Colores y lápices de color</li><li>Dibujo detallado</li><li>Pintura en múltiples materiales</li></ul>
                </div>
            </div>
            <div class="tribute-message">
                <h2>Un Homenaje Merecido</h2>
                <p>Esta galería digital nace como un tributo al talento y la sensibilidad de un artista que merece ser reconocido. Cada obra es testigo de años de dedicación, práctica y amor por el arte.</p>
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
</html>
EOF

# 5. Crear css/styles.css
cat << 'EOF' > css/styles.css
* { margin: 0; padding: 0; box-sizing: border-box; }
:root { --primary-color: #8B4513; --secondary-color: #D4A574; --accent-color: #2C5F2D; --light-bg: #FDF8F3; --dark-text: #2C2416; }
body { font-family: 'Lato', sans-serif; color: var(--dark-text); line-height: 1.6; background-color: var(--light-bg); }
h1, h2, h3 { font-family: 'Playfair Display', serif; }
.navbar { background: white; padding: 1rem 2rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 100; display: flex; justify-content: space-between; align-items: center; }
.logo { font-family: 'Playfair Display', serif; font-size: 1.5rem; color: var(--primary-color); text-decoration: none; font-weight: 700; }
.nav-links { list-style: none; display: flex; gap: 2rem; }
.nav-links a { text-decoration: none; color: var(--dark-text); font-weight: 500; transition: color 0.3s; }
.nav-links a:hover { color: var(--primary-color); }
.hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 80vh; display: flex; align-items: center; justify-content: center; text-align: center; color: white; }
.hero-content { padding: 2rem; animation: fadeIn 1s ease; }
.title { font-size: 4rem; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
.subtitle { font-size: 2rem; font-weight: 300; margin-bottom: 0.5rem; }
.location { font-size: 1.2rem; font-style: italic; margin-bottom: 2rem; }
.cta-button { display: inline-block; padding: 1rem 2.5rem; background: white; color: var(--primary-color); text-decoration: none; border-radius: 50px; font-weight: 700; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
.cta-button:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0,0,0,0.3); }
.intro, .preview, .gallery-section, .artist-section { padding: 5rem 2rem; }
.intro { background: white; text-align: center; }
.intro h2, .preview h2, .gallery-section h1, .artist-section h1 { font-size: 2.5rem; color: var(--primary-color); margin-bottom: 2rem; text-align: center; }
.intro p { max-width: 800px; margin: 0 auto 1.5rem; font-size: 1.2rem; line-height: 1.8; }
.container { max-width: 1200px; margin: 0 auto; }
.gallery-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 3rem; }
.artwork-card { background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center; transition: transform 0.3s ease; }
.artwork-card:hover { transform: translateY(-10px); }
.artwork-card img { width: 100%; height: 250px; object-fit: cover; border-radius: 10px; margin-bottom: 1rem; }
.artwork-card h3 { color: var(--primary-color); margin-bottom: 0.5rem; }
.view-all { display: inline-block; padding: 1rem 2rem; background: var(--primary-color); color: white; text-decoration: none; border-radius: 5px; font-weight: 700; transition: all 0.3s ease; }
.view-all:hover { background: var(--accent-color); }
.gallery-intro { text-align: center; font-size: 1.2rem; margin-bottom: 2rem; color: #666; }
.filter-buttons { display: flex; justify-content: center; gap: 1rem; margin-bottom: 3rem; flex-wrap: wrap; }
.filter-btn { padding: 0.75rem 1.5rem; border: 2px solid var(--primary-color); background: white; color: var(--primary-color); border-radius: 25px; cursor: pointer; font-weight: 600; transition: all 0.3s; }
.filter-btn:hover, .filter-btn.active { background: var(--primary-color); color: white; }
.full-gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2rem; }
.gallery-item { position: relative; overflow: hidden; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); cursor: pointer; }
.gallery-item img { width: 100%; height: 350px; object-fit: cover; transition: transform 0.5s ease; }
.gallery-item:hover img { transform: scale(1.05); }
.overlay { position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); color: white; padding: 2rem 1.5rem 1.5rem; transform: translateY(100%); transition: transform 0.3s ease; }
.gallery-item:hover .overlay { transform: translateY(0); }
.overlay h3 { font-size: 1.3rem; margin-bottom: 0.5rem; }
.overlay p { font-size: 0.95rem; line-height: 1.5; }
.artist-content { background: white; padding: 3rem; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin-bottom: 3rem; }
.artist-info h2 { color: var(--primary-color); margin-bottom: 1.5rem; text-align: left; }
.artist-info h3 { color: var(--accent-color); margin: 2rem 0 1rem; }
.artist-info ul { margin-left: 2rem; margin-bottom: 1rem; }
.tribute-message { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 3rem; border-radius: 15px; text-align: center; }
.tribute-message h2 { color: white; margin-bottom: 1.5rem; }
footer { background: var(--dark-text); color: white; text-align: center; padding: 2rem; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
@media (max-width: 768px) { .title { font-size: 2.5rem; } .nav-links { gap: 1rem; font-size: 0.9rem; } .full-gallery { grid-template-columns: 1fr; } }
EOF

# 6. Crear README.md
cat << 'EOF' > README.md
# 🎨 Lienzos del Alma
Galería Digital de Bernardo León Mejía Rivera.
Un homenaje al arte, la sensibilidad y el legado del maestro de Copacabana, Antioquia, Colombia.
EOF

echo "✅ ¡TODOS LOS ARCHIVOS HAN SIDO CREADOS EXITOSAMENTE!"
echo "📁 Ahora solo debes colocar tus 26 imágenes en la carpeta 'images/' con estos nombres exactos:"
echo "   obra_01.jpg, obra_02.jpg, obra_03.jpg ... hasta obra_26.jpg"
echo "🚀 Luego ejecuta: git add . && git commit -m 'Sitio web completo generado' && git push origin main"

#!/bin/bash

set -e

echo "🎨 LIENZOS DEL ALMA"
echo "🌎 Construyendo galería internacional..."
echo

mkdir -p css js

cat > index.html <<'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">

  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >

  <title>
    Lienzos del Alma | Bernardo León Mejía Rivera
  </title>

  <meta
    name="description"
    content="Galería digital dedicada a la obra artística de Bernardo León Mejía Rivera, desde Copacabana, Antioquia, Colombia."
  >

  <meta
    name="author"
    content="Lienzos del Alma"
  >

  <meta
    name="theme-color"
    content="#17120e"
  >

  <meta
    property="og:title"
    content="Lienzos del Alma — Bernardo León Mejía Rivera"
  >

  <meta
    property="og:description"
    content="Una galería digital de arte desde Copacabana, Antioquia, Colombia."
  >

  <meta
    property="og:type"
    content="website"
  >

  <meta
    property="og:locale"
    content="es_CO"
  >

  <link rel="stylesheet" href="css/style.css">

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "VisualArtwork",
    "name": "Lienzos del Alma",
    "creator": {
      "@type": "Person",
      "name": "Bernardo León Mejía Rivera"
    },
    "locationCreated": {
      "@type": "Place",
      "name": "Copacabana, Antioquia, Colombia"
    },
    "artform": "Visual Art"
  }
  </script>
</head>

<body>

<header class="site-header">

  <a class="brand" href="#inicio">
    <span class="brand-mark">L</span>

    <span>
      <strong>Lienzos del Alma</strong>
      <small>Bernardo León Mejía Rivera</small>
    </span>
  </a>

  <nav>
    <a href="#inicio">Inicio</a>
    <a href="#galeria">Galería</a>
    <a href="#artista">El Artista</a>
  </nav>

  <button
    id="language"
    class="language"
    type="button"
    aria-label="Cambiar idioma"
  >
    EN
  </button>

</header>


<main>

<section id="inicio" class="hero">

  <div class="hero-glow"></div>

  <div class="hero-content">

    <p class="eyebrow">
      COPACABANA · ANTIOQUIA · COLOMBIA
    </p>

    <h1>
      Lienzos<br>
      <em>del Alma</em>
    </h1>

    <p
      class="hero-text"
      data-es="Una colección de obras nacidas de la sensibilidad, la fe, la naturaleza y el amor por el arte."
      data-en="A collection of works born from sensitivity, faith, nature and a love for art."
    >
      Una colección de obras nacidas de la sensibilidad,
      la fe, la naturaleza y el amor por el arte.
    </p>

    <div class="hero-actions">

      <a class="button primary" href="#galeria">
        Explorar la colección
      </a>

      <a class="button ghost" href="#artista">
        Conocer al artista
      </a>

    </div>

    <div class="hero-meta">

      <div>
        <strong>26</strong>
        <span>obras</span>
      </div>

      <div>
        <strong>∞</strong>
        <span>historias</span>
      </div>

      <div>
        <strong>CO</strong>
        <span>Colombia</span>
      </div>

    </div>

  </div>

  <div class="hero-art">

    <div class="hero-frame">

      <img
        src="https://i.ibb.co/rRJ3fGND/IMG-20260816-WA0008.jpg"
        alt="Obra artística de Bernardo León Mejía Rivera"
      >

    </div>

  </div>

</section>


<section class="intro">

  <p class="eyebrow">EL ARTE COMO MEMORIA</p>

  <h2>
    Cada obra guarda<br>
    <em>una historia.</em>
  </h2>

  <p>
    Lienzos del Alma nace como un espacio digital para conservar,
    contemplar y compartir la obra de Bernardo León Mejía Rivera.
    Desde Copacabana, Antioquia, estas obras encuentran una nueva
    ventana hacia el mundo.
  </p>

</section>


<section id="galeria" class="gallery-section">

  <div class="section-heading">

    <div>
      <p class="eyebrow">LA COLECCIÓN</p>

      <h2>
        Obras
        <em>destacadas</em>
      </h2>
    </div>

    <p>
      Explora las 26 obras de la colección.
    </p>

  </div>


  <div class="filters">

    <button class="filter active" data-filter="all">
      Todas
    </button>

    <button class="filter" data-filter="religioso">
      Religioso
    </button>

    <button class="filter" data-filter="retratos">
      Retratos
    </button>

    <button class="filter" data-filter="naturaleza">
      Naturaleza
    </button>

    <button class="filter" data-filter="paisajes">
      Paisajes
    </button>

  </div>


  <div id="gallery" class="gallery"></div>

</section>


<section id="artista" class="artist">

  <div class="artist-image">

    <div class="artist-card">

      <span>BERNARDO</span>

      <strong>
        LEÓN<br>
        MEJÍA<br>
        RIVERA
      </strong>

      <small>
        COPACABANA · ANTIOQUIA
      </small>

    </div>

  </div>


  <div class="artist-content">

    <p class="eyebrow">
      EL ARTISTA
    </p>

    <h2>
      El maestro de<br>
      <em>Copacabana</em>
    </h2>

    <p>
      Bernardo León Mejía Rivera ha dedicado su expresión
      artística a explorar diferentes formas, colores y temas.
      Su colección reúne escenas religiosas, retratos,
      animales, naturaleza y paisajes.
    </p>

    <p>
      Su trabajo combina sensibilidad, observación y dedicación,
      dando lugar a imágenes que invitan a detenerse y mirar.
    </p>

    <div class="techniques">

      <span>Pasteles al óleo</span>
      <span>Pasteles secos</span>
      <span>Lápices de color</span>
      <span>Dibujo</span>
      <span>Pintura</span>

    </div>

  </div>

</section>


<section class="quote">

  <div class="quote-line"></div>

  <blockquote>
    “El arte también es una forma
    de conservar aquello que amamos.”
  </blockquote>

  <p>
    LIENZOS DEL ALMA · COPACABANA, COLOMBIA
  </p>

</section>

</main>


<footer>

  <div class="footer-brand">
    <strong>Lienzos del Alma</strong>
    <span>
      Bernardo León Mejía Rivera
    </span>
  </div>

  <div>
    Copacabana · Antioquia · Colombia
  </div>

  <div>
    © 2026 Lienzos del Alma
  </div>

</footer>


<div
  id="lightbox"
  class="lightbox"
  aria-hidden="true"
>

  <button
    id="closeLightbox"
    class="close"
    aria-label="Cerrar"
  >
    ×
  </button>

  <button
    id="previous"
    class="lightbox-nav previous"
    aria-label="Obra anterior"
  >
    ‹
  </button>

  <figure>

    <img
      id="lightboxImage"
      src=""
      alt=""
    >

    <figcaption>

      <strong id="lightboxTitle"></strong>

      <span id="lightboxDescription"></span>

    </figcaption>

  </figure>

  <button
    id="next"
    class="lightbox-nav next"
    aria-label="Obra siguiente"
  >
    ›
  </button>

</div>


<script src="js/app.js"></script>

</body>
</html>
EOF


cat > js/app.js <<'EOF'
const works = [

  {
    id: 1,
    title: "Mirada de infancia",
    category: "retratos",
    image: "https://i.ibb.co/rRJ3fGND/IMG-20260816-WA0008.jpg",
    description: "Retrato infantil realizado con una delicada exploración del color."
  },

  {
    id: 2,
    title: "Pasión y esperanza",
    category: "religioso",
    image: "https://i.ibb.co/Ng3Z6S9K/IMG-20260816-WA0006.jpg",
    description: "Composición de carácter religioso llena de símbolos y color."
  },

  {
    id: 3,
    title: "El Buen Pastor",
    category: "religioso",
    image: "https://i.ibb.co/1NfhvhG/IMG-20260816-WA0009.jpg",
    description: "Interpretación artística de una escena bíblica."
  },

  {
    id: 4,
    title: "Oración",
    category: "religioso",
    image: "https://i.ibb.co/93mzGN93/IMG-20260816-WA0010.jpg",
    description: "Retrato de una figura infantil en actitud de oración."
  },

  {
    id: 5,
    title: "Naturaleza en color",
    category: "naturaleza",
    image: "https://i.ibb.co/LdmHB3WW/IMG-20260816-WA0011.jpg",
    description: "Una interpretación vibrante de la fuerza de la naturaleza."
  },

  {
    id: 6,
    title: "Camino de luz",
    category: "paisajes",
    image: "https://i.ibb.co/gMf2frdM/IMG-20260816-WA0012.jpg",
    description: "Paisaje luminoso donde naturaleza y arquitectura se encuentran."
  },

  {
    id: 7,
    title: "Noche sobre el agua",
    category: "paisajes",
    image: "https://i.ibb.co/h19PhnHZ/IMG-20260816-WA0005.jpg",
    description: "Paisaje nocturno construido alrededor del agua y la luz."
  },


  {
    id: 9,
    title: "Aves de colores",
    category: "naturaleza",
    image: "https://i.ibb.co/Ps0Hbztc/IMG-20260816-WA0014.jpg",
    description: "Observación de aves en una composición llena de color."
  },

  {
    id: 10,
    title: "Encuentro",
    category: "naturaleza",
    image: "https://i.ibb.co/chVpBYzQ/IMG-20260816-WA0015.jpg",
    description: "Dos aves protagonizan una escena íntima y delicada."
  },

  {
    id: 11,
    title: "Flamencos al atardecer",
    category: "naturaleza",
    image: "https://i.ibb.co/zHFcFYrL/IMG-20260816-WA0017.jpg",
    description: "Fauna y paisaje reunidos alrededor de la luz del atardecer."
  },

  {
    id: 12,
    title: "Luz entre las sombras",
    category: "religioso",
    image: "https://i.ibb.co/RtRY47P/IMG-20260816-WA0007.jpg",
    description: "Interpretación simbólica de una escena religiosa."
  },

  {
    id: 13,
    title: "Encuentro espiritual",
    category: "religioso",
    image: "https://i.ibb.co/VpzpjYpy/IMG-20260816-WA0018.jpg",
    description: "Una composición de inspiración espiritual."
  },

  {
    id: 14,
    title: "Colibríes y flores",
    category: "naturaleza",
    image: "https://i.ibb.co/CKX7KF3N/IMG-20260816-WA0016.jpg",
    description: "Color, movimiento y naturaleza en una misma escena."
  },

  {
    id: 15,
    title: "Ave sobre el agua",
    category: "naturaleza",
    image: "https://i.ibb.co/JWzkJbcP/IMG-20260816-WA0019.jpg",
    description: "Estudio de fauna junto a un paisaje acuático."
  },

  {
    id: 16,
    title: "El Pastor y el cordero",
    category: "religioso",
    image: "https://i.ibb.co/HpP1FvhD/IMG-20260816-WA0021.jpg",
    description: "Escena de inspiración cristiana."
  },

  {
    id: 17,
    title: "Vuelo",
    category: "naturaleza",
    image: "https://i.ibb.co/tTQzDZw4/IMG-20260816-WA0022.jpg",
    description: "Estudio de un ave en pleno vuelo."
  },

  {
    id: 18,
    title: "Encuentro junto al mar",
    category: "religioso",
    image: "https://i.ibb.co/SXJf4NbB/IMG-20260816-WA0020.jpg",
    description: "Paisaje de inspiración espiritual."
  },

  {
    id: 19,
    title: "Horizonte",
    category: "paisajes",
    image: "https://i.ibb.co/QvbkQ9dW/IMG-20260819-WA0016.jpg",
    description: "Paisaje abierto donde cielo, agua y tierra dialogan."
  },

  {
    id: 20,
    title: "Pequeños habitantes",
    category: "naturaleza",
    image: "https://i.ibb.co/XrXSzVK1/IMG-20260820-WA0014.jpg",
    description: "Estudio de aves y vegetación."
  },

  {
    id: 21,
    title: "Paisaje de agua",
    category: "paisajes",
    image: "https://i.ibb.co/h1fbX5bK/IMG-20260824-WA0001.jpg",
    description: "Paisaje natural trabajado con una paleta luminosa."
  },

  {
    id: 22,
    title: "Memoria del paisaje",
    category: "paisajes",
    image: "https://i.ibb.co/dw9mW6m2/IMG-20260823-WA0006.jpg",
    description: "Una composición de naturaleza y paisaje."
  },

  {
    id: 23,
    title: "Lago bajo la luna",
    category: "paisajes",
    image: "https://i.ibb.co/HL5vWGHh/IMG-20260825-WA0020.jpg",
    description: "Paisaje nocturno construido alrededor de agua y luz."
  },

  {
    id: 24,
    title: "Naturaleza en contemplación",
    category: "paisajes",
    image: "https://i.ibb.co/GQG4bgVD/IMG-20260826-WA0004.jpg",
    description: "Una interpretación personal del paisaje."
  },

  {
    id: 25,
    title: "Contemplación",
    category: "religioso",
    image: "https://i.ibb.co/q33TJhW5/IMG-20260829-WA0004.jpg",
    description: "Retrato de inspiración religiosa."
  },

  {
    id: 26,
    title: "Espíritu de la montaña",
    category: "naturaleza",
    image: "https://i.ibb.co/GQV8DxDw/IMG-20260916-WA0003.jpg",
    description: "Fauna y paisaje unidos en una composición simbólica."
  }

];


const gallery = document.getElementById("gallery");

const filters = document.querySelectorAll(".filter");

const lightbox = document.getElementById("lightbox");

const lightboxImage =
  document.getElementById("lightboxImage");

const lightboxTitle =
  document.getElementById("lightboxTitle");

const lightboxDescription =
  document.getElementById("lightboxDescription");

let currentIndex = 0;

let visibleWorks = [...works];


function renderGallery(list = works) {

  visibleWorks = list;

  gallery.innerHTML = list.map((work, index) => `

    <article
      class="art-card"
      data-category="${work.category}"
      data-index="${index}"
    >

      <button
        class="art-image"
        aria-label="Ver ${work.title}"
      >

        <img
          src="${work.image}"
          alt="${work.title} — Bernardo León Mejía Rivera"
          loading="lazy"
        >

        <span class="art-number">
          ${String(work.id).padStart(2, "0")}
        </span>

        <span class="view">
          Ver obra
        </span>

      </button>

      <div class="art-info">

        <span class="category">
          ${work.category}
        </span>

        <h3>
          ${work.title}
        </h3>

        <p>
          ${work.description}
        </p>

      </div>

    </article>

  `).join("");

  document
    .querySelectorAll(".art-image")
    .forEach((button, index) => {

      button.addEventListener("click", () => {

        openLightbox(index);

      });

    });

}


function openLightbox(index) {

  currentIndex = index;

  const work = visibleWorks[currentIndex];

  lightboxImage.src = work.image;

  lightboxImage.alt = work.title;

  lightboxTitle.textContent =
    `${String(work.id).padStart(2, "0")} · ${work.title}`;

  lightboxDescription.textContent =
    work.description;

  lightbox.classList.add("open");

  lightbox.setAttribute("aria-hidden", "false");

  document.body.classList.add("no-scroll");

}


function closeLightbox() {

  lightbox.classList.remove("open");

  lightbox.setAttribute("aria-hidden", "true");

  document.body.classList.remove("no-scroll");

}


function move(direction) {

  currentIndex =
    (currentIndex + direction + visibleWorks.length)
    % visibleWorks.length;

  openLightbox(currentIndex);

}


filters.forEach(filter => {

  filter.addEventListener("click", () => {

    filters.forEach(item =>
      item.classList.remove("active")
    );

    filter.classList.add("active");

    const value = filter.dataset.filter;

    if (value === "all") {

      renderGallery(works);

    } else {

      renderGallery(
        works.filter(work =>
          work.category === value
        )
      );

    }

  });

});


document
  .getElementById("closeLightbox")
  .addEventListener("click", closeLightbox);


document
  .getElementById("previous")
  .addEventListener("click", () => move(-1));


document
  .getElementById("next")
  .addEventListener("click", () => move(1));


document.addEventListener("keydown", event => {

  if (!lightbox.classList.contains("open")) {
    return;
  }

  if (event.key === "Escape") {
    closeLightbox();
  }

  if (event.key === "ArrowLeft") {
    move(-1);
  }

  if (event.key === "ArrowRight") {
    move(1);
  }

});


lightbox.addEventListener("click", event => {

  if (event.target === lightbox) {
    closeLightbox();
  }

});


const languageButton =
  document.getElementById("language");

let english = false;


languageButton.addEventListener("click", () => {

  english = !english;

  document
    .querySelectorAll("[data-es][data-en]")
    .forEach(element => {

      element.textContent =
        english
          ? element.dataset.en
          : element.dataset.es;

    });

  languageButton.textContent =
    english ? "ES" : "EN";

});


renderGallery();
EOF


cat > css/style.css <<'EOF'
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

:root {

  --ink: #17120e;
  --paper: #f4eee4;
  --cream: #fbf8f1;

  --gold: #b88a3b;
  --gold-light: #d6b36a;

  --terracotta: #a95636;
  --wine: #713b39;

  --green: #50634a;
  --blue: #47748b;

  --muted: #756b60;

  --line: rgba(23, 18, 14, .14);

  --shadow:
    0 25px 80px rgba(23, 18, 14, .14);

}


* {
  box-sizing: border-box;
}


html {
  scroll-behavior: smooth;
}


body {

  margin: 0;

  background:
    radial-gradient(
      circle at 10% 10%,
      rgba(184, 138, 59, .10),
      transparent 30%
    ),
    var(--paper);

  color: var(--ink);

  font-family:
    "DM Sans",
    sans-serif;

}


body.no-scroll {
  overflow: hidden;
}


.site-header {

  position: sticky;

  top: 0;

  z-index: 50;

  height: 78px;

  display: flex;

  align-items: center;

  justify-content: space-between;

  gap: 30px;

  padding: 0 5vw;

  background:
    rgba(244, 238, 228, .88);

  backdrop-filter: blur(18px);

  border-bottom:
    1px solid var(--line);

}


.brand {

  display: flex;

  align-items: center;

  gap: 12px;

  color: var(--ink);

  text-decoration: none;

}


.brand-mark {

  width: 42px;

  height: 42px;

  display: grid;

  place-items: center;

  border-radius: 50%;

  background: var(--ink);

  color: var(--gold-light);

  font-family:
    "Cormorant Garamond",
    serif;

  font-size: 25px;

}


.brand strong,
.brand small {

  display: block;

}


.brand strong {

  font-family:
    "Cormorant Garamond",
    serif;

  font-size: 21px;

}


.brand small {

  color: var(--muted);

  font-size: 10px;

  letter-spacing: .13em;

  text-transform: uppercase;

}


nav {

  display: flex;

  gap: 30px;

}


nav a {

  color: var(--ink);

  text-decoration: none;

  font-size: 13px;

}


nav a:hover {

  color: var(--terracotta);

}


.language {

  border: 1px solid var(--line);

  background: transparent;

  padding: 8px 13px;

  border-radius: 999px;

  cursor: pointer;

}


.hero {

  min-height: calc(100vh - 78px);

  display: grid;

  grid-template-columns: 1.05fr .95fr;

  align-items: center;

  gap: 7vw;

  padding: 8vw 9vw;

  position: relative;

  overflow: hidden;

}


.hero-glow {

  position: absolute;

  width: 600px;

  height: 600px;

  border-radius: 50%;

  background:
    radial-gradient(
      circle,
      rgba(184,138,59,.18),
      transparent 68%
    );

  right: -180px;

  top: -150px;

}


.hero-content {

  position: relative;

  z-index: 2;

}


.eyebrow {

  color: var(--terracotta);

  font-size: 11px;

  font-weight: 700;

  letter-spacing: .2em;

  text-transform: uppercase;

}


h1,
h2 {

  font-family:
    "Cormorant Garamond",
    serif;

  font-weight: 500;

  line-height: .9;

  margin: 20px 0;

}


h1 {

  font-size:
    clamp(70px, 10vw, 150px);

}


h2 {

  font-size:
    clamp(50px, 7vw, 100px);

}


h1 em,
h2 em {

  color: var(--terracotta);

  font-weight: 400;

}


.hero-text {

  max-width: 540px;

  color: var(--muted);

  font-size: 17px;

  line-height: 1.8;

}


.hero-actions {

  display: flex;

  gap: 12px;

  flex-wrap: wrap;

  margin-top: 32px;

}


.button {

  display: inline-block;

  padding: 15px 22px;

  border-radius: 999px;

  text-decoration: none;

  font-size: 13px;

  font-weight: 700;

}


.button.primary {

  background: var(--ink);

  color: var(--cream);

}


.button.ghost {

  border: 1px solid var(--line);

  color: var(--ink);

}


.hero-meta {

  display: flex;

  gap: 45px;

  margin-top: 55px;

}


.hero-meta strong {

  display: block;

  font-family:
    "Cormorant Garamond",
    serif;

  font-size: 34px;

}


.hero-meta span {

  color: var(--muted);

  font-size: 11px;

  text-transform: uppercase;

  letter-spacing: .12em;

}


.hero-art {

  display: flex;

  justify-content: center;

}


.hero-frame {

  width: min(440px, 90vw);

  padding: 13px;

  background: #fff;

  box-shadow: var(--shadow);

  transform: rotate(2deg);

}


.hero-frame img {

  width: 100%;

  display: block;

}


.intro {

  max-width: 800px;

  padding: 130px 25px;

  margin: auto;

  text-align: center;

}


.intro p:not(.eyebrow) {

  max-width: 650px;

  margin: auto;

  color: var(--muted);

  line-height: 1.9;

}


.gallery-section {

  padding: 100px 6vw;

  background:
    linear-gradient(
      135deg,
      rgba(255,255,255,.55),
      rgba(236,224,207,.8)
    );

}


.section-heading {

  display: flex;

  align-items: end;

  justify-content: space-between;

  gap: 40px;

  margin-bottom: 45px;

}


.section-heading > p {

  max-width: 300px;

  color: var(--muted);

  line-height: 1.7;

}


.filters {

  display: flex;

  gap: 10px;

  flex-wrap: wrap;

  margin-bottom: 35px;

}


.filter {

  border: 1px solid var(--line);

  background: transparent;

  border-radius: 999px;

  padding: 10px 17px;

  cursor: pointer;

}


.filter.active,
.filter:hover {

  background: var(--ink);

  color: white;

}


.gallery {

  display: grid;

  grid-template-columns:
    repeat(4, minmax(0, 1fr));

  gap: 26px;

}


.art-card {

  min-width: 0;

}


.art-image {

  width: 100%;

  border: 0;

  padding: 0;

  background: #fff;

  cursor: pointer;

  position: relative;

  overflow: hidden;

  aspect-ratio: 4 / 5;

}


.art-image img {

  width: 100%;

  height: 100%;

  display: block;

  object-fit: cover;

  transition:
    transform .7s ease,
    filter .7s ease;

}


.art-card:hover img {

  transform: scale(1.045);

  filter: saturate(1.08);

}


.art-number {

  position: absolute;

  left: 14px;

  top: 14px;

  padding: 6px 9px;

  background: rgba(23,18,14,.78);

  color: white;

  border-radius: 999px;

  font-size: 10px;

}


.view {

  position: absolute;

  bottom: 16px;

  right: 16px;

  background: rgba(255,255,255,.92);

  color: var(--ink);

  padding: 8px 12px;

  border-radius: 999px;

  opacity: 0;

  transform: translateY(8px);

  transition: .3s;

  font-size: 11px;

}


.art-card:hover .view {

  opacity: 1;

  transform: translateY(0);

}


.art-info {

  padding: 17px 2px 35px;

}


.category {

  color: var(--terracotta);

  font-size: 9px;

  font-weight: 700;

  letter-spacing: .16em;

  text-transform: uppercase;

}


.art-info h3 {

  font-family:
    "Cormorant Garamond",
    serif;

  font-size: 27px;

  font-weight: 600;

  margin: 7px 0;

}


.art-info p {

  color: var(--muted);

  font-size: 12px;

  line-height: 1.6;

  margin: 0;

}


.artist {

  display: grid;

  grid-template-columns: 1fr 1fr;

  min-height: 700px;

}


.artist-image {

  display: grid;

  place-items: center;

  padding: 10vw;

  background:
    linear-gradient(
      145deg,
      var(--wine),
      var(--ink)
    );

}


.artist-card {

  width: 300px;

  aspect-ratio: 4 / 5;

  padding: 35px;

  display: flex;

  flex-direction: column;

  justify-content: space-between;

  border:
    1px solid rgba(255,255,255,.25);

  color: white;

  background:
    linear-gradient(
      145deg,
      rgba(184,138,59,.25),
      rgba(0,0,0,.2)
    );

  box-shadow:
    25px 25px 0 rgba(184,138,59,.18);

}


.artist-card span {

  font-size: 10px;

  letter-spacing: .2em;

}


.artist-card strong {

  font-family:
    "Cormorant Garamond",
    serif;

  font-size: 48px;

  line-height: .85;

}


.artist-card small {

  font-size: 10px;

  letter-spacing: .12em;

}


.artist-content {

  display: flex;

  flex-direction: column;

  justify-content: center;

  padding: 9vw;

}


.artist-content p:not(.eyebrow) {

  color: var(--muted);

  line-height: 1.85;

  max-width: 580px;

}


.techniques {

  display: flex;

  flex-wrap: wrap;

  gap: 9px;

  margin-top: 20px;

}


.techniques span {

  padding: 8px 12px;

  border: 1px solid var(--line);

  border-radius: 999px;

  font-size: 10px;

}


.quote {

  text-align: center;

  padding: 150px 25px;

}


.quote-line {

  width: 50px;

  height: 2px;

  background: var(--gold);

  margin: auto;

}


blockquote {

  max-width: 800px;

  margin: 35px auto;

  font-family:
    "Cormorant Garamond",
    serif;

  font-size:
    clamp(40px, 6vw, 75px);

  line-height: .95;

}


.quote p {

  color: var(--muted);

  font-size: 10px;

  letter-spacing: .2em;

}


footer {

  display: grid;

  grid-template-columns:
    1fr 1fr 1fr;

  gap: 30px;

  padding: 40px 6vw;

  background: var(--ink);

  color: #eee4d5;

  font-size: 11px;

}


footer > div:not(.footer-brand) {

  display: flex;

  align-items: center;

}


.footer-brand strong,
.footer-brand span {

  display: block;

}


.footer-brand strong {

  font-family:
    "Cormorant Garamond",
    serif;

  font-size: 25px;

}


.footer-brand span {

  color: #aa9f91;

}


.lightbox {

  position: fixed;

  inset: 0;

  z-index: 100;

  display: none;

  place-items: center;

  padding: 40px;

  background:
    rgba(12,9,7,.96);

}


.lightbox.open {

  display: grid;

}


.lightbox figure {

  max-width: min(90vw, 900px);

  max-height: 90vh;

  margin: 0;

  display: flex;

  flex-direction: column;

  align-items: center;

}


.lightbox figure img {

  max-width: 100%;

  max-height: 76vh;

  object-fit: contain;

}


.lightbox figcaption {

  color: white;

  text-align: center;

  padding-top: 18px;

}


.lightbox figcaption strong,
.lightbox figcaption span {

  display: block;

}


.lightbox figcaption strong {

  font-family:
    "Cormorant Garamond",
    serif;

  font-size: 27px;

}


.lightbox figcaption span {

  margin-top: 4px;

  color: #aaa;

  font-size: 12px;

}


.close {

  position: absolute;

  top: 25px;

  right: 30px;

  width: 45px;

  height: 45px;

  border: 1px solid #555;

  border-radius: 50%;

  background: transparent;

  color: white;

  font-size: 30px;

  cursor: pointer;

}


.lightbox-nav {

  position: absolute;

  top: 50%;

  transform: translateY(-50%);

  border: 0;

  background: transparent;

  color: white;

  font-size: 60px;

  cursor: pointer;

}


.previous {

  left: 25px;

}


.next {

  right: 25px;

}


@media (max-width: 1000px) {

  .gallery {

    grid-template-columns:
      repeat(3, minmax(0, 1fr));

  }

}


@media (max-width: 800px) {

  .site-header {

    height: auto;

    min-height: 70px;

    padding: 12px 20px;

  }

  nav {

    display: none;

  }

  .hero {

    grid-template-columns: 1fr;

    padding: 70px 25px;

  }

  .hero-art {

    order: -1;

  }

  .section-heading {

    display: block;

  }

  .gallery {

    grid-template-columns:
      repeat(2, minmax(0, 1fr));

  }

  .artist {

    grid-template-columns: 1fr;

  }

  .artist-image {

    min-height: 550px;

  }

  footer {

    grid-template-columns: 1fr;

  }

}


@media (max-width: 520px) {

  h1 {

    font-size: 70px;

  }

  .gallery {

    grid-template-columns: 1fr;

  }

  .hero-meta {

    gap: 25px;

  }

  .lightbox {

    padding: 15px;

  }

  .lightbox-nav {

    font-size: 40px;

  }

}
EOF


cat > README.md <<'EOF'
# 🎨 Lienzos del Alma

## Bernardo León Mejía Rivera

**Copacabana · Antioquia · Colombia**

Galería digital dedicada a preservar y compartir una colección de 26 obras de Bernardo León Mejía Rivera.

---

## 🌎 La colección

La galería reúne obras relacionadas con:

- Arte religioso
- Retratos
- Naturaleza
- Aves y fauna
- Paisajes
- Escenas de inspiración espiritual

Las imágenes utilizadas en la galería proceden de la colección alojada en ImgBB.

---

## ✨ Características

- 26 obras
- Diseño responsive
- Español / English
- Filtros por temática
- Visor de obras
- Navegación con teclado
- SEO
- Open Graph
- Schema.org
- Accesibilidad
- GitHub Pages compatible
- Sin backend
- Sin base de datos
- HTML + CSS + JavaScript

---

## 🏛️ Identidad

**Lienzos del Alma** es un homenaje digital al trabajo artístico de:

**Bernardo León Mejía Rivera**

Copacabana, Antioquia, Colombia.

---

## 🚀 Publicación

Este proyecto está preparado para GitHub Pages.

Repositorio:

https://github.com/ariasalejo/lienzosdelalma

Sitio:

https://ariasalejo.github.io/lienzosdelalma/

---

## 📜 Nota

Las descripciones de las obras son textos curatoriales de presentación creados para organizar la colección. No pretenden establecer títulos oficiales de las obras cuando estos no han sido proporcionados.

---

© 2026 Lienzos del Alma
EOF


cat > .nojekyll <<'EOF'
EOF


echo
echo "=========================================="
echo "🎨 LIENZOS DEL ALMA — LISTO"
echo "=========================================="
echo
echo "26 obras integradas"
echo "Galería responsive"
echo "Lightbox"
echo "Filtros"
echo "SEO"
echo "Open Graph"
echo "Schema.org"
echo "Español / English"
echo
echo "Ejecuta:"
echo
echo "git status"
echo
echo "Luego:"
echo
echo "git add ."
echo "git commit -m 'feat: transformar galeria en experiencia artistica internacional'"
echo "git push origin main"
echo

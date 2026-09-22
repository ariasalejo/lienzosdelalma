from pathlib import Path
import re
import html
import shutil
import json

ROOT = Path(__file__).resolve().parent
APP = ROOT / "js" / "app.js"
OBRAS = ROOT / "obras"
CSS = ROOT / "css"
JS = ROOT / "js"

OBRAS.mkdir(exist_ok=True)
CSS.mkdir(exist_ok=True)
JS.mkdir(exist_ok=True)

ARTISTA = "Bernardo León Mejía Rivera"
COLECCION = "Lienzos del Alma"
LUGAR = "Copacabana · Antioquia · Colombia"

# ============================================================
# FUENTE DE IMÁGENES
# ============================================================

source = APP.read_text(encoding="utf-8", errors="ignore")

def extract_string(block, key):
    patterns = [
        rf'["\']{re.escape(key)}["\']\s*:\s*["\'](.*?)["\']',
        rf'\b{re.escape(key)}\s*:\s*["\'](.*?)["\']',
    ]

    for pattern in patterns:
        m = re.search(pattern, block, re.S)
        if m:
            return m.group(1).replace("\\/", "/").strip()

    return ""

def extract_works(text):
    """
    Extrae objetos JS aunque utilicen:
      id: "01"
      title: "..."
      category: "..."
      image: "..."
      description: "..."
    o claves entre comillas.
    """

    found = []

    # Objetos con llaves relativamente simples.
    blocks = re.findall(r'\{(?:(?!\n\s*\}).){0,5000}\}', text, re.S)

    for block in blocks:
        image = extract_string(block, "image")
        if not image:
            image = extract_string(block, "imagen")

        title = extract_string(block, "title")
        if not title:
            title = extract_string(block, "titulo")

        category = extract_string(block, "category")
        if not category:
            category = extract_string(block, "categoria")

        description = extract_string(block, "description")
        if not description:
            description = extract_string(block, "descripcion")

        ident = extract_string(block, "id")

        if image and title:
            if not ident:
                # Buscar un número dentro del bloque.
                m = re.search(r'\b(0?[1-9]|1\d|2[0-6])\b', block)
                ident = m.group(1) if m else ""

            if ident:
                ident = ident.zfill(2)

            found.append({
                "id": ident,
                "title": title,
                "category": category or "Colección",
                "image": image,
                "description": description or "",
            })

    # Eliminar duplicados por ID/URL
    unique = {}
    for w in found:
        if not w["id"]:
            continue

        if w["id"] == "08":
            continue

        unique[w["id"]] = w

    return sorted(unique.values(), key=lambda x: int(x["id"]))


works = extract_works(source)

# Si la estructura de app.js no permite extracción automática,
# buscar URLs conocidas directamente.
if not works:
    urls = re.findall(
        r'https?://[^"\']+\.(?:jpg|jpeg|png|webp)(?:\?[^"\']*)?',
        source,
        re.I
    )

    for n, url in enumerate(urls, 1):
        if n == 8:
            continue

        works.append({
            "id": str(n).zfill(2),
            "title": f"Obra {n:02d}",
            "category": "Colección",
            "image": url,
            "description": "",
        })

# Nunca permitir obra 08.
works = [w for w in works if w["id"] != "08"]

# ============================================================
# TEXTOS CURATORIALES
# ============================================================

CURATORIAL = {
    "01": {
        "intro": "Retrato infantil realizado con una delicada exploración del color.",
        "seeing": "Retrato vertical de un niño de cabello claro y ojos azules, vestido en tonos violetas. El rostro ocupa buena parte de la composición y se recorta sobre un fondo luminoso de verdes y azules suaves.",
        "reading": "La frontalidad del retrato concentra la atención en la mirada y en la presencia del niño. La combinación de violetas, azules y verdes construye una atmósfera íntima y serena.",
        "keywords": ["infancia", "retrato", "mirada", "color", "intimidad"],
    }
}

DEFAULT_CURATORIAL = {
    "intro": "Una obra que forma parte del archivo artístico de Bernardo León Mejía Rivera.",
    "seeing": "La composición reúne formas, colores y elementos que construyen una escena propia dentro del universo visual del artista.",
    "reading": "La obra invita a detener la mirada y recorrer sus relaciones de color, espacio y materia sin apresurar una interpretación única.",
    "keywords": ["color", "memoria", "contemplación", "paisaje", "obra"],
}

def esc(value):
    return html.escape(str(value), quote=True)

def curatorial(w):
    return CURATORIAL.get(w["id"], DEFAULT_CURATORIAL)

def image_url(w):
    return w["image"]

# ============================================================
# CSS — MUSEO
# ============================================================

CSS_CONTENT = r'''
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Inter:wght@400;500;600&display=swap');

:root{
  --paper:#f3efe7;
  --paper-deep:#e7e0d4;
  --ink:#171714;
  --muted:#716c63;
  --line:rgba(23,23,20,.14);
  --soft-line:rgba(23,23,20,.075);
  --bronze:#94764c;
  --night:#11110f;
  --night-text:#eee9df;
  --serif:"Cormorant Garamond", Georgia, serif;
  --sans:"Inter", Arial, sans-serif;
  --wide:1400px;
  --reading:1040px;
}

*,
*::before,
*::after{
  box-sizing:border-box;
}

html{
  background:var(--paper);
  color:var(--ink);
  scroll-behavior:smooth;
}

body{
  margin:0;
  background:var(--paper);
  color:var(--ink);
  font-family:var(--sans);
  -webkit-font-smoothing:antialiased;
}

img{
  display:block;
  max-width:100%;
}

a{
  color:inherit;
  text-decoration:none;
}

button{
  font:inherit;
}

/* =========================================================
   HEADER
   ========================================================= */

.site-header{
  height:70px;
  padding:0 clamp(20px,4vw,58px);

  display:flex;
  align-items:center;
  justify-content:space-between;

  border-bottom:1px solid var(--soft-line);

  background:rgba(243,239,231,.95);

  position:sticky;
  top:0;
  z-index:100;

  backdrop-filter:blur(16px);
  -webkit-backdrop-filter:blur(16px);
}

.wordmark{
  display:flex;
  flex-direction:column;
  gap:1px;
}

.wordmark-main{
  font-family:var(--serif);
  font-size:19px;
  font-weight:500;
  letter-spacing:.06em;
}

.wordmark-sub{
  font-size:7px;
  letter-spacing:.18em;
  text-transform:uppercase;
  color:var(--muted);
}

.header-link{
  color:var(--muted);
  font-size:9px;
  letter-spacing:.15em;
  text-transform:uppercase;
}

.header-link:hover{
  color:var(--bronze);
}

/* =========================================================
   HOME
   ========================================================= */

.home{
  min-height:calc(100vh - 70px);
}

.home-hero{
  width:min(var(--wide),92vw);
  min-height:calc(100vh - 70px);
  margin:auto;

  display:grid;
  grid-template-columns:minmax(0,1.1fr) minmax(300px,.9fr);
  align-items:center;
  gap:8vw;

  padding:6vh 0;
}

.home-copy{
  max-width:800px;
}

.eyebrow{
  margin:0 0 25px;

  color:var(--bronze);
  font-size:9px;
  font-weight:600;
  letter-spacing:.2em;
  text-transform:uppercase;
}

.home-title{
  margin:0;

  font-family:var(--serif);
  font-size:clamp(5rem,10vw,10.5rem);
  font-weight:400;
  line-height:.78;
  letter-spacing:-.045em;
}

.home-title em{
  display:block;
  margin-left:.7em;
  font-style:italic;
}

.home-lead{
  max-width:590px;
  margin:40px 0 34px;

  font-family:var(--serif);
  font-size:clamp(1.3rem,2vw,2rem);
  line-height:1.15;
}

.primary-link{
  display:inline-flex;
  align-items:center;
  gap:18px;

  padding:13px 0;

  border-bottom:1px solid var(--ink);

  font-size:9px;
  letter-spacing:.16em;
  text-transform:uppercase;
}

.primary-link:hover{
  color:var(--bronze);
  border-color:var(--bronze);
}

.home-feature{
  position:relative;
}

.home-feature img{
  width:100%;
  max-height:72vh;
  object-fit:contain;

  background:#ddd7cc;

  box-shadow:0 25px 70px rgba(20,18,14,.15);
}

.feature-caption{
  display:flex;
  justify-content:space-between;

  margin-top:13px;

  color:var(--muted);
  font-size:8px;
  letter-spacing:.13em;
  text-transform:uppercase;
}

.home-statement{
  width:min(var(--reading),88vw);
  margin:0 auto;
  padding:150px 0;

  text-align:center;
}

.home-statement p{
  margin:0;

  font-family:var(--serif);
  font-size:clamp(2.5rem,6vw,6rem);
  line-height:.9;
}

.home-stat{
  display:grid;
  grid-template-columns:repeat(3,1fr);

  width:min(900px,88vw);
  margin:0 auto;
  border-top:1px solid var(--line);
}

.home-stat div{
  padding:28px 15px;
  border-right:1px solid var(--line);
}

.home-stat div:last-child{
  border-right:0;
}

.home-stat strong{
  display:block;

  font-family:var(--serif);
  font-size:3rem;
  font-weight:400;
}

.home-stat span{
  color:var(--muted);
  font-size:8px;
  letter-spacing:.14em;
  text-transform:uppercase;
}

.home-categories{
  width:min(var(--wide),92vw);
  margin:120px auto;

  border-top:1px solid var(--line);
}

.home-categories a{
  display:grid;
  grid-template-columns:100px 1fr auto;

  align-items:center;

  padding:22px 0;

  border-bottom:1px solid var(--soft-line);

  transition:padding-left .25s ease,color .25s ease;
}

.home-categories a:hover{
  padding-left:12px;
  color:var(--bronze);
}

.home-categories small{
  color:var(--muted);
  font-size:8px;
}

.home-categories span{
  font-family:var(--serif);
  font-size:clamp(1.8rem,4vw,4rem);
  line-height:.9;
}

.home-categories b{
  font-weight:400;
  color:var(--muted);
}

.artist-note{
  width:min(var(--reading),88vw);
  margin:140px auto;

  display:grid;
  grid-template-columns:1fr 2fr;
  gap:60px;

  border-top:1px solid var(--line);
  padding-top:30px;
}

.artist-note h2{
  margin:0;

  font-family:var(--serif);
  font-size:2rem;
  font-weight:400;
}

.artist-note p{
  margin:0;
  max-width:650px;

  font-family:var(--serif);
  font-size:1.7rem;
  line-height:1.1;
}

.final-invitation{
  padding:140px 20px;

  background:var(--night);
  color:var(--night-text);

  text-align:center;
}

.final-invitation p{
  margin:0 0 40px;

  font-family:var(--serif);
  font-size:clamp(3rem,7vw,7rem);
  line-height:.82;
}

.final-invitation .primary-link{
  border-color:var(--night-text);
}

.site-footer{
  padding:30px clamp(20px,4vw,58px);

  display:flex;
  justify-content:space-between;
  gap:20px;

  color:var(--muted);
  border-top:1px solid var(--line);

  font-size:8px;
  letter-spacing:.12em;
  text-transform:uppercase;
}

/* =========================================================
   COLLECTION
   ========================================================= */

.collection-intro{
  width:min(var(--reading),88vw);
  margin:0 auto;
  padding:95px 0 70px;
}

.collection-intro .eyebrow{
  margin-bottom:20px;
}

.collection-title{
  margin:0;
  max-width:1000px;

  font-family:var(--serif);
  font-size:clamp(4rem,8vw,8rem);
  font-weight:400;
  line-height:.82;
  letter-spacing:-.04em;
}

.collection-description{
  max-width:650px;
  margin:35px 0 0;

  color:var(--muted);

  font-family:var(--serif);
  font-size:1.45rem;
  line-height:1.15;
}

.collection-grid{
  width:min(var(--wide),92vw);
  margin:0 auto 120px;

  display:grid;
  grid-template-columns:repeat(12,1fr);
  gap:60px 28px;
}

.work-card{
  grid-column:span 4;
}

.work-card:nth-child(5n+1){
  grid-column:span 5;
}

.work-card:nth-child(5n+2){
  grid-column:span 7;
  padding-top:80px;
}

.work-card:nth-child(5n+3){
  grid-column:span 4;
}

.work-card:nth-child(5n+4){
  grid-column:span 4;
  padding-top:55px;
}

.work-card:nth-child(5n+5){
  grid-column:span 4;
}

.work-card-image{
  overflow:hidden;
  background:#ddd7cc;
}

.work-card-image img{
  width:100%;
  aspect-ratio:4/5;
  object-fit:cover;

  transition:transform .7s cubic-bezier(.2,.7,.2,1);
}

.work-card:nth-child(5n+2) img{
  aspect-ratio:16/10;
}

.work-card:hover img{
  transform:scale(1.025);
}

.work-card-meta{
  display:grid;
  grid-template-columns:45px 1fr auto;
  gap:12px;

  padding:13px 0;

  border-top:1px solid var(--line);
}

.work-card-number,
.work-card-category{
  color:var(--muted);
  font-size:8px;
  letter-spacing:.1em;
  text-transform:uppercase;
}

.work-card-title{
  font-family:var(--serif);
  font-size:1.45rem;
  line-height:1;
}

.work-card-arrow{
  color:var(--muted);
}

/* =========================================================
   OBRA INDIVIDUAL
   ========================================================= */

.work-page{
  min-height:100vh;
}

.work-header{
  width:min(var(--reading),88vw);
  margin:0 auto;
  padding:48px 0 32px;

  display:grid;
  grid-template-columns:80px 1fr;
  gap:28px;
}

.work-number{
  color:var(--bronze);
  font-size:9px;
  letter-spacing:.16em;
}

.work-category{
  margin:0 0 8px;

  color:var(--muted);
  font-size:8px;
  letter-spacing:.17em;
  text-transform:uppercase;
}

.work-title{
  margin:0;

  font-family:var(--serif);
  font-size:clamp(4rem,8vw,8.5rem);
  font-weight:400;
  line-height:.78;
  letter-spacing:-.045em;
}

.work-artist{
  margin:18px 0 0;

  color:var(--muted);
  font-family:var(--serif);
  font-size:1.15rem;
}

.artwork-frame{
  width:min(var(--wide),94vw);
  margin:0 auto 95px;
  padding:35px clamp(15px,4vw,60px);

  display:flex;
  justify-content:center;
  align-items:center;

  background:var(--paper-deep);

  border-top:1px solid var(--soft-line);
  border-bottom:1px solid var(--soft-line);
}

.artwork-frame img{
  max-width:100%;
  max-height:78vh;

  width:auto;
  height:auto;

  object-fit:contain;

  box-shadow:
    0 25px 65px rgba(20,18,14,.18),
    0 5px 16px rgba(20,18,14,.08);

  cursor:zoom-in;
}

.artwork-caption{
  width:min(var(--reading),88vw);
  margin:-65px auto 85px;

  color:var(--muted);
  font-size:8px;
  letter-spacing:.1em;
  text-transform:uppercase;
}

.curatorial{
  width:min(var(--reading),88vw);
  margin:auto;
}

.curatorial-section{
  display:grid;
  grid-template-columns:145px 1fr;
  gap:55px;

  padding:35px 0 70px;

  border-top:1px solid var(--line);
}

.curatorial-label{
  color:var(--bronze);
  font-size:8px;
  font-weight:600;
  letter-spacing:.17em;
  text-transform:uppercase;
}

.curatorial-text{
  max-width:720px;

  font-family:var(--serif);
  font-size:clamp(1.5rem,2.5vw,2.35rem);
  line-height:1.08;
}

.record{
  width:min(var(--reading),88vw);
  margin:0 auto;

  border-top:1px solid var(--line);
  border-bottom:1px solid var(--line);
}

.record-row{
  display:grid;
  grid-template-columns:180px 1fr;

  padding:13px 0;

  border-bottom:1px solid var(--soft-line);
}

.record-row:last-child{
  border-bottom:0;
}

.record-key{
  color:var(--muted);
  font-size:8px;
  letter-spacing:.12em;
  text-transform:uppercase;
}

.record-value{
  font-size:11px;
}

.mirror{
  margin-top:100px;

  padding:100px 0;

  background:var(--night);
  color:var(--night-text);
}

.mirror-inner{
  width:min(var(--reading),88vw);
  margin:auto;
}

.mirror .curatorial-section{
  border-color:rgba(255,255,255,.13);
}

.mirror .curatorial-label{
  color:#aa8b5d;
}

.keywords{
  width:min(var(--reading),88vw);
  margin:80px auto 0;
}

.keywords-list{
  display:flex;
  flex-wrap:wrap;
  gap:0;

  margin-top:22px;
}

.keywords-list span{
  color:var(--muted);
  font-size:8px;
  letter-spacing:.13em;
  text-transform:uppercase;
}

.keywords-list span:not(:last-child)::after{
  content:"·";
  margin:0 14px;
  color:var(--bronze);
}

.related{
  width:min(var(--reading),88vw);
  margin:110px auto 0;
}

.related-heading{
  margin:0 0 25px;

  color:var(--bronze);
  font-size:8px;
  letter-spacing:.17em;
  text-transform:uppercase;
}

.related-link{
  display:grid;
  grid-template-columns:60px 1fr 30px;

  align-items:center;

  padding:20px 0;

  border-top:1px solid var(--line);

  transition:padding-left .2s ease,color .2s ease;
}

.related-link:last-child{
  border-bottom:1px solid var(--line);
}

.related-link:hover{
  padding-left:10px;
  color:var(--bronze);
}

.related-num{
  color:var(--muted);
  font-size:8px;
}

.related-title{
  font-family:var(--serif);
  font-size:1.7rem;
  line-height:1;
}

.work-nav{
  width:min(var(--reading),88vw);
  margin:100px auto;

  display:grid;
  grid-template-columns:1fr 1fr;

  border-top:1px solid var(--line);
}

.work-nav a{
  min-height:140px;
  padding:25px 0;

  display:flex;
  flex-direction:column;
  justify-content:center;
  gap:9px;
}

.work-nav a+a{
  padding-left:35px;
  border-left:1px solid var(--line);
  text-align:right;
  align-items:flex-end;
}

.nav-small{
  color:var(--muted);
  font-size:8px;
  letter-spacing:.15em;
  text-transform:uppercase;
}

.nav-big{
  font-family:var(--serif);
  font-size:clamp(1.5rem,3vw,2.7rem);
  line-height:.9;
}

/* =========================================================
   LIGHTBOX
   ========================================================= */

.lightbox{
  position:fixed;
  inset:0;
  z-index:1000;

  display:none;
  align-items:center;
  justify-content:center;

  padding:25px;

  background:rgba(10,10,9,.97);
}

.lightbox.open{
  display:flex;
}

.lightbox img{
  max-width:95vw;
  max-height:92vh;
  object-fit:contain;
}

.lightbox-close{
  position:absolute;
  top:18px;
  right:22px;

  width:42px;
  height:42px;

  border:1px solid rgba(255,255,255,.25);
  background:transparent;

  color:white;
  cursor:pointer;
}

/* =========================================================
   RESPONSIVE
   ========================================================= */

@media(max-width:800px){

  .site-header{
    height:60px;
  }

  .home-hero{
    min-height:auto;

    display:flex;
    flex-direction:column;
    align-items:stretch;
    gap:55px;

    padding:55px 0 80px;
  }

  .home-title{
    font-size:clamp(4.2rem,19vw,7rem);
  }

  .home-lead{
    margin-top:30px;
  }

  .home-feature img{
    max-height:68vh;
  }

  .home-statement{
    padding:100px 0;
  }

  .home-stat strong{
    font-size:2.2rem;
  }

  .artist-note{
    grid-template-columns:1fr;
    gap:25px;
    margin:100px auto;
  }

  .artist-note p{
    font-size:1.4rem;
  }

  .collection-intro{
    padding:65px 0 50px;
  }

  .collection-title{
    font-size:clamp(3.8rem,17vw,6rem);
  }

  .collection-grid{
    display:block;
    width:92vw;
  }

  .work-card,
  .work-card:nth-child(5n+1),
  .work-card:nth-child(5n+2),
  .work-card:nth-child(5n+3),
  .work-card:nth-child(5n+4),
  .work-card:nth-child(5n+5){
    margin-bottom:55px;
    padding-top:0;
  }

  .work-card-image img,
  .work-card:nth-child(5n+2) img{
    aspect-ratio:4/5;
  }

  .work-header{
    display:block;
    padding:35px 0 27px;
  }

  .work-number{
    display:block;
    margin-bottom:14px;
  }

  .work-title{
    font-size:clamp(3.6rem,18vw,6rem);
  }

  .artwork-frame{
    width:100%;
    padding:18px 10px;
    margin-bottom:65px;
  }

  .artwork-frame img{
    max-width:94vw;
    max-height:70vh;
  }

  .artwork-caption{
    margin:-35px auto 60px;
  }

  .curatorial-section{
    grid-template-columns:1fr;
    gap:18px;
    padding:28px 0 50px;
  }

  .curatorial-text{
    font-size:1.55rem;
  }

  .record-row{
    grid-template-columns:1fr;
    gap:5px;
    padding:12px 0;
  }

  .mirror{
    margin-top:65px;
    padding:65px 0;
  }

  .keywords{
    margin-top:60px;
  }

  .related{
    margin-top:75px;
  }

  .related-title{
    font-size:1.45rem;
  }

  .work-nav{
    grid-template-columns:1fr;
    margin:75px auto;
  }

  .work-nav a+a{
    padding-left:0;
    border-left:0;
    border-top:1px solid var(--line);
    text-align:left;
    align-items:flex-start;
  }

  .site-footer{
    flex-direction:column;
    line-height:1.6;
  }
}

@media(prefers-reduced-motion:reduce){
  html{
    scroll-behavior:auto;
  }

  *{
    transition:none !important;
  }
}
'''

(CSS / "museum.css").write_text(CSS_CONTENT, encoding="utf-8")

# ============================================================
# JAVASCRIPT DEL MUSEO
# ============================================================

JS_CONTENT = r'''
document.addEventListener("DOMContentLoaded", () => {

  const lightbox = document.querySelector(".lightbox");
  const lightboxImage = document.querySelector(".lightbox img");
  const close = document.querySelector(".lightbox-close");

  if (!lightbox || !lightboxImage) return;

  document.querySelectorAll("[data-lightbox]").forEach(img => {
    img.addEventListener("click", () => {
      lightboxImage.src = img.currentSrc || img.src;
      lightboxImage.alt = img.alt || "";
      lightbox.classList.add("open");
      document.body.style.overflow = "hidden";
    });
  });

  function closeLightbox(){
    lightbox.classList.remove("open");
    document.body.style.overflow = "";
  }

  close?.addEventListener("click", closeLightbox);

  lightbox.addEventListener("click", event => {
    if(event.target === lightbox) closeLightbox();
  });

  document.addEventListener("keydown", event => {
    if(event.key === "Escape") closeLightbox();
  });

});
'''

(JS / "museum.js").write_text(JS_CONTENT, encoding="utf-8")

# ============================================================
# HEADER / FOOTER
# ============================================================

def header(back_href="coleccion.html", back_text="La colección"):
    return f'''
<header class="site-header">
  <a class="wordmark" href="index.html" aria-label="Lienzos del Alma">
    <span class="wordmark-main">Lienzos del Alma</span>
    <span class="wordmark-sub">{ARTISTA}</span>
  </a>

  <a class="header-link" href="{back_href}">← {back_text}</a>
</header>
'''

def footer():
    return f'''
<footer class="site-footer">
  <span>{COLECCION} · {ARTISTA}</span>
  <span>{LUGAR} · © 2026</span>
</footer>
'''

# ============================================================
# INDEX
# ============================================================

featured = next((w for w in works if w["id"] == "09"), works[0])

index_html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{esc(COLECCION)} — archivo digital de la obra de {esc(ARTISTA)}.">
<title>{esc(COLECCION)} · {esc(ARTISTA)}</title>
<link rel="stylesheet" href="css/museum.css">
</head>

<body>

{header("coleccion.html","Explorar colección")}

<main class="home">

<section class="home-hero">

  <div class="home-copy">

    <p class="eyebrow">{esc(LUGAR)}</p>

    <h1 class="home-title">
      Una vida
      <em>en color.</em>
    </h1>

    <p class="home-lead">
      Un archivo de memoria, naturaleza, espiritualidad y paisaje.
      Veinticinco obras reunidas para ser contempladas sin prisa.
    </p>

    <a class="primary-link" href="coleccion.html">
      Entrar al museo <span>→</span>
    </a>

  </div>

  <a class="home-feature" href="obras/obra-{featured['id']}.html">

    <img
      src="{esc(image_url(featured))}"
      alt="{esc(featured['title'])} — {esc(ARTISTA)}"
    >

    <div class="feature-caption">
      <span>{esc(featured['title'])}</span>
      <span>{featured['id']} / {len(works):02d}</span>
    </div>

  </a>

</section>

<section class="home-statement">
  <p>
    Hay obras que se miran.<br>
    Hay obras que permanecen.
  </p>
</section>

<section class="home-stat">
  <div>
    <strong>{len(works)}</strong>
    <span>obras</span>
  </div>
  <div>
    <strong>04</strong>
    <span>universos</span>
  </div>
  <div>
    <strong>01</strong>
    <span>artista</span>
  </div>
</section>

<section class="home-categories">

  <a href="coleccion.html">
    <small>01</small>
    <span>Retratos</span>
    <b>→</b>
  </a>

  <a href="coleccion.html">
    <small>02</small>
    <span>Naturaleza</span>
    <b>→</b>
  </a>

  <a href="coleccion.html">
    <small>03</small>
    <span>Paisajes</span>
    <b>→</b>
  </a>

  <a href="coleccion.html">
    <small>04</small>
    <span>Religioso</span>
    <b>→</b>
  </a>

</section>

<section class="artist-note">

  <h2>El artista</h2>

  <p>
    La colección conserva una mirada construida desde el color,
    la contemplación y la memoria. Cada obra forma parte de un
    recorrido personal que aquí encuentra una segunda vida:
    la del museo digital.
  </p>

</section>

<section class="final-invitation">

  <p>
    Descubrir<br>
    la colección.
  </p>

  <a class="primary-link" href="coleccion.html">
    Ver las {len(works)} obras <span>→</span>
  </a>

</section>

</main>

{footer()}

</body>
</html>
'''

(ROOT / "index.html").write_text(index_html, encoding="utf-8")

# ============================================================
# COLECCIÓN
# ============================================================

cards = []

for w in works:
    cards.append(f'''
<article class="work-card">

  <a href="obras/obra-{w["id"]}.html">

    <div class="work-card-image">
      <img
        src="{esc(image_url(w))}"
        alt="{esc(w["title"])} — {esc(ARTISTA)}"
        loading="lazy"
      >
    </div>

    <div class="work-card-meta">
      <span class="work-card-number">{w["id"]}</span>
      <span class="work-card-title">{esc(w["title"])}</span>
      <span class="work-card-arrow">↗</span>
    </div>

    <div class="work-card-category">{esc(w["category"])}</div>

  </a>

</article>
''')

collection_html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>La colección · {esc(COLECCION)}</title>
<link rel="stylesheet" href="css/museum.css">
</head>

<body>

{header("index.html","Inicio")}

<main>

<section class="collection-intro">
  <p class="eyebrow">02 · La colección</p>

  <h1 class="collection-title">
    Veinticinco obras.<br>
    Un mismo recorrido.
  </h1>

  <p class="collection-description">
    Una colección organizada para contemplar el trabajo de
    {esc(ARTISTA)} como un conjunto, pero también para descubrir
    cada pieza de manera individual.
  </p>
</section>

<section class="collection-grid">
{''.join(cards)}
</section>

</main>

{footer()}

</body>
</html>
'''

(ROOT / "coleccion.html").write_text(collection_html, encoding="utf-8")

# ============================================================
# PÁGINAS INDIVIDUALES
# ============================================================

for index, w in enumerate(works):

    prev_w = works[index - 1] if index > 0 else None
    next_w = works[index + 1] if index + 1 < len(works) else None

    c = curatorial(w)

    related = [
        x for x in works
        if x["id"] != w["id"] and x["category"] == w["category"]
    ][:2]

    related_html = ""

    for r in related:
        related_html += f'''
<a class="related-link" href="obra-{r["id"]}.html">
  <span class="related-num">{r["id"]}</span>
  <span class="related-title">{esc(r["title"])}</span>
  <span>↗</span>
</a>
'''

    prev_html = ""

    if prev_w:
        prev_html = f'''
<a href="obra-{prev_w["id"]}.html">
  <span class="nav-small">← Anterior · {prev_w["id"]}</span>
  <span class="nav-big">{esc(prev_w["title"])}</span>
</a>
'''
    else:
        prev_html = '''
<a href="../coleccion.html">
  <span class="nav-small">← Regresar</span>
  <span class="nav-big">La colección</span>
</a>
'''

    if next_w:
        next_html = f'''
<a href="obra-{next_w["id"]}.html">
  <span class="nav-small">Siguiente · {next_w["id"]} →</span>
  <span class="nav-big">{esc(next_w["title"])}</span>
</a>
'''
    else:
        next_html = '''
<a href="../coleccion.html">
  <span class="nav-small">Fin del recorrido →</span>
  <span class="nav-big">Volver a la colección</span>
</a>
'''

    keywords = "".join(
        f"<span>{esc(k)}</span>" for k in c["keywords"]
    )

    desc = w["description"] or c["intro"]

    page = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<meta name="description"
content="{esc(desc)}">

<title>{esc(w["title"])} · {esc(COLECCION)}</title>

<link rel="stylesheet" href="../css/museum.css">
</head>

<body>

<div class="work-page">

{header("../coleccion.html","Colección")}

<main>

<header class="work-header">

  <div class="work-number">
    {w["id"]} / {len(works):02d}
  </div>

  <div>
    <p class="work-category">{esc(w["category"])}</p>

    <h1 class="work-title">
      {esc(w["title"])}
    </h1>

    <p class="work-artist">
      {esc(ARTISTA)}
    </p>
  </div>

</header>

<figure class="artwork-frame">

  <img
    src="{esc(image_url(w))}"
    alt="{esc(w["title"])} — {esc(ARTISTA)}"
    data-lightbox
  >

</figure>

<p class="artwork-caption">
  {esc(w["title"])} · {esc(w["category"])} · {w["id"]} / {len(works):02d}
</p>

<section class="curatorial">

  <div class="curatorial-section">

    <div class="curatorial-label">
      01 · Sobre la obra
    </div>

    <div class="curatorial-text">
      {esc(c["intro"])}
    </div>

  </div>

</section>

<section class="record">

  <div class="record-row">
    <span class="record-key">Artista</span>
    <span class="record-value">{esc(ARTISTA)}</span>
  </div>

  <div class="record-row">
    <span class="record-key">Categoría</span>
    <span class="record-value">{esc(w["category"])}</span>
  </div>

  <div class="record-row">
    <span class="record-key">Colección</span>
    <span class="record-value">{esc(COLECCION)}</span>
  </div>

  <div class="record-row">
    <span class="record-key">Archivo</span>
    <span class="record-value">{w["id"]} / {len(works):02d}</span>
  </div>

  <div class="record-row">
    <span class="record-key">Lugar asociado</span>
    <span class="record-value">{LUGAR}</span>
  </div>

</section>

<section class="mirror">

  <div class="mirror-inner">

    <div class="curatorial-section">

      <div class="curatorial-label">
        02 · Lo que vemos
      </div>

      <div class="curatorial-text">
        {esc(c["seeing"])}
      </div>

    </div>

    <div class="curatorial-section">

      <div class="curatorial-label">
        03 · Una mirada
      </div>

      <div class="curatorial-text">
        {esc(c["reading"])}
      </div>

    </div>

  </div>

</section>

<section class="keywords">

  <div class="curatorial-label">
    Palabras clave
  </div>

  <div class="keywords-list">
    {keywords}
  </div>

</section>

<section class="related">

  <p class="related-heading">
    El recorrido continúa
  </p>

  <div>
    {related_html}
  </div>

</section>

<nav class="work-nav">

  {prev_html}
  {next_html}

</nav>

</main>

{footer()}

</div>

<div class="lightbox" aria-hidden="true">

  <button
    class="lightbox-close"
    aria-label="Cerrar"
  >×</button>

  <img src="" alt="">

</div>

<script src="../js/museum.js"></script>

</body>
</html>
'''

    (OBRAS / f"obra-{w['id']}.html").write_text(
        page,
        encoding="utf-8"
    )

# ============================================================
# PÁGINA DEL ARTISTA
# ============================================================

artist_html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>El artista · {esc(ARTISTA)}</title>
<link rel="stylesheet" href="css/museum.css">
</head>

<body>

{header("coleccion.html","La colección")}

<main>

<section class="collection-intro">

  <p class="eyebrow">03 · El artista</p>

  <h1 class="collection-title">
    Bernardo León<br>
    Mejía Rivera.
  </h1>

  <p class="collection-description">
    Copacabana · Antioquia · Colombia
  </p>

</section>

<section class="artist-note">

  <h2>Una memoria en color</h2>

  <p>
    Lienzos del Alma reúne una parte del universo visual de
    Bernardo León Mejía Rivera: retratos, naturaleza, paisajes
    y escenas de carácter religioso que encuentran en el color
    una forma de memoria.
  </p>

</section>

<section class="artist-note">

  <h2>El archivo</h2>

  <p>
    Este museo digital conserva las veinticinco obras actualmente
    integradas a la colección y propone un recorrido pensado para
    mirar cada pieza con el tiempo y la atención que merece.
  </p>

</section>

<section class="final-invitation">

  <p>
    Entrar<br>
    a las obras.
  </p>

  <a class="primary-link" href="coleccion.html">
    Explorar la colección →
  </a>

</section>

</main>

{footer()}

</body>
</html>
'''

(ROOT / "artista.html").write_text(artist_html, encoding="utf-8")

# ============================================================
# INVENTARIO NUEVO
# ============================================================

(ROOT / "inventario_museo.json").write_text(
    json.dumps(
        {
            "coleccion": COLECCION,
            "artista": ARTISTA,
            "lugar": LUGAR,
            "total": len(works),
            "obras": works,
        },
        ensure_ascii=False,
        indent=2
    ),
    encoding="utf-8"
)

print()
print("=" * 64)
print("LIENZOS DEL ALMA · MUSEO DIGITAL")
print("=" * 64)
print()
print(f"Artista:     {ARTISTA}")
print(f"Colección:   {COLECCION}")
print(f"Obras:       {len(works)}")
print(f"Excluida:    08")
print()
print("Archivos creados:")
print("  ✓ index.html")
print("  ✓ coleccion.html")
print("  ✓ artista.html")
print("  ✓ css/museum.css")
print("  ✓ js/museum.js")
print("  ✓ inventario_museo.json")
print(f"  ✓ {len(works)} páginas individuales")
print()

for w in works:
    print(f'{w["id"]} · {w["title"]} · {w["category"]}')

print()
print("=" * 64)

if len(works) != 25:
    print("⚠️ ADVERTENCIA: se esperaban 25 obras.")
else:
    print("✅ 25 obras listas.")

if any(w["id"] == "08" for w in works):
    print("❌ ERROR: apareció la obra 08.")
else:
    print("✅ Obra 08 excluida.")

print("=" * 64)

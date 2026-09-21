from pathlib import Path
from html import escape
import re
import json

ROOT = Path(__file__).parent
APP = ROOT / "js" / "app.js"
OUT = ROOT / "obras"

app = APP.read_text(encoding="utf-8")

pattern = re.compile(
    r'id:\s*(\d+),\s*'
    r'title:\s*"([^"]*)",\s*'
    r'category:\s*"([^"]*)",\s*'
    r'image:\s*"([^"]*)",\s*'
    r'description:\s*"([^"]*)"',
    re.S
)

matches = pattern.findall(app)

if len(matches) != 26:
    raise SystemExit(
        f"ERROR: se encontraron {len(matches)} obras; se esperaban 26."
    )

works = [
    {
        "id": int(i),
        "title": title,
        "category": category,
        "image": image,
        "description": description,
    }
    for i, title, category, image, description in matches
]

works.sort(key=lambda x: x["id"])

for expected, work in enumerate(works, 1):
    if work["id"] != expected:
        raise SystemExit(
            f"ERROR: falta la obra {expected:02d}."
        )

labels = {
    "religioso": "Religioso",
    "retratos": "Retratos",
    "naturaleza": "Naturaleza",
    "paisajes": "Paisajes",
}


OUT.mkdir(exist_ok=True)


# INVENTARIO_CURATORIAL_INTEGRADO
# ------------------------------------------------------------
# Enriquece cada obra con la información curatorial validada.
# El inventario es la fuente de contenido editorial.
# ------------------------------------------------------------

INVENTARIO_PATH = ROOT / "inventario_curatorial.json"

if not INVENTARIO_PATH.exists():
    raise SystemExit("❌ No existe inventario_curatorial.json")

with INVENTARIO_PATH.open(encoding="utf-8") as f:
    inventario = json.load(f)

if len(inventario) != 26:
    raise SystemExit(
        f"❌ Inventario incorrecto: se esperaban 26 obras, hay {len(inventario)}."
    )

inventario_por_id = {item["id"]: item for item in inventario}

if set(inventario_por_id) != set(range(1, 27)):
    raise SystemExit(
        "❌ El inventario debe contener exactamente los IDs 1–26."
    )

campos_curatoriales = {
    "descripcion_visual",
    "lectura_curatorial",
    "elementos_visuales",
    "palabras_clave",
    "alt_text",
    "obras_relacionadas",
    "estado_curatorial",
}

for work in works:
    item = inventario_por_id[work["id"]]

    faltantes = campos_curatoriales - set(item)
    if faltantes:
        raise SystemExit(
            f"❌ Obra {work['id']} incompleta: {sorted(faltantes)}"
        )

    work.update({
        "descripcion_visual": item["descripcion_visual"],
        "lectura_curatorial": item["lectura_curatorial"],
        "elementos_visuales": item["elementos_visuales"],
        "palabras_clave": item["palabras_clave"],
        "alt_text": item["alt_text"],
        "obras_relacionadas": item["obras_relacionadas"],
        "estado_curatorial": item["estado_curatorial"],
    })

for index, work in enumerate(works):

    number = f"{work['id']:02d}"

    title = escape(work["title"])
    category = escape(
        labels.get(work["category"], work["category"].title())
    )
    image = escape(work["image"], quote=True)
    description = escape(work["description"])
    reading = escape(work["lectura_curatorial"])
    visual_description = escape(work["descripcion_visual"])
    alt_text = escape(work["alt_text"], quote=True)
    keywords = work["palabras_clave"]
    related_ids = work["obras_relacionadas"]
    related_links = []
    works_by_id = {item["id"]: item for item in works}

    for related_id in related_ids:
        related = works_by_id.get(related_id)
        if related:
            related_links.append(
                f'<a href="../obras/obra-{related["id"]:02d}.html">'
                f'<span>{related["id"]:02d}</span>'
                f'<strong>{escape(related["title"])}</strong>'
                f'</a>'
            )

    editorial_status = work["estado_curatorial"]

    previous = (
        f'''
        <a class="nav-link previous"
           data-previous
           href="../obras/obra-{works[index-1]["id"]:02d}.html">
          <span class="nav-label">Anterior</span>
          <span class="nav-title">{escape(works[index-1]["title"])}</span>
        </a>
        '''
        if index > 0
        else '<span class="nav-empty"></span>'
    )

    next_link = (
        f'''
        <a class="nav-link next"
           data-next
           href="../obras/obra-{works[index+1]["id"]:02d}.html">
          <span class="nav-label">Siguiente</span>
          <span class="nav-title">{escape(works[index+1]["title"])}</span>
        </a>
        '''
        if index < len(works) - 1
        else '<span class="nav-empty"></span>'
    )

    meta_description = escape(
        f"{work['description']} "
        f"{work['title']} · "
        "Bernardo León Mejía Rivera · "
        "Lienzos del Alma · "
        "Copacabana, Antioquia, Colombia.",
        quote=True
    )

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">

<title>{title} · Lienzos del Alma</title>

<meta
  name="description"
  content="{meta_description}"
>

<meta
  property="og:title"
  content="{title} · Lienzos del Alma"
>

<meta
  property="og:description"
  content="{escape(description, quote=True)}"
>

<meta
  property="og:image"
  content="{image}"
>

<meta property="og:type" content="article">

<link rel="stylesheet" href="../css/obra.css">
</head>

<body>

<div class="obra-page">

<header class="obra-header">

  <a class="brand" href="../index.html">

    <strong>Lienzos del Alma</strong>

    <span>
      Bernardo León Mejía Rivera
    </span>

  </a>

  <a class="back" href="../index.html#galeria">
    <span aria-hidden="true">←</span>
    Colección
  </a>

</header>


<main class="obra-main">

  <div class="obra-intro">

    <div class="obra-index">
      {number} / 26
    </div>

    <p class="obra-kicker">
      {category}
    </p>

    <h1 class="obra-title">
      {title}
    </h1>

    <p class="obra-artist">
      Bernardo León Mejía Rivera
    </p>

  </div>


  <figure class="obra-stage">

    <img
      class="obra-image"
      src="{image}"
      alt="{escape(work["alt_text"], quote=True)}"
      loading="eager"
      decoding="async"
      draggable="false"
    >

    <figcaption>
      {title} · {category}
    </figcaption>

  </figure>


  <section class="obra-editorial">

    <div class="editorial-main">

      <p class="editorial-label">
        Sobre la obra
      </p>

      <p class="obra-description">
        {description}
      </p>

    </div>


    <aside class="obra-record">

      <p class="editorial-label">
        Ficha
      </p>

      <dl>

        <div>
          <dt>Artista</dt>
          <dd>Bernardo León Mejía Rivera</dd>
        </div>

        <div>
          <dt>Categoría</dt>
          <dd>{category}</dd>
        </div>

        <div>
          <dt>Colección</dt>
          <dd>Lienzos del Alma</dd>
        </div>

        <div>
          <dt>Ubicación asociada</dt>
          <dd>Copacabana · Antioquia · Colombia</dd>
        </div>

      </dl>

    </aside>

  </section>


  <section class="obra-visual-description">

    <p class="editorial-label">
      Lo que vemos
    </p>

    <p class="visual-description">
      {visual_description}
    </p>

  </section>


  <section class="obra-reading">

    <p class="editorial-label">
      Una mirada
    </p>

    <div class="reading-copy">

      <p>
        {reading}
      </p>

    </div>

  </section>


  <section class="obra-keywords">

    <p class="editorial-label">
      Palabras clave
    </p>

    <div class="keyword-list">
      {"".join(
          f'<span>{escape(keyword)}</span>'
          for keyword in keywords
      )}
    </div>

  </section>


  <section class="obra-related">

    <p class="editorial-label">
      Obras relacionadas
    </p>

    <div class="related-list">
      {"".join(related_links)}
    </div>

  </section>


  <nav
    class="obra-navigation"
    aria-label="Navegación entre obras"
  >

    {previous}

    <a
      class="collection-link"
      href="../index.html#galeria"
    >
      <span class="collection-symbol">✦</span>
      <span>Ver colección</span>
    </a>

    {next_link}

  </nav>

</main>


<footer class="obra-footer">

  <div>
    <strong>Lienzos del Alma</strong>
  </div>

  <div>
    Bernardo León Mejía Rivera
  </div>

  <div>
    Copacabana · Antioquia · Colombia
  </div>

</footer>


<div
  class="lightbox"
  aria-hidden="true"
>

  <button
    class="lightbox-close"
    aria-label="Cerrar imagen"
  >
    ×
  </button>

  <img
    src=""
    alt=""
  >

</div>

</div>


<script src="../js/obra.js"></script>

</body>
</html>
"""

    output = OUT / f"obra-{number}.html"
    html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
    output.write_text(html, encoding="utf-8")


print(f"OK: {len(works)} páginas preparadas.")

for work in works:
    label = labels.get(
        work["category"],
        work["category"]
    )

    print(
        f"{work['id']:02d} · "
        f"{work['title']} · "
        f"{label}"
    )

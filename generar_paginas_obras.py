from pathlib import Path
from html import escape
import re
import json

ROOT = Path(__file__).parent
APP = ROOT / "js" / "app.js"
OUT = ROOT / "obras"
INVENTARIO_PATH = ROOT / "inventario_curatorial.json"

OUT.mkdir(exist_ok=True)

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

if not matches:
    raise SystemExit(
        "ERROR: no se encontraron obras en js/app.js"
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

ids = [w["id"] for w in works]

if len(ids) != len(set(ids)):
    raise SystemExit("ERROR: existen IDs duplicados.")

if 8 in ids:
    raise SystemExit(
        "ERROR: la obra 08 todavía aparece en js/app.js."
    )

if not INVENTARIO_PATH.exists():
    raise SystemExit(
        "ERROR: falta inventario_curatorial.json"
    )

with INVENTARIO_PATH.open(encoding="utf-8") as f:
    inventario = json.load(f)

inventario_por_id = {
    item["id"]: item for item in inventario
}

campos = {
    "descripcion_visual",
    "lectura_curatorial",
    "elementos_visuales",
    "palabras_clave",
    "alt_text",
    "obras_relacionadas",
    "estado_curatorial",
}

for work in works:

    item = inventario_por_id.get(work["id"])

    if not item:
        raise SystemExit(
            f"ERROR: falta información curatorial para la obra "
            f"{work['id']:02d}"
        )

    faltantes = campos - set(item)

    if faltantes:
        raise SystemExit(
            f"ERROR: obra {work['id']:02d} incompleta: "
            f"{sorted(faltantes)}"
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


labels = {
    "religioso": "Religioso",
    "retratos": "Retratos",
    "naturaleza": "Naturaleza",
    "paisajes": "Paisajes",
}


category_classes = {
    "religioso": "religioso",
    "retratos": "retratos",
    "naturaleza": "naturaleza",
    "paisajes": "paisajes",
}


works_by_id = {
    work["id"]: work
    for work in works
}


def esc(value, quote=False):
    return escape(str(value), quote=quote)


def category_label(value):
    return labels.get(
        value.lower(),
        value.title()
    )


for index, work in enumerate(works):

    number = f"{work['id']:02d}"
    total = len(works)

    title = esc(work["title"])
    category = esc(
        category_label(work["category"])
    )

    category_class = category_classes.get(
        work["category"].lower(),
        "general"
    )

    image = esc(
        work["image"],
        quote=True
    )

    description = esc(
        work["description"]
    )

    visual_description = esc(
        work["descripcion_visual"]
    )

    reading = esc(
        work["lectura_curatorial"]
    )

    alt_text = esc(
        work["alt_text"],
        quote=True
    )

    keywords_html = "".join(
        f"<li>{esc(keyword)}</li>"
        for keyword in work["palabras_clave"]
    )

    related_html = []

    for related_id in work["obras_relacionadas"]:

        related = works_by_id.get(related_id)

        if not related:
            continue

        related_html.append(
            f"""
            <a
              class="related-work"
              href="obra-{related['id']:02d}.html"
            >
              <span class="related-number">
                {related['id']:02d}
              </span>

              <span class="related-info">
                <small>
                  {esc(category_label(related['category']))}
                </small>

                <strong>
                  {esc(related['title'])}
                </strong>
              </span>

              <span class="related-arrow">↗</span>
            </a>
            """
        )

    related_html = "".join(related_html)

    previous_html = ""

    if index > 0:

        previous = works[index - 1]

        previous_html = f"""
        <a
          class="work-nav previous"
          href="obra-{previous['id']:02d}.html"
        >
          <span class="work-nav-label">
            ← Anterior
          </span>

          <strong>
            {esc(previous['title'])}
          </strong>

          <small>
            {previous['id']:02d} / {total}
          </small>
        </a>
        """

    next_html = ""

    if index < len(works) - 1:

        following = works[index + 1]

        next_html = f"""
        <a
          class="work-nav next"
          href="obra-{following['id']:02d}.html"
        >
          <span class="work-nav-label">
            Siguiente →
          </span>

          <strong>
            {esc(following['title'])}
          </strong>

          <small>
            {following['id']:02d} / {total}
          </small>
        </a>
        """

    meta_description = esc(
        f"{work['description']} "
        f"{work['title']} · "
        "Bernardo León Mejía Rivera · "
        "Lienzos del Alma · "
        "Copacabana, Antioquia, Colombia.",
        quote=True
    )

    html = f"""<!doctype html>
<html lang="es">

<head>

<meta charset="utf-8">

<meta
  name="viewport"
  content="width=device-width, initial-scale=1"
>

<title>
{title} · Lienzos del Alma
</title>

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
  content="{esc(work['description'], quote=True)}"
>

<meta
  property="og:image"
  content="{image}"
>

<meta
  property="og:type"
  content="article"
>

<link
  rel="stylesheet"
  href="../css/obra.css"
>

</head>

<body
  class="obra-page category-{category_class}"
>

<header class="obra-header">

  <a
    class="museum-brand"
    href="../index.html"
  >

    <span class="brand-name">
      LIENZOS DEL ALMA
    </span>

    <span class="brand-artist">
      Bernardo León Mejía Rivera
    </span>

  </a>

  <a
    class="collection-back"
    href="../coleccion.html"
  >

    <span>←</span>

    <span>
      Colección
    </span>

  </a>

</header>


<main class="obra-main">

  <!-- ==================================================
       IDENTIDAD
       ================================================== -->

  <section class="work-identity">

    <div class="work-number">

      <span>
        {number}
      </span>

      <small>
        / {total}
      </small>

    </div>

    <div class="work-heading">

      <p class="work-category">
        {category}
      </p>

      <h1>
        {title}
      </h1>

      <p class="work-artist">
        Bernardo León Mejía Rivera
      </p>

    </div>

  </section>


  <!-- ==================================================
       OBRA
       ================================================== -->

  <figure class="artwork">

    <button
      class="artwork-button"
      type="button"
      aria-label="Ampliar {title}"
    >

      <img
        src="{image}"
        alt="{alt_text}"
        class="artwork-image"
        loading="eager"
        decoding="async"
        draggable="false"
      >

      <span class="artwork-expand">
        ampliar ↗
      </span>

    </button>

    <figcaption>

      <span>
        {title}
      </span>

      <span>
        {number} / {total}
      </span>

    </figcaption>

  </figure>


  <!-- ==================================================
       SOBRE LA OBRA
       ================================================== -->

  <section class="museum-section introduction">

    <div class="section-marker">

      <span>01</span>

      <span>
        Sobre la obra
      </span>

    </div>

    <div class="section-content">

      <p class="lead-text">
        {description}
      </p>

    </div>

  </section>


  <!-- ==================================================
       FICHA
       ================================================== -->

  <section class="museum-section record">

    <div class="section-marker">

      <span>02</span>

      <span>
        Ficha del museo
      </span>

    </div>

    <div class="record-content">

      <dl>

        <div>
          <dt>Artista</dt>
          <dd>
            Bernardo León Mejía Rivera
          </dd>
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
          <dt>Archivo</dt>
          <dd>{number} / {total}</dd>
        </div>

        <div>
          <dt>Lugar asociado</dt>
          <dd>
            Copacabana · Antioquia · Colombia
          </dd>
        </div>

      </dl>

    </div>

  </section>


  <!-- ==================================================
       MIRAR
       ================================================== -->

  <section class="looking">

    <div class="looking-intro">

      <span class="looking-number">
        03
      </span>

      <span>
        Mirar
      </span>

    </div>


    <div class="looking-content">

      <div class="looking-block">

        <p class="looking-label">
          Lo que vemos
        </p>

        <p class="looking-text">
          {visual_description}
        </p>

      </div>


      <div class="looking-block">

        <p class="looking-label">
          Una mirada
        </p>

        <p class="looking-text">
          {reading}
        </p>

      </div>

    </div>

  </section>


  <!-- ==================================================
       PALABRAS CLAVE
       ================================================== -->

  <section class="keywords">

    <p class="keywords-label">
      Palabras clave
    </p>

    <ul>
      {keywords_html}
    </ul>

  </section>


  <!-- ==================================================
       RELACIONADAS
       ================================================== -->

  <section class="related">

    <div class="related-heading">

      <span>
        04
      </span>

      <h2>
        El recorrido continúa
      </h2>

      <p>
        Otras obras de la colección.
      </p>

    </div>

    <div class="related-list">
      {related_html}
    </div>

  </section>


  <!-- ==================================================
       NAVEGACIÓN
       ================================================== -->

  <nav
    class="work-navigation"
    aria-label="Navegación entre obras"
  >

    <div class="navigation-side">
      {previous_html}
    </div>

    <a
      class="navigation-collection"
      href="../coleccion.html"
    >

      <span>✦</span>

      <small>
        Volver a la colección
      </small>

    </a>

    <div class="navigation-side">
      {next_html}
    </div>

  </nav>


  <!-- ==================================================
       CONTACTO
       ================================================== -->

  <section class="contact">

    <p class="contact-eyebrow">
      LIENZOS DEL ALMA
    </p>

    <h2>
      ¿Esta obra<br>
      <em>te encontró?</em>
    </h2>

    <p class="contact-text">
      Si deseas conocer más sobre esta pieza,
      conversar sobre el trabajo de Bernardo León
      Mejía Rivera o realizar una consulta,
      puedes escribir directamente.
    </p>

    <a
      class="contact-link"
      href="https://wa.me/573222201931"
      target="_blank"
      rel="noopener"
    >
      Conversar sobre esta obra
      <span>↗</span>
    </a>

  </section>

</main>


<footer class="obra-footer">

  <div>
    <strong>
      LIENZOS DEL ALMA
    </strong>
  </div>

  <div>
    Bernardo León Mejía Rivera
  </div>

  <div>
    Copacabana · Antioquia · Colombia
  </div>

  <div>
    © 2026
  </div>

</footer>


<!-- ====================================================
     LIGHTBOX
     ==================================================== -->

<div
  class="lightbox"
  aria-hidden="true"
>

  <button
    class="lightbox-close"
    type="button"
    aria-label="Cerrar imagen"
  >
    ×
  </button>

  <img
    src=""
    alt=""
  >

</div>


<script src="../js/obra.js"></script>

</body>
</html>
"""

    output = OUT / f"obra-{number}.html"

    output.write_text(
        "\n".join(
            line.rstrip()
            for line in html.splitlines()
        ) + "\n",
        encoding="utf-8"
    )


print(
    f"OK: {len(works)} páginas de museo generadas."
)

for work in works:

    print(
        f"{work['id']:02d} · "
        f"{work['title']} · "
        f"{category_label(work['category'])}"
    )

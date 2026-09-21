from pathlib import Path
from html import escape
import re

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

for index, work in enumerate(works):
    number = f"{work['id']:02d}"
    title = escape(work["title"])
    category = escape(labels.get(work["category"], work["category"].title()))
    image = escape(work["image"], quote=True)
    description = escape(work["description"])

    previous = (
        f'<a class="nav-link previous" data-previous '
        f'href="../obras/obra-{works[index-1]["id"]:02d}.html">'
        f'← Obra anterior</a>'
        if index > 0 else '<span></span>'
    )

    next_link = (
        f'<a class="nav-link next" data-next '
        f'href="../obras/obra-{works[index+1]["id"]:02d}.html">'
        f'Obra siguiente →</a>'
        if index < len(works) - 1 else '<span></span>'
    )

    meta_description = escape(
        f"{work['description']} {work['title']} · "
        "Bernardo León Mejía Rivera · "
        "Lienzos del Alma · Copacabana, Antioquia, Colombia.",
        quote=True
    )

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">

<title>{title} · Lienzos del Alma</title>

<meta name="description" content="{meta_description}">
<meta property="og:title" content="{title} · Lienzos del Alma">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:image" content="{image}">
<meta property="og:type" content="article">

<link rel="stylesheet" href="../css/obra.css">
</head>

<body>

<div class="obra-page">

<header class="obra-header">

<a class="brand" href="../index.html">
<strong>Lienzos del Alma</strong>
Bernardo León Mejía Rivera
</a>

<a class="back" href="../index.html#galeria">
← Colección
</a>

</header>

<main class="obra-main">

<section class="obra-stage">

<img
class="obra-image"
src="{image}"
alt="{title} · Bernardo León Mejía Rivera"
loading="eager"
decoding="async"
draggable="false">

</section>

<section class="obra-info">

<div class="obra-number">
Obra {number} · Lienzos del Alma
</div>

<p class="obra-kicker">
{category}
</p>

<h1 class="obra-title">
{title}
</h1>

<p class="obra-description">
{description}
</p>

<div class="obra-meta">
<span class="meta">Bernardo León Mejía Rivera</span>
<span class="meta">Copacabana · Antioquia · Colombia</span>
</div>

</section>

<nav class="obra-navigation" aria-label="Navegación entre obras">

{previous}

<a class="collection-link" href="../index.html#galeria">
Volver a la colección
</a>

{next_link}

</nav>

</main>

<footer class="obra-footer">
Lienzos del Alma · Bernardo León Mejía Rivera · Copacabana · Antioquia · Colombia
</footer>

<div class="lightbox" aria-hidden="true">
<button class="lightbox-close" aria-label="Cerrar">×</button>
<img src="" alt="">
</div>

</div>

<script src="../js/obra.js"></script>

</body>
</html>
"""

    (OUT / f"obra-{number}.html").write_text(html, encoding="utf-8")

print(f"OK: {len(works)} páginas preparadas.")
for work in works:
    print(f"{work['id']:02d} · {work['title']} · {labels.get(work['category'], work['category'])}")

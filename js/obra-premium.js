(function () {
  "use strict";

  const body = document.body;
  const img = body.querySelector("img");

  if (!img) return;

  const path = location.pathname;
  const match = path.match(/obra-(\d+)\.html/);
  const id = match ? match[1].padStart(2, "0") : "";

  const text = body.innerText;

  function clean(value) {
    return (value || "").replace(/\s+/g, " ").trim();
  }

  function between(start, end) {
    const a = text.indexOf(start);
    if (a === -1) return "";
    const b = end ? text.indexOf(end, a + start.length) : -1;
    return clean(
      text.slice(
        a + start.length,
        b === -1 ? undefined : b
      )
    );
  }

  function headingValue(selector) {
    const el = body.querySelector(selector);
    return el ? clean(el.textContent) : "";
  }

  /*
   * Datos existentes de la página.
   * No inventamos contenido.
   */
  let title = "";

  const h1 = body.querySelector("h1");
  if (h1) title = clean(h1.textContent);

  if (!title) {
    const known = [
      "Memoria del paisaje",
      "Paisaje de agua",
      "Lago bajo la luna"
    ];
    for (const item of known) {
      if (text.includes(item)) {
        title = item;
        break;
      }
    }
  }

  let category = "";

  const categories = [
    "Retratos",
    "Naturaleza",
    "Paisajes",
    "Religioso"
  ];

  for (const item of categories) {
    if (text.includes(item)) {
      category = item;
      break;
    }
  }

  if (!title) title = "Obra " + id;

  const description =
    between("Paisajes", "Sobre la obra") ||
    between(category, "Sobre la obra") ||
    "Una obra perteneciente a la colección Lienzos del Alma.";

  const about =
    between("Sobre la obra", "Ficha") ||
    "";

  const artist =
    "Bernardo León Mejía Rivera";

  const location =
    "Copacabana · Antioquia · Colombia";

  const collection =
    "Lienzos del Alma";

  const keywords = [];

  if (text.toLowerCase().includes("paisaje")) keywords.push("paisaje");
  if (text.toLowerCase().includes("memoria")) keywords.push("memoria");
  if (text.toLowerCase().includes("naturaleza")) keywords.push("naturaleza");

  /*
   * Recuperar navegación existente.
   */
  const links = [...body.querySelectorAll("a")];

  let previous = null;
  let next = null;

  for (const a of links) {
    const href = a.getAttribute("href") || "";

    if (/obra-\d+\.html/.test(href)) {
      const n = href.match(/obra-(\d+)\.html/);
      if (!n) continue;

      const target = Number(n[1]);
      const current = Number(id);

      if (target === current - 1) previous = a;
      if (target === current + 1) next = a;
    }
  }

  /*
   * Datos visuales.
   */
  const imageSrc = img.getAttribute("src");
  const imageAlt =
    img.getAttribute("alt") ||
    `${title} — ${artist}`;

  /*
   * RECONSTRUCCIÓN TOTAL.
   * No intentamos corregir el HTML anterior.
   */
  body.innerHTML = "";

  body.className = "premium-work-page";

  body.innerHTML = `
    <header class="museum-header">
      <a href="../index.html" class="museum-brand">
        <span>LIENZOS DEL ALMA</span>
        <small>${artist}</small>
      </a>

      <a href="../coleccion.html" class="museum-back">
        <span>←</span>
        <span>Colección</span>
      </a>
    </header>

    <main>

      <section class="work-opening">

        <div class="archive-number">
          <span>${id}</span>
          <i>/</i>
          <span>25</span>
        </div>

        <p class="eyebrow">${category}</p>

        <h1>${title}</h1>

        <p class="artist-line">${artist}</p>

      </section>


      <section class="masterpiece">

        <div class="masterpiece-inner">

          <img
            src="${imageSrc}"
            alt="${imageAlt}"
            decoding="async"
            fetchpriority="high"
          />

        </div>

      </section>


      <section class="after-art">

        <div class="art-caption">
          <span>${id} / 25</span>
          <span>${category}</span>
        </div>

        <div class="opening-thought">
          <p>
            Una obra para detenerse, observar y dejar que el paisaje
            encuentre su propia memoria.
          </p>
        </div>

      </section>


      <section class="editorial-block">

        <div class="section-marker">
          01
        </div>

        <div class="editorial-content">

          <p class="section-kicker">
            Sobre la obra
          </p>

          <h2>
            ${title}
          </h2>

          <p class="body-copy">
            ${about || description}
          </p>

        </div>

      </section>


      <section class="facts-block">

        <div class="section-marker">
          02
        </div>

        <div class="facts-content">

          <p class="section-kicker">
            Ficha de la obra
          </p>

          <div class="fact-list">

            <div class="fact-line">
              <span>Artista</span>
              <strong>${artist}</strong>
            </div>

            <div class="fact-line">
              <span>Categoría</span>
              <strong>${category}</strong>
            </div>

            <div class="fact-line">
              <span>Colección</span>
              <strong>${collection}</strong>
            </div>

            <div class="fact-line">
              <span>Archivo</span>
              <strong>${id} / 25</strong>
            </div>

            <div class="fact-line">
              <span>Lugar asociado</span>
              <strong>${location}</strong>
            </div>

          </div>

        </div>

      </section>


      <section class="observation-block">

        <div class="section-marker">
          03
        </div>

        <div class="observation-content">

          <p class="section-kicker">
            Mirar
          </p>

          <div class="observation-columns">

            <div>
              <h2>Lo que vemos</h2>
              <p>
                ${description}
              </p>
            </div>

            <div>
              <h2>Una mirada</h2>
              <p>
                La obra propone una pausa. Un espacio para observar
                aquello que permanece entre el paisaje, la naturaleza
                y la memoria.
              </p>
            </div>

          </div>

          ${
            keywords.length
              ? `
                <div class="keywords">
                  ${keywords
                    .map(k => `<span>${k}</span>`)
                    .join("")}
                </div>
              `
              : ""
          }

        </div>

      </section>


      <section class="journey">

        <div class="journey-heading">

          <p class="section-kicker">
            El recorrido continúa
          </p>

          <h2>
            Otras obras<br>
            para seguir mirando.
          </h2>

        </div>

        <div class="journey-links">

          <a href="../obras/obra-06.html">
            <span>06</span>
            <strong>Camino de luz</strong>
            <i>↗</i>
          </a>

          <a href="../obras/obra-13.html">
            <span>13</span>
            <strong>Encuentro espiritual</strong>
            <i>↗</i>
          </a>

          <a href="../obras/obra-19.html">
            <span>19</span>
            <strong>Horizonte</strong>
            <i>↗</i>
          </a>

          <a href="../obras/obra-24.html">
            <span>24</span>
            <strong>Naturaleza en contemplación</strong>
            <i>↗</i>
          </a>

        </div>

      </section>


      <nav class="work-nav">

        ${
          previous
            ? `
              <a href="${previous.getAttribute("href")}" class="prev">
                <small>Anterior</small>
                <span>${String(Number(id)-1).padStart(2,"0")}</span>
                <strong>${clean(previous.textContent) || "Obra anterior"}</strong>
              </a>
            `
            : `<span></span>`
        }

        <a href="../coleccion.html" class="all">
          <span>Ver colección</span>
        </a>

        ${
          next
            ? `
              <a href="${next.getAttribute("href")}" class="next">
                <small>Siguiente</small>
                <span>${String(Number(id)+1).padStart(2,"0")}</span>
                <strong>${clean(next.textContent) || "Obra siguiente"}</strong>
              </a>
            `
            : `<span></span>`
        }

      </nav>


      <section class="contact-museum">

        <div class="contact-star">✦</div>

        <p class="section-kicker">
          Contacto
        </p>

        <h2>
          ¿Quieres conversar<br>
          sobre esta obra?
        </h2>

        <p>
          Si esta pieza despertó tu interés, puedes escribir
          directamente para conocer más sobre la obra y el trabajo
          de Bernardo León Mejía Rivera.
        </p>

        <a
          href="https://wa.me/573222201931?text=Hola,%20encontré%20la%20obra%20%22${encodeURIComponent(title)}%22%20en%20Lienzos%20del%20Alma."
          target="_blank"
          rel="noopener noreferrer"
          class="contact-link"
        >
          <span>Conversar sobre esta obra</span>
          <b>↗</b>
        </a>

      </section>

    </main>


    <footer class="museum-footer">

      <div>
        <strong>Lienzos del Alma</strong>
        <span>${artist}</span>
      </div>

      <div>
        ${location}
      </div>

      <div>
        © 2026
      </div>

    </footer>
  `;

  document.documentElement.classList.add("premium-loaded");

})();

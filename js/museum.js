
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

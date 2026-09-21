(function(){

  const image = document.querySelector(".obra-image");
  const stage = document.querySelector(".obra-stage");
  const lightbox = document.querySelector(".lightbox");
  const lightboxImage = document.querySelector(".lightbox img");
  const closeButton = document.querySelector(".lightbox-close");

  if(!image || !stage) return;

  function classifyImage(){

    const width = image.naturalWidth;
    const height = image.naturalHeight;

    if(!width || !height) return;

    stage.classList.remove("vertical","horizontal","square");

    if(height > width){
      stage.classList.add("vertical");
    }else if(width > height){
      stage.classList.add("horizontal");
    }else{
      stage.classList.add("square");
    }
  }

  image.addEventListener("load",classifyImage);

  if(image.complete){
    classifyImage();
  }

  function openLightbox(){

    if(!lightbox || !lightboxImage) return;

    lightboxImage.src = image.currentSrc || image.src;
    lightboxImage.alt = image.alt || "";
    lightbox.classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function closeLightbox(){

    if(!lightbox) return;

    lightbox.classList.remove("open");
    document.body.style.overflow = "";
  }

  image.addEventListener("click",openLightbox);

  if(closeButton){
    closeButton.addEventListener("click",closeLightbox);
  }

  if(lightbox){
    lightbox.addEventListener("click",function(event){
      if(event.target === lightbox){
        closeLightbox();
      }
    });
  }

  document.addEventListener("keydown",function(event){

    if(event.key === "Escape"){
      closeLightbox();
    }

    if(event.key === "ArrowLeft"){
      const previous = document.querySelector("[data-previous]");
      if(previous) window.location.href = previous.href;
    }

    if(event.key === "ArrowRight"){
      const next = document.querySelector("[data-next]");
      if(next) window.location.href = next.href;
    }

  });

})();

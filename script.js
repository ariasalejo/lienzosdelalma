
document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('modal-zoom');
  const activeImg = document.getElementById('active-artwork');
  const lightboxImg = document.getElementById('lightbox-img');
  
  function openZoom() { lightboxImg.src = activeImg.src; modal.style.display = 'flex'; }
  function closeZoom() { modal.style.display = 'none'; }

  document.getElementById('btn-zoom').addEventListener('click', openZoom);
  activeImg.addEventListener('click', openZoom);
  document.getElementById('btn-close-modal').addEventListener('click', closeZoom);

  modal.addEventListener('click', (e) => { if (e.target === modal) closeZoom(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && modal.style.display === 'flex') closeZoom(); });
});

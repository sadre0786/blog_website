document.addEventListener("DOMContentLoaded", () => {
  const carousel = document.querySelector(".carousel");
  const dots = document.querySelectorAll(".dot");
  const slides = document.querySelectorAll(".carousel-item");
  const texts = document.querySelectorAll("[id^='text-']");
  let currentIndex = 0;

  // Update carousel position and text visibility
  const updateCarousel = () => {
    const offset = -currentIndex * 100; // Calculate translateX value
    carousel.style.transform = `translateX(${offset}%)`;

    dots.forEach((dot, index) => {
      dot.classList.toggle("bg-white", index === currentIndex);
      dot.classList.toggle("bg-gray-500", index !== currentIndex);
    });

    texts.forEach((text, index) => {
      text.classList.toggle("opacity-100", index === currentIndex);
      text.classList.toggle("opacity-0", index !== currentIndex);
      if (index === currentIndex) {
        text.classList.add("animate-slide-up");
      } else {
        text.classList.remove("animate-slide-up");
      }
    });
  };

  // Auto-slide every 3 seconds
  const autoSlide = () => {
    setInterval(() => {
      currentIndex = (currentIndex + 1) % slides.length;
      updateCarousel();
    }, 3000);
  };

  // Handle dot clicks
  dots.forEach((dot, index) => {
    dot.addEventListener("click", () => {
      currentIndex = index;
      updateCarousel();
    });
  });

  updateCarousel();
  autoSlide();
});

document.addEventListener("DOMContentLoaded", function () {
    // اختر كل سلايدر
    let sliders = document.querySelectorAll(".slider-container");

    // التكرار عبر كل سلايدر
    sliders.forEach((sliderContainer) => {
        let slider = sliderContainer.querySelector(".slider");
        let slides = slider.querySelectorAll(".slide");
        let totalSlides = slides.length;
        let currentIndex = 0;

        // تحديث السلايدر بناءً على الفهرس الحالي
        function updateSlider() {
            slider.style.transform = `translateX(-${currentIndex * 100}%)`;
        }

        // التعامل مع الزر السابق
        sliderContainer.querySelector(".prev").addEventListener("click", function () {
            currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
            updateSlider();
        });

        // التعامل مع الزر التالي
        sliderContainer.querySelector(".next").addEventListener("click", function () {
            currentIndex = (currentIndex + 1) % totalSlides;
            updateSlider();
        });

        // إعداد السلايدر عند تحميل الصفحة
        updateSlider();
        
    });
});

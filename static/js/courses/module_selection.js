document.addEventListener("DOMContentLoaded", function () {
    const moduleItems = document.querySelectorAll(".module-item");
    const moduleContents = document.querySelectorAll(".module-content");
    const moduleButtons = document.querySelectorAll(".module-button");

    moduleButtons.forEach(button => {
        button.addEventListener("click", function () {
            // Remove active state from all buttons
            moduleButtons.forEach(btn => btn.classList.remove("active"));

            // Add active state to clicked button
            this.classList.add("active");
        });
    });

    moduleItems.forEach(item => {
        item.addEventListener("click", function () {
            moduleItems.forEach(el => el.classList.remove("active"));
            this.classList.add("active");

            moduleContents.forEach(content => {
                if (!content.classList.contains("d-none")) {
                    content.style.marginLeft = "100%";
                    setTimeout(() => content.classList.add("d-none"), 600);
                }
            });

            const moduleId = this.getAttribute("data-module-id");
            const targetModule = document.getElementById(moduleId);

            setTimeout(() => {
                targetModule.classList.remove("d-none");
                targetModule.style.marginLeft = "100%";
                setTimeout(() => targetModule.style.marginLeft = "0", 50);
            }, 600);
        });
    });
});
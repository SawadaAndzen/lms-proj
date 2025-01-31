document.addEventListener("DOMContentLoaded", function () {
    const moduleItems = document.querySelectorAll(".module-item");
    const moduleContents = document.querySelectorAll(".module-content");

    moduleItems.forEach(item => {
        item.addEventListener("click", function () {
            moduleItems.forEach(el => el.classList.remove("active"));
            this.classList.add("active");

            moduleContents.forEach(content => content.classList.add("d-none"));

            const moduleId = this.getAttribute("data-module-id");
            document.getElementById(moduleId).classList.remove("d-none");
        });
    });
});
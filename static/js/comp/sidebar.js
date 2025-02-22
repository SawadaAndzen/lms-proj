document.addEventListener("DOMContentLoaded", function () {
    let sidebar = document.getElementById("sidebar");
    let content = document.getElementById("content");
    let toggleBtn = document.getElementById("toggleSidebar");

    let sidebarWidth = 230;

    toggleBtn.addEventListener("click", function () {
        if (sidebar.style.left === "-260px" || sidebar.style.left === "") {
            sidebar.style.left = "0";
            content.style.marginLeft = sidebarWidth + "px";
            content.style.width = `calc(100% - ${sidebarWidth}px)`;
        } else {
            sidebar.style.left = "-260px";
            content.style.marginLeft = "0";
            content.style.width = "100%";
        }
    });
});
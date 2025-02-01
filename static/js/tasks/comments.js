document.addEventListener("DOMContentLoaded", function () {
    var toggleButton = document.getElementById("toggleCommentsBtn");
    var commentsSection = document.getElementById("commentsSection");

    toggleButton.addEventListener("click", function () {
        if (commentsSection.style.display === "none") {
            commentsSection.style.display = "block";
            toggleButton.textContent = "Hide Comments";
        } else {
            commentsSection.style.display = "none";
            toggleButton.textContent = "Show Comments";
        }
    });
});
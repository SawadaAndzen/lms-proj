document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.querySelector("input[type='file']");
    const submitButton = document.getElementById("submit-btn");

    fileInput.addEventListener("change", function() {
        if (fileInput.files.length > 0) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    });

    submitButton.disabled = true;
});
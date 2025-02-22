document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.querySelector("input[type='file']");
    const previewContainer = document.getElementById("file-preview");

    fileInput.addEventListener("change", function(event) {
        previewContainer.innerHTML = "";

        if (fileInput.files.length > 0) {
            const file = fileInput.files[0];
            const fileName = file.name;
            const fileType = file.type;

            const previewElement = document.createElement("div");
            previewElement.classList.add("mt-2");

            if (fileType.startsWith("image/")) {
                const imgPreview = document.createElement("img");
                imgPreview.src = URL.createObjectURL(file);
                imgPreview.classList.add("img-fluid", "rounded", "mt-2");
                imgPreview.style.maxHeight = "80px";
                previewElement.appendChild(imgPreview);
            } else {
                previewElement.innerHTML = `<p class="text-muted small"><i class="bi bi-file-earmark"></i> ${fileName}</p>`;
            }

            previewContainer.appendChild(previewElement);
        }
    });
});
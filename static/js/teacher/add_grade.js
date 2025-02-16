document.addEventListener("DOMContentLoaded", function () {
    const gradeModal = document.getElementById("gradeModal");

    if (!gradeModal) {
        console.error("gradeModal not found");
        return;
    }

    gradeModal.addEventListener("show.bs.modal", function (event) {
        let button = event.relatedTarget;
        let answerId = button.getAttribute("data-answer-id");
        document.getElementById("answerId").value = answerId;
    });

    document.getElementById("gradeForm").addEventListener("submit", function (event) {
        event.preventDefault();
        let formData = new FormData(this);
        
        let csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value;

        fetch("/add-grade/", {
            method: "POST",
            body: formData,
            headers: { "X-CSRFToken": csrfToken }
        })
        .then(response => response.json())
        .then(data => {
            console.log("Отримано від сервера:", data);
        
            if (data.success) {
                alert("Grade was saved!");
        
                let gradeElement = document.querySelector(`#grade-${data.answer_id}`);
                if (gradeElement) {
                    gradeElement.textContent = `Grade: ${data.grade}`;
                } else {
                    console.error(`Елемент #grade-${data.answer_id} не знайдено`);
                }
        
                let modal = bootstrap.Modal.getInstance(gradeModal);
                modal.hide();
            } else {
                alert("Error saving grade.");
            }
        })
        .catch(error => console.error("Fetch error:", error));
    });
});
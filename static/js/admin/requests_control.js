document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".accept-btn").forEach(button => {
        button.addEventListener("click", function () {
            const requestId = this.getAttribute("data-id");

            fetch(`/join-request/accept/${requestId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.closest(".border").remove();
                } else {
                    alert("Error: " + data.message);
                }
            });
        });
    });

    document.querySelectorAll(".decline-btn").forEach(button => {
        button.addEventListener("click", function () {
            const requestId = this.getAttribute("data-id");

            fetch(`/join-request/decline/${requestId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.closest(".border").remove();
                } else {
                    alert("Error: " + data.message);
                }
            });
        });
    });
});

function getCSRFToken() {
    return document.querySelector("input[name=csrfmiddlewaretoken]").value;
}
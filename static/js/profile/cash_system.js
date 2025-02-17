document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("cash-form").addEventListener("submit", function (event) {
        event.preventDefault();

        let amount = document.getElementById("amount").value;
        let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

        fetch("/add-cash/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": csrfToken
            },
            body: new URLSearchParams({ amount: amount })
        })
        .then(response => response.json())
        .then(data => {
            let messageDiv = document.getElementById("cash-message");
            if (data.success) {
                messageDiv.innerHTML = `<div class="alert alert-success">${data.message} New balance: $${data.new_balance}</div>`;
                document.getElementById("amount").value = "";
                
                setTimeout(() => {
                    location.reload();
                }, 1000); 
            } else {
                messageDiv.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
            }
        })
        .catch(error => console.error("Error:", error));
    });
});
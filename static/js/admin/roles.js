document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("#create-role-form").addEventListener("submit", function (event) {
        event.preventDefault();
        let actionUrl = "/role/create/";

        fetch(actionUrl, {
            method: "POST",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams(new FormData(this))
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                alert("Error creating role");
            }
        })
        .catch(error => console.error("Error:", error));
    });

    document.querySelectorAll(".update-btn").forEach(button => {
        button.addEventListener("click", function () {
            let modal = document.querySelector("#updateRoleModal");
            modal.querySelector("[name=id]").value = this.dataset.id;
            modal.querySelector("[name=role]").value = this.dataset.role;
            
            let userSelect = modal.querySelector("[name=user]");
            userSelect.value = this.dataset.userId;

            let actionUrl = `/role/edit/${this.dataset.id}/`;
            document.querySelector("#update-role-form").setAttribute("action", actionUrl);
        });
    });

    document.querySelector("#update-role-form").addEventListener("submit", function (event) {
        event.preventDefault();
        let actionUrl = this.getAttribute("action");

        fetch(actionUrl, {
            method: "POST",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams(new FormData(this))
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                alert("Error updating role");
            }
        })
        .catch(error => console.error("Error:", error));
    });

    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function () {
            let actionUrl = `/role/delete/${this.dataset.id}/`;
            document.querySelector("#delete-role-form").setAttribute("action", actionUrl);
        });
    });

    document.querySelector("#delete-role-form").addEventListener("submit", function (event) {
        event.preventDefault();
        let actionUrl = this.getAttribute("action");

        fetch(actionUrl, {
            method: "POST",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams(new FormData(this))
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            } else {
                alert("Error deleting role");
            }
        })
        .catch(error => console.error("Error:", error));
    });
});
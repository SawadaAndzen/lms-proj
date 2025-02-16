document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("#create-class-form").addEventListener("submit", function (event) {
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
                alert("Error creating class");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Something went wrong. Check the console for details.");
        });
    });

    document.querySelectorAll(".update-btn").forEach(button => {
        button.addEventListener("click", function () {
            let modal = document.querySelector("#updateClassModal");
            modal.querySelector("[name=id]").value = this.dataset.id;
            modal.querySelector("[name=name]").value = this.dataset.name;
            modal.querySelector("[name=desc]").value = this.dataset.desc;
            modal.querySelector("[name=course]").value = this.dataset.course;
            modal.querySelector("[name=teacher]").value = this.dataset.teacher;
    
            let studentSelect = modal.querySelector("[name='students']");
            
            [...studentSelect.options].forEach(option => {
                option.selected = false;
            });
    
            let selectedStudents = JSON.parse(this.dataset.students);
            selectedStudents.forEach(studentId => {
                let option = studentSelect.querySelector(`option[value="${studentId}"]`);
                if (option) {
                    option.selected = true;
                }
            });
    
            let actionUrl = `/groups/edit/${this.dataset.id}/`;
            document.querySelector("#update-class-form").setAttribute("action", actionUrl);
        });
    });
    

    document.querySelector("#update-class-form").addEventListener("submit", function (event) {
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
                let updatedClassItem = document.querySelector(`.class-item[data-id="${data.id}"]`);
                updatedClassItem.querySelector("strong").innerText = `@${data.name}`;
                updatedClassItem.querySelector("small").innerText = `${data.course_name}`;
                location.reload();
            } else {
                alert("Error updating class");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Something went wrong. Check the console for details.");
        });
    });

    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", function () {
            document.querySelector("#delete-class-name").innerText = this.dataset.name;
            let actionUrl = `/groups/delete/${this.dataset.id}/`;
            console.log("Delete URL:", actionUrl);
            document.querySelector("#delete-class-form").setAttribute("action", actionUrl);
        });
    });

    document.querySelector("#delete-class-form").addEventListener("submit", function (event) {
        event.preventDefault();
        let actionUrl = this.getAttribute("action");
        console.log("Deleting class at:", actionUrl);

        fetch(actionUrl, {
            method: "POST",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams(new FormData(this))
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                console.log("Delete successful:", data);
                location.reload();
            } else {
                alert("Error deleting class");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Something went wrong. Check the console for details.");
        });
    });
});
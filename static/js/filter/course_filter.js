document.getElementById("FilterButton").addEventListener("click", function (event) {
    event.preventDefault();
    
    var minPrice = document.getElementById("min_price").value;
    var maxPrice = document.getElementById("max_price").value;

    fetch(`/courses/filter/${minPrice}/${maxPrice}/`, { method: "GET" })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            let coursesRow = document.getElementById("CoursesRow");
            coursesRow.innerHTML = "";

            if (data.length === 0) {
                coursesRow.innerHTML = "<p class='text-center text-danger'>No courses found.</p>";
                return;
            }

            data.forEach(course => {
                let priceText = course.price > 0 ? `${course.price}$` : "FREE";
                let courseHTML = `
                    <div class="col-md-auto col-lg-auto ms-auto me-auto">
                        <div class="card mb-4 overflow-hidden position-relative" style="max-height: 400px;">
                            <div class="card-body">
                                <h3>
                                    <div class="bg-image rounded-4"></div>
                                    <h4 class="display-4 fs-2">${course.name}</h4>
                                    <h6
                                    class = "text-muted fs-6"
                                    style = "width: 450px; white-space: nowrap; 
                                    overflow: hidden; 
                                    text-overflow: ellipsis;">
                                        ${course.desc}
                                    </h6>
                                    <div class = 'd-flex justify-content-between'>
                                        <a class = "btn btn-primary" href = "course/id=${course.id}/info">
                                            <i class="bi bi-eye bi-primary"></i> Read
                                        </a>
                                        <text class = "display-4 fs-6 text-white">${priceText}</text>
                                    </div>
                                </h3>
                            </div>
                        </div>
                    </div>`;
                coursesRow.innerHTML += courseHTML;
            });
        })
        .catch(error => console.log('Error:', error));
});
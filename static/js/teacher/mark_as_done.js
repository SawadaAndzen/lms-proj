function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]')?.value ||
           document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
}


document.querySelectorAll('.toggle-task-status').forEach(button => {
    button.addEventListener('click', function() {
        const answerId = this.dataset.answerId.trim();

        fetch(toggleTaskStatusUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ 'answer_id': answerId })
        })        
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const statusText = document.getElementById('task-status-' + answerId);
                const buttonText = this;

                if (data.is_done) {
                    statusText.innerHTML = `<i class="bi bi-check-circle text-success"></i>`;
                    buttonText.innerHTML = '<small>Undone</small>';
                } else {
                    statusText.innerHTML = `<i class="bi bi-slash-circle text-danger"></i>`;
                    buttonText.innerHTML = '<small>Done</small>';
                }
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('upload-form');
    const progressContainer = document.getElementById('progress-container');
    const progressBar = document.getElementById('progress-bar');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Prepare the form data
        const formData = new FormData(form);

        // Create an AJAX request
        const xhr = new XMLHttpRequest();
        xhr.open('POST', form.action, true);

        // Add CSRF token header
        xhr.setRequestHeader('X-CSRFToken', form.querySelector('[name=csrfmiddlewaretoken]').value);

        // Show the progress bar
        progressContainer.style.display = 'block';

        // Track the upload progress
        xhr.upload.addEventListener('progress', function (e) {
            if (e.lengthComputable) {
                const percentComplete = (e.loaded / e.total) * 100;
                progressBar.style.width = percentComplete + '%';
            }
        });

        // Handle the upload completion
        xhr.onload = function () {
            if (xhr.status === 200) {
                alert('Upload successful!');
                progressBar.style.width = '0%'; // Reset progress bar
                form.reset(); // Reset the form
            } else {
                alert('An error occurred during the upload.');
            }
        };

        // Send the form data
        xhr.send(formData);
    });
});

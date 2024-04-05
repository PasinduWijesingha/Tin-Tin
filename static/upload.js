document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData();
    const fileInput = document.getElementById('fileInput');
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        document.getElementById('message').textContent = data.message;
    } catch (error) {
        console.error('Error:', error);
    }
});

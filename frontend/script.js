document.getElementById('submitBtn').addEventListener('click', function() {
    const code = monaco.editor.getModels()[0].getValue();
    
    fetch('/api/submit_code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('feedbackMessage').innerText = `Response: ${data.message}, Code: ${data.code}`;
        $('#feedbackModal').modal('show');  // Show the modal
    })
    .catch(error => {
        document.getElementById('feedbackMessage').innerText = `Error: ${error.message}`;
        $('#feedbackModal').modal('show');  // Show the modal
    });
});

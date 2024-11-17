async function saveDocument(docId) {
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    const response = await fetch('/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: docId, title, content })
    });

    if (response.ok) {
        alert('Document saved successfully!');
        window.location.href = '/';
    } else {
        alert('Failed to save document.');
    }
}

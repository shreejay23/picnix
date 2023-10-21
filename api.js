const formData = new FormData();
formData.append('image', new File(['./some.png'], 'some.png'));

fetch('http://127.0.0.1:8000/upload/', {
    method: 'POST',
    body: formData,
});
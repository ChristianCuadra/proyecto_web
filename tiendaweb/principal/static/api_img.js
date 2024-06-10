const apiKey = '1hL6Rcu5Q7kVyHIlauxyHZprRIuamE25sgH6uRIWCO7tLI6rup6CcpXU'; // Reemplaza 'Tu-Clave-de-API' con tu clave de API

const gallery = document.getElementById('gallery');

const storedImageURL = localStorage.getItem('imageURL');

if (storedImageURL) {
    // Si hay una URL de imagen almacenada, mostrarla directamente
    const image = document.createElement('img');
    image.src = storedImageURL;
    gallery.appendChild(image);
} else {
    // Generar un número aleatorio entre 1 y 10 (cambia según el número total de páginas en la API)
    const randomPage = Math.floor(Math.random() * 10) + 1;

    fetch(`https://api.pexels.com/v1/search?query=people&page=${randomPage}&per_page=1`, {
        headers: {
            Authorization: apiKey
        }
    })
    .then(response => response.json())
    .then(data => {
        // Procesar los datos recibidos
        const photo = data.photos[0];
        const imageURL = photo.src.large;

        // Almacenar la URL de la imagen en localStorage
        localStorage.setItem('imageURL', imageURL);

        // Mostrar la imagen en la galería
        const image = document.createElement('img');
        image.src = imageURL;
        gallery.appendChild(image);
    })
    .catch(error => console.log(error));
}
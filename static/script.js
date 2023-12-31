console.log("Hello")

document.addEventListener('DOMContentLoaded', function() {
    var getImagesButton = document.getElementById('get-images-button');

    if (getImagesButton) {
        getImagesButton.addEventListener('click', function() {
            console.log('Button clicked. Calling getImages...');
            getImages();
        });
    }
});

function getImages() {
    var storyTextElement = document.getElementById('text-container');
    var storyText = storyTextElement.textContent.trim();

    console.log('Text for image retrieval:', storyText);

    // Use Fetch API for AJAX request
    fetch('/get_images', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: storyText }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(images => {
        console.log('Images received:', images);
        displayImages(images);
    })
    .catch(error => {
        console.error('Error fetching images:', error);
    });
}

function displayImages(images) {
    var imageContainer = document.getElementById('image-container');

    if (imageContainer) {
        imageContainer.innerHTML = '';

        images.forEach(function(imageSrc) {
            var imgElement = document.createElement('img');
            imgElement.src = imageSrc;
            imageContainer.appendChild(imgElement);

            console.log('Image added:', imageSrc);
        });
    }
}

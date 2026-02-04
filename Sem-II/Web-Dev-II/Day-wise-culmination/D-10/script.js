// Wait for the DOM to load before executing
document.addEventListener('DOMContentLoaded', function() {
    // Create new element and set its content
    const newParagraph = document.createElement('p');
    newParagraph.textContent = 'This is a dynamically added paragraph.';
    document.body.appendChild(newParagraph);

    // Append the new element in the container
    const container = document.getElementById('container');
    container.appendChild(newParagraph);

    // Remove the content of the container
    document.querySelector('#container p').remove();

    const image = document.createElement("img");
    image.setAttribute("src", "https://picsum.photos/300/200");
    image.setAttribute("alt", "Placeholder Image");
    document.body.appendChild(image);
});

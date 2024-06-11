document.addEventListener('DOMContentLoaded', (event) => {
    const mainDiv = document.getElementById('main');
    const dateParagraph = mainDiv.querySelector('.date');
    const h1Element = mainDiv.querySelector('h1');
    mainDiv.insertBefore(dateParagraph, h1Element.nextSibling);
});

document.addEventListener('DOMContentLoaded', (event) => {
    const pasteButton = document.getElementById('paste-button');
    const urlInput = document.querySelector('input[name="url"]');

    pasteButton.addEventListener('click', () => {
        navigator.clipboard.readText()
            .then(text => {
                urlInput.value = text;
            })
            .catch(err => {
                console.error('Failed to read clipboard contents: ', err);
            });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var currentUrl = window.location.pathname;
    var navLinks = document.querySelectorAll('.nav-links a');

    navLinks.forEach(function(link) {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });
});

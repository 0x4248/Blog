/* MarkdownBlog
 * Write blogs in markdown and generate static html files that are
 * ready to be served by a web server and are hackable.
 * Github: https://www.github.com/0x4248/MarkdownBlog
 * Licence: GNU General Public License v3.0
 * By: 0x4248 
 *
 * content/js/pre_copy.js
 * This script adds a copy button to all pre tags so that users 
 * can easily copy the code snippets to their clipboard.
*/

function createCopyButton(preTag) {
    const button = document.createElement('button');
    button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clipboard" viewBox="0 0 16 16"><path d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1z"/><path d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0z"/></svg>';
    button.classList.add('copy-button');
    button.addEventListener('click', () => {
        const text = preTag.textContent;
        navigator.clipboard.writeText(text)
            .then(() => animateButton()).catch(err => console.error('Failed to copy: ', err));
    });
    return button;
}

const preTags = document.querySelectorAll('pre');
preTags.forEach(preTag => {
    const copyButton = createCopyButton(preTag);
    preTag.appendChild(copyButton);
});
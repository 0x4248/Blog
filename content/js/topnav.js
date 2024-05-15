/* MarkdownBlog
 * Write blogs in markdown and generate static html files that are
 * ready to be served by a web server and are hackable.
 * Github: https://www.github.com/0x4248/MarkdownBlog
 * Licence: GNU General Public License v3.0
 * By: 0x4248 
 *
 * content/js/topnav.js
 * This script makes the topnav smaller when the user scrolls down
 * and makes it bigger when the user scrolls to the top.
*/

window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
        makeTopnavSmaller();
    } else {
        makeTopnavBigger();
    }
});


function makeTopnavBigger() {
    const sitename = document.querySelector('.sitename');
    sitename.style.transition = 'font-size 0.5s';
    sitename.style.fontSize = '1.5rem';

}

function makeTopnavSmaller() {
    const sitename = document.querySelector('.sitename');
    sitename.style.transition = 'font-size 0.5s';
    sitename.style.fontSize = '1rem';
}
/* MarkdownBlog
 * Write blogs in markdown and generate static html files that are
 * ready to be served by a web server and are hackable.
 * Github: https://www.github.com/0x4248/MarkdownBlog
 * Licence: GNU General Public License v3.0
 * By: 0x4248 
 * 
 * content/js/checks.js
 * This file checks for the existence of the custom CSS file
 * and logs an error if it doesn't exist
*/


function checkForCustomCSS() {
    fetch('/content/css/custom.css')
    .then(response => {
        if (!response.ok) {
            console.error('MarkdownBlog [checks.js]:\nThe custom CSS file was not found\nYou can create it by running the following command:\n\nmake css-create-custom\n\nThat only applies if you want a custom CSS file')
        }
    })
}

checkForCustomCSS();
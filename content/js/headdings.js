/* MarkdownBlog
 * Write blogs in markdown and generate static html files that are
 * ready to be served by a web server and are hackable.
 * Github: https://www.github.com/0x4248/MarkdownBlog
 * Licence: GNU General Public License v3.0
 * By: 0x4248 
 * 
 * content/js/headdings.js
 * Tags all the headdings with ids based on their content
*/

function tagHeaddings() {
    const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
    headings.forEach((heading, index) => {
        heading.id = heading.innerHTML.replace(/\s+/g, '-').toLowerCase();
    });
}

tagHeaddings();
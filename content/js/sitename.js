/* MarkdownBlog
 * Write blogs in markdown and generate static html files that are
 * ready to be served by a web server and are hackable.
 * Github: https://www.github.com/0x4248/MarkdownBlog
 * Licence: GNU General Public License v3.0
 * By: 0x4248 
 * 
 * content/js/sitename.js
 * Reads the config file and sets the site name in the title
*/

function setSiteName() {
    fetch('/config/siteconf.json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('sitename').innerHTML = data.sitename;
    })
    .catch(error => console.error("Your sitename is not set in the config file."))
}

setSiteName();
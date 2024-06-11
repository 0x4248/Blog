/* MarkdownBlog
 * Write blogs in markdown and generate static html files that are
 * ready to be served by a web server and are hackable.
 * Github: https://www.github.com/0x4248/MarkdownBlog
 * Licence: GNU General Public License v3.0
 * By: 0x4248 
 * 
 * content/js/posts.js
 * Main javascript file for the posts page
*/

function getPosts() {
    fetch('/pages/sitemap.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        let main = document.getElementById('main');
        let fragment = document.createDocumentFragment();

        data.pages.sort((a, b) => new Date(b.Date) - new Date(a.Date));

        data.pages.forEach(page => {
            let a = document.createElement('a');
            a.href = page.location;
            let h2 = createElementWithText('h2', page.Title);
            a.appendChild(h2);

            let date = createElementWithText('p', page.Date);
            let description = createElementWithText('p', page.Description);
            let tags = document.createElement('div');
            tags.className = 'tags';

            let tagsTitle = createElementWithText('p', 'Tags:');
            tags.appendChild(tagsTitle);
            tagsTitle.className = 'no_tags_bg';


            page.Tags.forEach(tag => {
                let tagElement = createElementWithText('p', tag);
                tags.appendChild(tagElement);
            });

            fragment.appendChild(a);
            fragment.appendChild(date);
            fragment.appendChild(description);
            fragment.appendChild(tags);
        });

        main.appendChild(fragment);
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}

function createElementWithText(tag, text) {
    let element = document.createElement(tag);
    let textNode = document.createTextNode(text);
    element.appendChild(textNode);
    return element;
}

getPosts();

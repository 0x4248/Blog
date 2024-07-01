function get_page_name() {
    return window.location.href.split("/")[5];
}

function get_raw_link() {
    return "https://raw.githubusercontent.com/0x4248/Blog/main/content/pages/" + get_page_name() + "/page.md";
}

function add_other_links() {
    var other_links = document.createElement("div");
    other_links.innerHTML = "<h2>Other links</h2><ul><li><a href='" + get_raw_link() + "'>Markdown RAW</a></li></ul>";
    document.getElementById("main").appendChild(other_links);
}

add_other_links();  
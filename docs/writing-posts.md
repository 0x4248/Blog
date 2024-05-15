# Writing Posts

To write a post, create a new directory in `content/posts` and add a `meta.json` and `post.md` file.

For example:

```
└── content
    ├── css
    ├── html
    ├── img
    ├── js
    └── pages
        ├── home
        │   ├── meta.json
        │   └── page.md
        └── new-page
            ├── meta.json
            └── page.md
```

The `meta.json` file contains the metadata for the page, such as the title and description. The `page.md` file contains the content of the page in Markdown format.

### Example `meta.json`

```json
{
    "location": "/sunday_trip/index.html",
    "Title": "Sunday Trip",
    "Description": "A trip to the beach on a sunny Sunday",
    "Keywords": ["beach", "sunday", "trip"],
    "Author": "John Doe",
    "Image": "/content/img/beach.jpg"
}
```

This file mostly contains the metadata for the page, such as the title, description, keywords, author, and image.

### Example `page.md`

```markdown
# Sunday Trip

This is a trip to the beach on a sunny Sunday.
...
```

## How to add images?

To add images, place them in the `content/img` directory and reference them in the `meta.json` file or on your pages.

```json
{
    ...
    "Image": "/content/img/beach.jpg"
}
```

```markdown
![Beach](/content/img/beach.jpg)
```
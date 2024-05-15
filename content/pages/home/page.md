# Hello world from Markdown blog


If you can see this page looks like its all working and ready to go!

## What's next?

Write pages in `content/pages` and run `make` again and it will update this site with your changes.

## Where is this file located?

This file is located at `content/pages/home/page.md`.

```
└── content
    ├── css
    ├── html
    ├── img
    ├── js
    └── pages
        └── home
            ├── meta.json
            └── page.md   <--- This file
```

You can edit this page to change the content of the home page and run `make` to rebuild the site.

## How to add new pages?

To add a new page, create a new directory in `content/pages` and add a `meta.json` and `page.md` file.

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

## Learn more

To learn more about how to use MarkdownBlog, please read the documentation.
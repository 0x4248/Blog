## What is obsidian? 
Obsidian is a markdown note taking app that is heavily customisable and and be used for almost any type of notes.

<img src="https://0x4248.github.io/Blog/content/img/Vault demo.png">

## Why do I use it?
I use obsidian to organise my ideas, projects and knowledge. Obsidian uses a note linking system that allows you to link other notes using links and tags which makes a graph of your notes which can be helpful in organising notes.

If you want to download my vault template you can do so [here](https://github.com/0x4248/My_obsidian_vault_template)

```
git clone https://github.com/0x4248/My_obsidian_vault_template
```

## Vault configuration
My vault is configured in a way that makes it easy to navigate between the different parts of my life and to make it quick and easy to format pages with just a few taps.
### Extensions
Firstly lets talk about what extensions i'm using. Im currently using the following:
- Home tab
- Kanban
- Exalidraw
- Completr
- File color
- Iconize
- Templater
- Projects
- Vault statstics
- Advanced slides
- Calendar
- Linter
#### Home tab
Home tab is a plugin that puts a search page on each new tab to quickly find files
#### Kanban
Kanban is a plugin that allows you to create kanban boards in obsidian to keep track of tasks and projects.
#### Exalidraw
Exalidraw is a plugin that allows you to create diagrams in obsidian.
#### Completr
Completr is a plugin that allows you to autocomplete whole words to speed up typing.
#### File color
File color is a plugin that allows you to colour code files in obsidian.
#### Iconize
Iconize is a plugin that allows you to add icons to files in obsidian.
#### Templater
Templater is a plugin that allows you to create templates for notes in obsidian to speed up note taking.
#### Projects
Projects is a plugin that allows you to create projects in obsidian to keep track of tasks and notes.
#### Vault statstics
Vault statistics is a plugin that allows you to see statistics about your vault.
#### Advanced slides
Advanced slides is a plugin that allows you to create slides in obsidian.
#### Calendar
Calendar is a plugin that allows you to create a calendar in obsidian.
#### Linter
Linter is a plugin that checks your markdown for errors.
### File structure
My vault is structured in a way that sections out the different types of notes.
- 00 Maps
- 01 Areas
- 02 Daily
- 03 Fleeting
- 04 Archive
- 05 Projects
- 06 Meta
#### Maps
Maps are files that contain links to parts of my vault. There like mini maps for sections of my vault to help me find my way around the vault.
#### Areas
Areas is the different interests and areas of my life that I have notes on. In my vault there are the following sub folders:
- Programming
- Cybersecurity
- Linux
- Home
- Hardware
- Networks
- Furry
- College

In your vault you can have any thing:
- Cooking
- Gardening
- Writing
- Movies
#### Daily
In here I have notes that are daily notes that I write to keep track of what I have done that day and things I have read or watched.

I use template to autofill things like the date and basic structure of the page.
#### Fleeting
Fleeting notes are notes that are quick notes that I write down to remember things or ideas that I have and want to quickly write down.
#### Archive
Archive is where I put notes that are no longer relevant or old notes that I don't need to see all the time.

Keeping archived notes is good because you can always go back and look at them if you need to.
#### Projects
Projects is where I keep notes on projects that I am working on.
#### Meta
Meta is where configuration files, templates and other notes for the obsidian app are kept.
### Templates
With the templater extension you can crate templates for notes to speed up note taking.
#### Daily
Template for daily notes:
```markdown
---
tags:
  - Daily_note
date: <%tp.date.now("YYYY-MM-DD")%>
cssclasses:
  - daily
---
# DAILY NOTE
## <%tp.date.now("DD-MM-YYYY")%>
***
### Overview
INSERT
### Events
#### Morning
INSERT
#### Afternoon
INSERT
#### Evening
INSERT
### Articles and sites read
- INSERT
- SITES
```

We will talk about CSS classes in a bit.

#### Base note
Template for general notes:
```markdown
---
tags: 
cssclasses:
  - neo-headings
  - bai-headings
  - rounded-images
---
# <% tp.file.title %> 
<p class="center" style="margin:0;color:gray;">Subtitle</p>

***
```
### CSS Snippets
There are many CSS classes that I use. Many of which are inspired by [CyanVoxel's obsidian vault template](https://github.com/CyanVoxel/Obsidian-Vault-Template). CSS Snippets 
#### Daily
- `Daily` sets the daily note theme
#### Tweaks
- `neo-headings` Sets the headings to the neo style
- `rounded-images` Sets images to have a rounded border
- `no-embed-border` Removes border around embeds
- `center` Center all text
- `center-headings` Center headings
- `center-main-headings` Center main headings 
- `space-images` Spaces images out
#### Fonts
- `gohu-font`
- `ms-dos-font`
- `bai-font`
- `kode-font`
- `sriracha-font`
- `kode-headings`
- `sriracha-headings`
- `bai-headings`
#### Snippets
##### Daily
```css
:root {
  --h1: #afc7f5;
  --text: #ffffff;
  --primary: #aaaaaa;
  --grey: #a7a7a7;
  --background: #171c26;
  --light-block: #bcbcbc98;
}

.daily {
  background-color: var(--background);
  color: var(--text);
}

.daily :is(
  h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  .HyperMD-header.HyperMD-header-1,
  .HyperMD-header.HyperMD-header-2,
  .HyperMD-header.HyperMD-header-3,
  .HyperMD-header.HyperMD-header-4,
  .HyperMD-header.HyperMD-header-5,
  .HyperMD-header.HyperMD-header-6
) {
  font-family: "Bai Jamjuree", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}

.daily :is(h1, .HyperMD-header.HyperMD-header-1) {
  color: var(--h1);
  text-align: center;
  font-size: 60px;
  padding: 0 !important;
}

.daily :is(h2, .HyperMD-header.HyperMD-header-2) {
  color: var(--grey);
  text-align: center;
  font-size: 30px;
  padding: 0 !important;
}

.daily :is(h3, .HyperMD-header.HyperMD-header-3) {
  color: var(--primary);
  font-size: 32px;
  padding-top: 0;
}

.daily :is(h4, .HyperMD-header.HyperMD-header-4) {
  background-color: var(--light-block);
  color: var(--text);
  font-weight: 900;
  font-size: 20px;
  padding: 0 6px;
  margin: 0;
  border-radius: 8px;
  width: fit-content;
  word-wrap: normal;
}
```

##### Neo headings
Neo headings sets new sizes for the headings and centers the h1 heading.
```css
.neo-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--primary);
    text-align: center;
    font-size: 40px;
}

.neo-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--primary);
    font-size: 32px;
}
  
.neo-headings :is(h3, .HyperMD-header.HyperMD-header-3) {

    font-size: 25px;
}
  
.neo-headings :is(h4, .HyperMD-header.HyperMD-header-4) {
    font-size: 20px;
}
  
.neo-headings :is(h5, .HyperMD-header.HyperMD-header-5) {
    font-size: 18px;
}
  
.neo-headings :is(h6, .HyperMD-header.HyperMD-header-6) {
    font-size: 16px;
}
```

##### Base tweaks
```css
body {
    --tag-color: #eaeaeae2;
    --tag-background: #5b5b5b9c;
    --code-background: #1b1b1bbb;
}

.center {
    text-align: center;
}


.callout {
    border-radius: 10px;
    border-width: 2px;
}
```
##### Image tweaks

```css
.space-images img {
    margin-right: 10px;
    margin-top: 10px;
}

.rounded-images img {
    border-radius: 10px;
}

.center-images img {
    display: block !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
```

##### Center headings
```css
.center-headings:is(h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    .HyperMD-header.HyperMD-header-1,
    .HyperMD-header.HyperMD-header-2,
    .HyperMD-header.HyperMD-header-3,
    .HyperMD-header.HyperMD-header-4,
    .HyperMD-header.HyperMD-header-5,
    .HyperMD-header.HyperMD-header-6) {
    text-align: center;
}


.center-headings:is(h1,
    h2,
    h3,
    .HyperMD-header.HyperMD-header-1,
    .HyperMD-header.HyperMD-header-2,
    .HyperMD-header.HyperMD-header-3) {
    text-align: center;
}
```

#### Fonts
The main font in the vault is Jetbrains Mono with neardfonts. Here are all the fonts I use.
- GohuFont uni11 Nerd Font Mono
- Perfect DOS VGA 437
- Bai Jamjuree
- Kode Mono
- Sriracha
##### CSS snippet
```css
.gohu-font {
  --font-text: "GohuFont uni11 Nerd Font Mono", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}

.ms-dos-font {
  --font-text: "Perfect DOS VGA 437", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}

.bai-font {
  --font-text: "Bai Jamjuree", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}

.kode-font {
  --font-text: "Kode Mono", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}

.sriracha-font {
  --font-text: "Sriracha", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}

.bai-headings :is(h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  .HyperMD-header.HyperMD-header-1,
  .HyperMD-header.HyperMD-header-2,
  .HyperMD-header.HyperMD-header-3,
  .HyperMD-header.HyperMD-header-4,
  .HyperMD-header.HyperMD-header-5,
  .HyperMD-header.HyperMD-header-6) {
  font-family: "Bai Jamjuree", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}

.kode-headings :is(h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  .HyperMD-header.HyperMD-header-1,
  .HyperMD-header.HyperMD-header-2,
  .HyperMD-header.HyperMD-header-3,
  .HyperMD-header.HyperMD-header-4,
  .HyperMD-header.HyperMD-header-5,
  .HyperMD-header.HyperMD-header-6) {
  font-family: "Kode Mono", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}

.sriracha-headings :is(h1,
  h2,
  h3,
  h4,
  h5,
  h6,
  .HyperMD-header.HyperMD-header-1,
  .HyperMD-header.HyperMD-header-2,
  .HyperMD-header.HyperMD-header-3,
  .HyperMD-header.HyperMD-header-4,
  .HyperMD-header.HyperMD-header-5,
  .HyperMD-header.HyperMD-header-6) {
  font-family: "Sriracha", "JetBrainsMono Nerd Font Mono", "JetBrains Mono";
}
```
#### Page colours
I colour my pages to help give my notes more life and to help separate parts of my notes 

<img src="https://0x4248.github.io/Blog/content/img/Page colours 1.png">

<img src="https://0x4248.github.io/Blog/content/img/Page colours 2.png">

##### Blue
```css
:root {
    --background-blue: #181f30;
    --text-blue-h1: #b9d0ff;
    --text-blue-h2: #c5d8ff;
    --text-blue-h3: #b2bedc;
}

.page-blue {
    background-color: var(--background-blue);
    --hr-color: #737a95;
}

.page-blue-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--text-blue-h1);
    text-align: center;
    font-size: 40px;
}

.page-blue-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--text-blue-h2);
    font-size: 32px;
}

.page-blue-headings :is(h3, .HyperMD-header.HyperMD-header-3) {
    color: var(--text-blue-h3);
}
```
##### Blue darker
```css
:root {
    --background-blue-darker: #11161f;
    --text-blue-darker-h1: #d7ddea;
    --text-blue-darker-h2: #b3c1dc;
    --text-blue-darker-h3: #afb9d3;
}

.page-blue-darker {
    background-color: var(--background-blue-darker);
    --hr-color: #737a95;
}

.page-blue-darker-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--text-blue-darker-h1);
    text-align: center;
    font-size: 40px;
}

.page-blue-darker-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--text-blue-darker-h2);
    font-size: 32px;
}

.page-blue-darker-headings :is(h3, .HyperMD-header.HyperMD-header-3) {
    color: var(--text-blue-darker-h3);
}
```
##### Mountain
```css
:root {
    --background-mountain: #22252b;
    --text-mountain-h1: #f2f5fa;
    --text-mountain-h2: #b8c2d8;
    --text-mountain-h3: #c2d2e1;
}

.page-mountain {
    background-color: var(--background-mountain);
    --hr-color: #737583;
}

.page-mountain-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--text-mountain-h1);
    text-align: center;
    font-size: 40px;
}

.page-mountain-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--text-mountain-h2);
    font-size: 32px;
}

.page-mountain-headings :is(h3, .HyperMD-header.HyperMD-header-3) {
    color: var(--text-mountain-h3);
}
```
##### Moonlight
```css
:root {
    --background-moonlight: #181e29;
    --text-moonlight-h1: #bed1f4;
    --text-moonlight-h2: #b9c0d0;
    --text-moonlight-h3: #c2c2c2;
}

.page-moonlight {
    background-color: var(--background-moonlight);
    --hr-color: #737583;
}

.page-moonlight-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--text-moonlight-h1);
    text-align: center;
    font-size: 40px;
}

.page-moonlight-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--text-moonlight-h2);
    font-size: 32px;
}

.page-moonlight-headings :is(h3, .HyperMD-header.HyperMD-header-3) {
    color: var(--text-moonlight-h3);
}
```

##### Granite
```css
:root {
    --background-granite: #18191c;
    --text-granite-h1: #d7e5ff;
    --text-granite-h2: #d6e0f3;
    --text-granite-h3: #9aa9c5f1;
}

.page-granite {
    background-color: var(--background-granite);
    --hr-color: #8594ae;
    color: #dbdbdb;
}

.page-granite-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--text-granite-h1);
    text-align: center;
    font-size: 40px;
}

.page-granite-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--text-granite-h2);
    font-size: 32px;
}

.page-granite-headings :is(h3, .HyperMD-header.HyperMD-header-3) {
    color: var(--text-granite-h3);
}
```

##### Slate
```css
:root {
    --background-slate: #262626;
    --text-slate-h1: #dadada;
    --text-slate-h2: #c3c3c3;
    --text-slate-h3: #bababa;
}

.page-slate {
    background-color: var(--background-slate);
    --hr-color: #aeaeae;
    color: #afafaf;
}

.page-slate-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--text-slate-h1);
    text-align: center;
    font-size: 40px;
}

.page-slate-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--text-slate-h2);
    font-size: 32px;
}

.page-slate-headings :is(h3, .HyperMD-header.HyperMD-header-3) {
    color: var(--text-slate-h3);
}
```
##### Sand
```css
:root {
    --background-sand: #352f2a;
    --text-sand-h1: #ece1cc;
    --text-sand-h2: #f2e5c5;
    --text-sand-h3: #e4d5b2;
}

.page-sand {
    background-color: var(--background-sand);
    --hr-color: #ccb58d;
    color: #e3d8c5;
}

.page-sand-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--text-sand-h1);
    text-align: center;
    font-size: 40px;
}

.page-sand-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--text-sand-h2);
    font-size: 32px;
}

.page-sand-headings :is(h3, .HyperMD-header.HyperMD-header-3) {
    color: var(--text-sand-h3);
}
```
##### Dusk
```css
:root {
    --background-dusk: #2d261f;
    --text-dusk-h1: #fff9ee;
    --text-dusk-h2: #e7dfca;
    --text-dusk-h3: #e4dbc8;
}

.page-dusk {
    background-color: var(--background-dusk);
    --hr-color: #e2d0b2;
    color: #e7d8c0;
}

.page-dusk-headings :is(h1, .HyperMD-header.HyperMD-header-1) {
    color: var(--text-dusk-h1);
    text-align: center;
    font-size: 40px;
}

.page-dusk-headings :is(h2, .HyperMD-header.HyperMD-header-2) {
    color: var(--text-dusk-h2);
    font-size: 32px;
}

.page-dusk-headings :is(h3, .HyperMD-header.HyperMD-header-3) {
    color: var(--text-dusk-h3);
}
```

## Inspiration 
I took heavy inspiration from Cyan Voxel's video that he made.
<iframe width="560" height="315" src="https://www.youtube.com/embed/rAkerV8rlow?si=DvOwOc4M_ALg87Le" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I also used his [obsidian vault template](https://github.com/CyanVoxel/Obsidian-Vault-Template) as a reference.

Again you want to download my vault template you can do so [here](https://github.com/0x4248/My_obsidian_vault_template)

```
git clone https://github.com/0x4248/My_obsidian_vault_template
```
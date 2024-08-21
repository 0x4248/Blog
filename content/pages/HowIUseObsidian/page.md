# How I use obsidian
***
## What is obsidian? 
Obsidian is a markdown note taking app that is heavily customisable and and be used for almost any type of notes.

<img src="https://0x4248.dev/Blog/content/img/Vault demo.png">

## Why do I use it?
I use obsidian to organise my ideas, projects and knowledge. Obsidian uses a note linking system that allows you to link other notes using links and tags which makes a graph of your notes which can be helpful in organising notes.

## Vault download
If you want to download the base configuration for my vault you can do so [here](https://github.com/0x4248/My_obsidian_vault_template)
## Vault configuration
My vault is configured in a way that makes it easy to navigate between the different parts of my life and to make it quick and easy to format pages with just a few taps.

### Extensions
Firstly lets talk about what extensions i'm using. Im currently using the following:

- Home tab
- Kanban
- Excalidraw
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
#### Excalidraw
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
- 04 Resources
- 05 Projects
- 06 Archive
- 07 Literature
- 08 Meta
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
- Rockets
- Aviation

In your vault you can have any thing:

- Cooking
- Gardening
- Writing
- Movies
- Books
- Art
#### Daily
In here I have notes that are daily notes that I write to keep track of what I have done that day and things I have read or watched.

I use template to autofill things like the date and basic structure of the page.
#### Fleeting
Fleeting notes are notes that are quick notes that I write down to remember things or ideas that I have and want to quickly write down.
#### Resources
Resources is where I keep things like quick tips, cheetsheets and other things that can be quickly used as reference or to help me remember things. Lets say I keep forgetting a bash. So I would look it up and write it down in a note in the resources folder. That way I can quickly look it up in my own notes.
#### Projects
Projects is where all my projects are kept. Each project has its own folder with notes on the project and its progress.
#### Archive
Here is where old notes that are no longer needed are placed but might come in use at a future date. Lets say its a old project for example.
#### Literature
Here is where you put in things you didn't write yourself but use it as reference. Sort of like a reading list.
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
- `audiowide-font`
- `lexend-font`
- `roboto-font`
- `roboto-mono-font`
- `orbitron-font`
- `lato-font`
- `tiny5-font`
- `sriracha-font`
- `kode-headings`
- `sriracha-headings`
- `bai-headings`
- `audiowide-headings`
- `lexend-headings`
- `roboto-headings`
- `roboto-mono-headings`
- `orbitron-headings`
- `lato-headings`
#### Fonts
The main font in the vault is Jetbrains Mono with neardfonts. Here are all the fonts I use.

- GohuFont uni11 Nerd Font Mono
- Perfect DOS VGA 437
- Bai Jamjuree
- Kode Mono
- Sriracha
- Audiowide
- Lexend
- Roboto
- Roboto mono
- Orbitron
- Lato
- Kode

#### Page colours
I colour my pages to help give my notes more life and to help separate parts of my notes 

<img src="https://0x4248.dev/Blog/content/img/Page colours 1.png">

<img src="https://0x4248.dev/Blog/content/img/Page colours 2.png">

Again this is part of my vault base template and CSS snippets.

## Inspiration 
I took heavy inspiration from Cyan Voxel's video that he made.
<iframe width="560" height="315" src="https://www.youtube.com/embed/rAkerV8rlow?si=DvOwOc4M_ALg87Le" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I also used his [obsidian vault template](https://github.com/CyanVoxel/Obsidian-Vault-Template) as a reference.

Again you want to download my vault template you can do so [here](https://github.com/0x4248/My_obsidian_vault_template)

```
git clone https://github.com/0x4248/My_obsidian_vault_template
```

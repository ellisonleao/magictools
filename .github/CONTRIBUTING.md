Thanks for your interest on contributing to this repo
=====================================================

## Before you start

To keep things simple and organized, we need to keep some basic rules when adding new links:

- Make sure the link you are adding is not already added
- Make sure the link is relevant to this repo. (We are focusing on game development here)
- Be nice, be cool, and we will always :heart: you!

:)

## How to add a new link to a topic?

- Fork this repo
- Create a new branch
- Add your link to the relevant section in `contents/<section>/<topic>.json`
  - Format:
    ```json
    {
      "pricing": "Open | Free | Freemium | Paid",
      "name": "Tool Name",
      "link": "https://toolwebsite.com",
      "description": "A short description of the tool and why it is useful"
    }
    ```
- Make a PR to the `main` branch

## How to create a new topic?

- Fork this repo
- Create a new branch
- Create a new JSON file in the relevant section folder inside `contents/<section>/`
  - Name the file as `<topic>.json`
    - use hyphens `-` for spaces
    - use underscores `_` for slashes
  - Add `<topic>` to the `index.json` (`contents/<section>/index.json`) file of the relevant section
  - Format:
    ```json
    {
      "name": "Topic Name",
      "description": "A short description of the topic",
      "contents": [
        {
          "pricing": "Open | Free | Freemium | Paid",
          "name": "Tool Name",
          "link": "https://toolwebsite.com",
          "description": "A short description of the tool and why it is useful"
        }
      ]
    }
    ```
- Make a PR to the `main` branch

## How to create a new section?

- Fork this repo
- Create a new branch
- Create a new folder inside `contents/` named `<section>`
  - use hyphens `-` for spaces
  - use underscores `_` for slashes
- Create an `index.json` file inside the newly created folder
  - Format:
    ```json
    {
      "name": "Section Name",
      "contents": [
        "topic-1",
        "topic-2"
      ]
    }
    ```
- Make sure to add all the topics you want in this section to the `index.json`
- Make a PR to the `main` branch


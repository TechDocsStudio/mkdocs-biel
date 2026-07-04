# AI chatbot plugin for MkDocs

Ask AI chatbot plugin for MkDocs sites, powered by [Biel.ai](https://biel.ai).

![AI chatbot MkDocs](https://docs.biel.ai/assets/images/biel-widget-docs-bd28548cf26a37bcb7c496487280bbfe.png)

Add an AI chatbot to your MkDocs documentation using Biel.ai's plugin. The integration works with any MkDocs theme, including Material for MkDocs, and adds both chat and search capabilities. No template overrides needed.

*Note: A Biel.ai plan is required to use this plugin. Try it free for 14 days—no credit card required.*

## Key features

- AI chatbot that provides instant responses to documentation queries.
- AI search engine for quick and relevant information retrieval.
- Integration with MkDocs, no `custom_dir` or template overrides required.
- Customizable to match your site's branding and user needs.

## Installation

```bash
pip install mkdocs-biel
```

Add the plugin to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - biel:
      project: <YOUR_PROJECT_ID>
      header_title: Biel.ai chatbot
```

Replace `<YOUR_PROJECT_ID>` with your project's ID from the [Biel.ai dashboard](https://app.biel.ai).

Run `mkdocs serve` and verify the chat button appears in the bottom-right corner.

## Configuration

All widget options are supported as snake_case keys, for example:

```yaml
plugins:
  - biel:
      project: <YOUR_PROJECT_ID>
      button_text: Ask AI
      button_position: bottom-right
      modal_position: bottom-right
      button_style: dark
      header_title: Documentation AI
```

Set `enable: false` to turn the widget off without removing the configuration.

## Get started

See the [MkDocs AI chatbot integration guide](https://docs.biel.ai/installation/mkdocs) for the full list of options and setup instructions.

## Support

Need assistance? [Contact us](https://docs.biel.ai/support) for help.

## License

Copyright (c) 2024 Biel.ai

Licensed under the [MIT License](LICENSE).

# AI assistant plugin for MkDocs

AI assistant plugin for MkDocs sites, with an **Ask AI** button powered by [Biel.ai](https://biel.ai).

![AI assistant MkDocs](https://docs.biel.ai/assets/images/biel-widget-docs-bd28548cf26a37bcb7c496487280bbfe.png)

Add an AI assistant to your MkDocs documentation using Biel.ai's plugin. The integration works with any MkDocs theme, including Material for MkDocs, and embeds the Ask AI button. Configure the documentation search widget separately. No template overrides needed.

*Note: A Biel.ai plan is required to use this plugin. Try it free for 14 days—no credit card required.*

## Key features

- **Ask AI** button that opens an AI assistant to answer questions from your documentation.
- **Documentation search** to find matching pages from indexed docs with a separately configured search widget.
- Connect menu to link the same indexed docs to Claude Code, Codex, and other compatible AI clients via [Biel.ai's hosted MCP server](https://docs.biel.ai/integrations/mcp-server).
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

### Theme keyboard shortcuts

Some themes, including Material for MkDocs, register global keyboard shortcuts (`f`, `s`, `/`, `p`, `n`) that fire while typing inside the Biel.ai widget. The plugin fixes this automatically: keystrokes inside the widget are scoped to it, and theme shortcuts keep working everywhere else on the page. Set `theme_shortcuts_fix: false` to opt out.

## Get started

See the [MkDocs AI assistant integration guide](https://docs.biel.ai/installation/mkdocs) for the full list of options and setup instructions.

## Support

Need assistance? [Contact us](https://docs.biel.ai/support) for help.

## License

Copyright (c) 2024 Biel.ai

Licensed under the [MIT License](LICENSE).

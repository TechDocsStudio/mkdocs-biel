"""
Ask AI chatbot plugin for MkDocs.

(c) 2024 - present Biel.ai
This code is licensed under MIT license (see LICENSE for details).
"""

import logging
from html import escape

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

log = logging.getLogger("mkdocs.plugins.biel")

DEFAULT_OPTIONS = {
    "enable": True,
    "version": "latest",
    "theme_shortcuts_fix": True,
    # biel-button
    "project": None,
    "button_position": "bottom-right",
    "button_text": "Ask AI",
    "button_style": "dark",
    "custom_font": None,
    "hide_icon": None,
    "ai_icon": None,
    "hide_avatars": None,
    "api_key": None,
    "metadata": None,
    # biel-bot
    "disable_input": None,
    "email": None,
    "expand_modal": None,
    "hide_close_button": None,
    "hide_connect_button": None,
    "hide_expand_button": None,
    "hide_refresh_button": None,
    "hide_settings_button": None,
    "hide_sources": None,
    "hide_feedback": None,
    "hide_think_mode_button": None,
    "hide_tooltips": None,
    "initial_messages": None,
    "keep_conversation": None,
    "modal_position": "bottom-right",
    "show_terms_modal": None,
    "think_mode_enabled": None,
    # biel-bot text
    "assistant_label": None,
    "close_button_text": None,
    "collapse_button_text": None,
    "connect_button_text": None,
    "error_message_4_0_3": None,
    "error_message_4_0_4": None,
    "error_message_default": None,
    "expand_button_text": None,
    "footer_text": None,
    "header_title": "Biel.ai chatbot",
    "input_placeholder_text": None,
    "mcp_claude_copied_description": None,
    "mcp_claude_description": None,
    "mcp_claude_text": None,
    "mcp_copied_text": None,
    "mcp_copilot_description": None,
    "mcp_copilot_text": None,
    "mcp_cursor_description": None,
    "mcp_cursor_text": None,
    "mcp_server_url": None,
    "mcp_url_copied_description": None,
    "mcp_url_description": None,
    "mcp_url_text": None,
    "refresh_button_text": None,
    "send_button_text": None,
    "settings_button_text": None,
    "sources_text": None,
    "suggested_questions": None,
    "suggested_questions_title": None,
    "terms_checkbox_text": None,
    "terms_description": None,
    "terms_title": None,
    "think_mode_auto_description": None,
    "think_mode_auto_text": None,
    "think_mode_button_text": None,
    "think_mode_fast_description": None,
    "think_mode_fast_text": None,
    "think_mode_think_description": None,
    "think_mode_think_text": None,
    "welcome_message": None,
}

# Options that configure the plugin itself rather than the <biel-button> element.
NON_ATTRIBUTE_OPTIONS = ("enable", "version", "button_text", "theme_shortcuts_fix")

# Themes like Material for MkDocs register global keyboard shortcuts (f, s, /,
# p, n) that fire while the user types inside Biel's shadow DOM, because the
# retargeted event doesn't look editable to the theme. Stop propagation at the
# document only for keystrokes originating inside a Biel component, so theme
# shortcuts keep working everywhere else.
THEME_SHORTCUTS_FIX = """\
<script>
document.addEventListener('keydown', function (e) {
  var path = e.composedPath ? e.composedPath() : [];
  for (var i = 0; i < path.length; i++) {
    var tag = path[i].tagName;
    if (tag && tag.toLowerCase().indexOf('biel-') === 0) {
      e.stopPropagation();
      return;
    }
  }
});
</script>
"""


def _snake_to_kebab(string):
    return string.replace("_", "-")


def _build_config_scheme():
    scheme = []
    for key, default in DEFAULT_OPTIONS.items():
        if isinstance(default, bool):
            scheme.append((key, config_options.Type(bool, default=default)))
        elif default is not None:
            scheme.append((key, config_options.Type(str, default=default)))
        else:
            scheme.append(
                (key, config_options.Optional(config_options.Type((str, bool, int))))
            )
    return tuple(scheme)


class BielPlugin(BasePlugin):
    config_scheme = _build_config_scheme()

    def on_config(self, config):
        if self.config.get("enable") and not self.config.get("project"):
            log.warning(
                "biel: no 'project' set. Add your project ID from the "
                "Biel.ai dashboard to mkdocs.yml."
            )
        return config

    def on_post_page(self, output, page, config):
        if not self.config.get("enable"):
            return output

        version = self.config.get("version") or "latest"
        head_tags = (
            f'<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/'
            f'biel-search@{version}/dist/biel-search/biel-search.css">\n'
            f'<script type="module" src="https://cdn.jsdelivr.net/npm/'
            f'biel-search@{version}/dist/biel-search/biel-search.esm.js"></script>\n'
        )

        attributes = []
        for key in DEFAULT_OPTIONS:
            if key in NON_ATTRIBUTE_OPTIONS:
                continue
            value = self.config.get(key)
            if value is None:
                continue
            if isinstance(value, bool):
                value = "true" if value else "false"
            attributes.append(
                f'{_snake_to_kebab(key)}="{escape(str(value), quote=True)}"'
            )

        button_text = escape(str(self.config.get("button_text") or "Ask AI"))
        button = f'<biel-button {" ".join(attributes)}>{button_text}</biel-button>\n'
        if self.config.get("theme_shortcuts_fix"):
            button += THEME_SHORTCUTS_FIX

        if "</head>" in output:
            output = output.replace("</head>", head_tags + "</head>", 1)
        else:
            output = head_tags + output

        if "</body>" in output:
            output = output.replace("</body>", button + "</body>", 1)
        else:
            output += button

        return output

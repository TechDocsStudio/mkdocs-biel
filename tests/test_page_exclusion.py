import unittest
from types import SimpleNamespace

from mkdocs_biel.plugin import BielPlugin


class PageExclusionTests(unittest.TestCase):
    def setUp(self):
        self.plugin = BielPlugin()
        errors, _ = self.plugin.load_config({"project": "example-project"})
        self.assertEqual(errors, [])
        self.html = "<html><head></head><body>Page content</body></html>"

    def render(self, metadata):
        return self.plugin.on_post_page(
            self.html, SimpleNamespace(meta=metadata), {}
        )

    def test_excluded_page_is_returned_without_injection(self):
        self.assertEqual(self.render({"exclude-biel": True}), self.html)

    def test_only_boolean_true_excludes_the_page(self):
        for value in (False, None, "true", "false", 1):
            with self.subTest(value=value):
                self.assertIn("<biel-button ", self.render({"exclude-biel": value}))

    def test_exclusion_does_not_affect_following_pages(self):
        expected = self.render({})
        self.render({"exclude-biel": True})
        self.assertEqual(self.render({}), expected)
        for content in (
            "biel-search.css",
            "biel-search.esm.js",
            '<biel-button project="example-project"',
            "document.addEventListener('keydown'",
        ):
            self.assertIn(content, expected)

    def test_global_disable_applies_to_every_page(self):
        self.plugin.config["enable"] = False
        self.assertEqual(self.render({}), self.html)
        self.assertEqual(self.render({"exclude-biel": False}), self.html)


if __name__ == "__main__":
    unittest.main()

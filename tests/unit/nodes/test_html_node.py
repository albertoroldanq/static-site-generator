import unittest

from src.nodes.html_node import HTMLNode
from tests.TestCase import TestCase


class TestTextNode(TestCase):
    def test_repr(self):
        node = HTMLNode("h1", "This is an h1", None, None)
        self.assertEqual(repr(node), "HTMLNode(h1, This is an h1, None, None)")


    def test_props_to_html(self):
        props1 = {
            "href": "https://www.google.com",
            "target": "_blank"
        }

        props2 = {
            "class": "thumbnail-wrapper",
            "width": "auto"
        }

        node = HTMLNode("a", "click here", None, props1)
        node2 = HTMLNode("div", None, None, props2)

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(node2.props_to_html(), ' class="thumbnail-wrapper" width="auto"')

    def test_to_html(self):
        node = HTMLNode("a", "click here", None, None)
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
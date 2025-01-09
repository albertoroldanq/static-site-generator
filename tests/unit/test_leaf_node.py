import unittest

from src.nodes.leaf_node import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        props1 = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = LeafNode("a", "click here", props1)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">click here</a>')

    def test_to_html_no_value(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        node = LeafNode(None, "click here")
        self.assertEqual(node.to_html(), "click here")

if __name__ == "__main__":
    unittest.main()
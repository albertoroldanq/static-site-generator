import unittest

from src.nodes import TextNode, TextType
from src.transformations.text_to_html import text_node_to_html_node
from tests.TestCase import TestCase


class TestTextToHtml(TestCase):

    def test_no_text_type_match(self):
        text_node = TextNode("Bold text", "incompatible type")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)


    def test_text_node_to_html_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)

        node = text_node_to_html_node(text_node)

        self.assertEqual(node.tag, 'b')
        self.assertEqual(node.value, 'Bold text')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_text_node_to_html_text(self):
        text_node = TextNode("Normal text", TextType.TEXT)

        node = text_node_to_html_node(text_node)

        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, 'Normal text')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_text_node_to_html_link(self):
        text_node = TextNode("Link text", TextType.LINK, 'https://test.com')

        node = text_node_to_html_node(text_node)

        self.assertEqual(node.tag, 'a')
        self.assertEqual(node.value, 'Link text')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {'href': 'https://test.com'})

    def test_text_node_to_html_image(self):
        text_node = TextNode("Image alt text", TextType.IMAGE, 'https://test.com')

        node = text_node_to_html_node(text_node)

        self.assertEqual(node.tag, 'img')
        self.assertEqual(node.value, '')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {'src': 'https://test.com', 'alt': 'Image alt text'})

if __name__ == "__main__":
    unittest.main()
import unittest

from src.nodes import TextNode, TextType
from src.transformations.split_nodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):

    def test_invalid_markdown_text(self):
        node = TextNode("Hello **bold text World invalid", TextType.TEXT)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], '**', TextType.BOLD)

    def test_no_markdown_text(self):
        node = TextNode("Hello World", TextType.TEXT)

        self.assertEqual('Hello World', node.text)
        self.assertEqual(TextType.TEXT, node.text_type)


    def test_correct_markdown_in_text(self):
        node = TextNode("Hello **bold text** World", TextType.TEXT)

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" World", TextType.TEXT),
        ]

        self.assertEqual(expected, split_nodes_delimiter([node], '**', TextType.BOLD))

    def test_ignore_other_markdown_delimiters(self):

        node = TextNode("Hello *italic text* World. This is my website: **albertoroldanq.com**", TextType.TEXT)

        expected = [
            # The italic markdown remains untouched
            TextNode("Hello *italic text* World. This is my website: ", TextType.TEXT),
            TextNode("albertoroldanq.com", TextType.BOLD),
        ]

        self.assertEqual(expected, split_nodes_delimiter([node], '**', TextType.BOLD))

    def test_two_markdown_elements_only_splits_first(self):
        node = TextNode("Hello *italic text* World. This is my website: *albertoroldanq.com*", TextType.TEXT)

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" World. This is my website: ", TextType.TEXT),
            TextNode("albertoroldanq.com", TextType.ITALIC),

        ]

        self.assertEqual(expected, split_nodes_delimiter([node], '*', TextType.ITALIC))


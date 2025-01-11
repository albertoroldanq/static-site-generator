import unittest

from src.nodes import TextNode, TextType
from src.transformations.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


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

    def test_split_nodes_image(self):

        text1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        text2 = "![image2](https://i.imgur.com/aKaOqIh.gif)"
        text3 = "![image3](https://i.imgur.com/aKaOqIh.gif) and ![img3](https://i.imgur.com/fJRm4Vk.jpeg)"
        node1 = TextNode(text1, TextType.TEXT)
        node2 = TextNode(text2, TextType.TEXT)
        node3 = TextNode(text3, TextType.TEXT)
        old_nodes = [node1, node2, node3]
        expected_results = [
            TextNode("This is text with a " , TextType.TEXT, None),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode( " and " , TextType.TEXT, None),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("image2", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode("image3", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode( " and " , TextType.TEXT, None),
            TextNode("img3", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]

        result = split_nodes_image(old_nodes)

        self.assertEqual(expected_results, result)


    def test_split_nodes_links(self):

        text1 = "This is text with a [github link](https://github.com/albertoroldanq) and [portfolio link](https://albertoroldanq.com)"
        text2 = "[link2](https://test.com/2)"
        text3 = "[link3](https://test.com/3/1) and [another link](https://test.com/3/2)"
        node1 = TextNode(text1, TextType.TEXT)
        node2 = TextNode(text2, TextType.TEXT)
        node3 = TextNode(text3, TextType.TEXT)
        old_nodes = [node1, node2, node3]
        expected_results = [
            TextNode("This is text with a " , TextType.TEXT, None),
            TextNode("github link", TextType.LINK, "https://github.com/albertoroldanq"),
            TextNode( " and " , TextType.TEXT, None),
            TextNode("portfolio link", TextType.LINK, "https://albertoroldanq.com"),
            TextNode("link2", TextType.LINK, "https://test.com/2"),
            TextNode("link3", TextType.LINK, "https://test.com/3/1"),
            TextNode( " and " , TextType.TEXT, None),
            TextNode("another link", TextType.LINK, "https://test.com/3/2")
        ]

        result = split_nodes_link(old_nodes)

        self.assertEqual(expected_results, result)




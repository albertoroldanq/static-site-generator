import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.albertoroldanq.com")
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node.url, node2.url)
        self.assertEqual(node.url, "https://www.albertoroldanq.com")
        self.assertEqual(node2.url, None)
        self.assertNotEqual(node.text_type, node2.text_type)

if __name__ == "__main__":
    unittest.main()
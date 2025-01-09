import unittest

from src.nodes.leaf_node import LeafNode
from src.nodes.parent_node import ParentNode


class TestTextNode(unittest.TestCase):
    def test_to_html_with_leaf_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],

            {"id": "paragraph", "class": "text"}
        )

        self.assertEqual(node.to_html(), '<p id="paragraph" class="text"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_with_parent_and_leaf_children(self):
        child_parent_node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        child_parent_node2 = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        parent_node = ParentNode(
            "section",
            [
                child_parent_node1,
                child_parent_node2,
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(parent_node.to_html(), '<section><p><b>Bold text</b><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><div><b>Bold text</b><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>Normal text</section>')


    def test_to_html_parentnodechildren_with_parentnodechildren(self):

        sub_child_parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "I am a leafnode"),
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],

            {"class": "subchild", "id": "subchild"}
        )

        child_parent_node1 = ParentNode(
            "div",
            [
                sub_child_parent_node,
                sub_child_parent_node
            ],
        )

        child_parent_node2 = ParentNode(
            "article",
            [
                sub_child_parent_node,
                sub_child_parent_node,
                sub_child_parent_node
            ],
        )

        parent_node = ParentNode(
            "div",
            [
                child_parent_node1,
                child_parent_node2,
            ],
        )

        self.assertEqual(parent_node.to_html(), '<div><div><p class="subchild" id="subchild"><b>I am a leafnode</b><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p class="subchild" id="subchild"><b>I am a leafnode</b><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div><article><p class="subchild" id="subchild"><b>I am a leafnode</b><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p class="subchild" id="subchild"><b>I am a leafnode</b><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p class="subchild" id="subchild"><b>I am a leafnode</b><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></article></div>')


    def test_to_html_no_tag(self):
        node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()



if __name__ == "__main__":
    unittest.main()
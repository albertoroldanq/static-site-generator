import unittest

from src.nodes import HTMLNode, ParentNode
from src.transformations.markdown_to_html_node import markdown_to_html_node
from tests.TestCase import TestCase
from tests.unit.transformations.markdown_to_html_node_test_data import unordered_list_data, ordered_list_data, \
    quote_data, code_data, heading1_data, heading2_data, heading6_data, paragraph_data


class TestMarkdownToHtmlNode(TestCase):

    def test_markdown_to_html_node_invalid_format(self):
        invalid_markdown = "# Heading with wrong **bold text"

        exception_message = "Invalid markdown format"

        with self.assertRaises(Exception) as context:
            markdown_to_html_node(invalid_markdown)
            self.assertIn("Invalid markdown detected", str(context.exception))
        self.assertEqual(exception_message, str(context.exception))

    def test_markdown_ordered_list_to_html_node(self):
        markdown_ordered_list = ("1. This is the first list item in a list block with a [link](https://test.com)\n"
                                 "2. This is a list item\n"
                                 "3. This is another list item\n")

        expected = HTMLNode(
            "div",
            None,
            [ordered_list_data()],
            None
        )

        result = markdown_to_html_node(markdown_ordered_list)

        self.assertEqual(expected, result)

    def test_markdown_unordered_list_to_html_node(self):
        markdown_unordered_list1 = ("* This is the first list item in a list block with a [link](https://test.com)\n"
                                   "* This is a list item\n"
                                   "* This is another list item\n")

        markdown_unordered_list2 = ("- This is the first list item in a list block with a [link](https://test.com)\n"
                                   "- This is a list item\n"
                                   "- This is another list item\n")
        expected_result_1 = HTMLNode(
            "div",
            None,
            [unordered_list_data()],
            None
        )
        result1 = markdown_to_html_node(markdown_unordered_list1)

        expected_result_2 = HTMLNode(
            "div",
            None,
            [unordered_list_data()],
            None
        )
        result2 = markdown_to_html_node(markdown_unordered_list2)

        self.assertEqual(expected_result_1, result1)
        self.assertEqual(expected_result_2, result2)

    def test_markdown_quote_to_html_node(self):
        markdown_quote = ">This is a quote with a [link](https://test.com)\n"

        expected = HTMLNode(
            "div",
            None,
            [quote_data()],
            None
        )

        result = markdown_to_html_node(markdown_quote)

        self.assertEqual(expected, result)

    def test_markdown_code_to_html_node(self):
        markdown_code = "```This is a paragraph with a [link](https://test.com)```\n"

        expected = HTMLNode(
            "div",
            None,
            [code_data()],
            None
        )

        result = markdown_to_html_node(markdown_code)

        self.assertEqual(expected, result)

    def test_markdown_heading_to_html_node(self):
        markdown_heading = "# This is a heading h1 with **bold text**    \n"
        expected = HTMLNode(
            "div",
            None,
            [heading1_data()],
            None
        )
        result = markdown_to_html_node(markdown_heading)

        self.assertEqual(expected, result)

    def test_markdown_document_to_html_node(self):
        markdown_heading1 = "# This is a heading h1 with **bold text**    \n"
        markdown_heading2 = "## This is a heading h2 with **bold text**    \n"
        markdown_heading6 = "###### This is a heading h6 with **bold text**    \n"
        markdown_paragraph = "This is a paragraph...\n"
        markdown_ordered_list = ("1. This is the first list item in a list block with a [link](https://test.com)\n"
                                 "2. This is a list item\n"
                                 "3. This is another list item\n")
        markdown_unordered_list = ("* This is the first list item in a list block with a [link](https://test.com)\n"
                                   "* This is a list item\n"
                                   "* This is another list item\n")
        markdown_code = "```This is a paragraph with a [link](https://test.com)```\n"
        markdown_quote = ">This is a quote with a [link](https://test.com)\n"

        markdown_document = (
                markdown_heading1 + "\n"
                + markdown_quote + "\n"
                + markdown_heading2 + "\n"
                + markdown_ordered_list + "\n"
                + markdown_code + "\n"
                + markdown_heading6 + "\n"
                + markdown_paragraph + "\n"
                + markdown_unordered_list
        )

        expected = HTMLNode(
            "div",
            None,
            [
                heading1_data(),
                quote_data(),
                heading2_data(),
                ordered_list_data(),
                code_data(),
                heading6_data(),
                paragraph_data(),
                unordered_list_data()
            ],
            None
        )
        result = markdown_to_html_node(markdown_document)

        self.assertEqual(expected, result)

import unittest

from src.transformations.markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from tests.TestCase import TestCase

class TestMarkdownToBlocks(TestCase):

    def test_markdown_to_blocks(self):
        heading = "# This is a heading   \n"
        paragraph = "   This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
        list_block = ("* This is the first list item in a list block\n"
                      "* This is a list item\n"
                      "* This is another list item\n")
        empty_text = ""
        markdown = heading + "\n" + paragraph + "\n" + list_block + "\n" + empty_text + "\n" + "\n"

        expected = [heading.strip(), paragraph.strip(), list_block.strip()]

        result = markdown_to_blocks(markdown)
        self.assertEqual(expected, result)

    def test_block_to_block_heading_type(self):
        heading = "# This is a heading"
        paragraph = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        unordered_list1 = ("* This is the first list item in a list block\n"
                           "* This is a list item\n"
                           "* This is another list item")
        unordered_list2 = ("- This is the first list item in a list block\n"
                           "- This is a list item\n"
                           "- This is another list item")
        ordered_list = ("1. This is the first list item in a list block\n"
                        "2. This is a list item\n"
                        "3. This is another list item")

        quote = (">This is the first line of a quote\n"
                 ">This is a quote line\n"
                 ">This is another quote line")

        code = "```This is a code block. It has some inside of it.```"

        blocks_to_types = {
            paragraph: BlockType.PARAGRAPH,
            heading: BlockType.HEADING,
            code: BlockType.CODE,
            quote: BlockType.QUOTE,
            unordered_list1: BlockType.UNORDERED_LIST,
            unordered_list2: BlockType.UNORDERED_LIST,
            ordered_list: BlockType.ORDERED_LIST,
        }

        for block in blocks_to_types:
            result = block_to_block_type(block)
            self.assertEqual(blocks_to_types[block], result)


    def test_block_to_block_malformed_defaults_to_paragraph(self):
        heading = "####### This is not a heading"
        paragraph = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        unordered_list1 = ("*This is not the first list item in a list block\n"
                           "* This is a list item\n"
                           "* This is another list item")
        unordered_list2 = ("- This is the first list item in a list block\n"
                           "-This is not a list item\n"
                           "- This is another list item")
        ordered_list = ("1. This is the first list item in a list block\n"
                        "3. This is not a list item\n"
                        "4. This is another list item")

        quote = (">This is the first line of a quote\n"
                 "This is not a quote line\n"
                 ">This is another quote line")

        code = "``This is not a code block. It has some inside of it.```"

        blocks_to_types = {
            paragraph: BlockType.PARAGRAPH,
            heading: BlockType.HEADING,
            code: BlockType.CODE,
            quote: BlockType.QUOTE,
            unordered_list1: BlockType.UNORDERED_LIST,
            unordered_list2: BlockType.UNORDERED_LIST,
            ordered_list: BlockType.ORDERED_LIST,
        }

        for block in blocks_to_types:
            result = block_to_block_type(block)
            self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()

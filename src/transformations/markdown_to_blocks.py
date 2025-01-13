from enum import Enum
from functools import reduce


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return list(filter(__block_is_not_empty, map(__remove_trailing_whitespace, blocks)))


def block_to_block_type(block):
    if __is_heading_type(block):
        return BlockType.HEADING
    if __is_code_type(block):
        return BlockType.CODE
    if __is_quote_type(block):
        return BlockType.QUOTE
    if __is_unordered_list_type(block):
        return BlockType.UNORDERED_LIST
    if __is_ordered_list_type(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def __block_is_not_empty(block):
    return block != ""

def __remove_trailing_whitespace(block):
   return block.strip()


def __is_heading_type(block):
    if block.startswith('#'):
        markdown = block.split(" ", 1)[0]
        count_hashes = reduce(lambda count, char: count + 1 if char == '#' else count, markdown, 0)
        return 1 <= count_hashes <= 6
    return False

def __is_code_type(block):
    if len(block) < 6:
        return False
    code_md = "```"
    return block[:3] == code_md and block[-3:] == code_md

def __is_quote_type(block):
    quote_md = ">"
    if not block.startswith(quote_md):
        return False
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(quote_md):
            return False
    return True

def __is_unordered_list_type(block):
    uo_list_md1 = "* "
    uo_list_md2 = "- "
    if not (block.startswith(uo_list_md1) or block.startswith(uo_list_md2)):
        return False

    lines = block.split("\n")
    for line in lines:
        if not (line.startswith(uo_list_md1) or line.startswith(uo_list_md2)):
            return False
    return True

def __is_ordered_list_type(block):
    item_number = 1
    for line in block.split("\n"):
        if not line.startswith(f"{item_number}. "):
            return False
        item_number += 1
    return True
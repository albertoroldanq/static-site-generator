import logging

from src.logger.logger import error
from src.nodes import HTMLNode, ParentNode
from src.transformations.markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.transformations.text_to_html import text_node_to_html_node
from src.transformations.text_to_text_nodes import text_to_text_nodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        html_blocks.append(__markdown_block_to_html(block))

    return HTMLNode('div', None, html_blocks)


def __markdown_block_to_html(block):
    block_type = block_to_block_type(block)
    try:
        match block_type:
            case BlockType.HEADING:
                return __markdown_heading_to_html(block)
            case BlockType.PARAGRAPH:
                return __markdown_paragraph_to_html(block)
            case BlockType.CODE:
                return __markdown_code_to_html(block)
            case BlockType.QUOTE:
                return __markdown_quote_to_html(block)
            case BlockType.UNORDERED_LIST:
                return __markdown_list_to_html(block, 'ul')
            case BlockType.ORDERED_LIST:
                return __markdown_list_to_html(block, 'ol')
            case _:
                return HTMLNode(None, block)
    except ValueError as e:
        error(f"Invalid markdown format. Exception: {str(e)}")
        raise ValueError('Invalid markdown format')


def __markdown_heading_to_html(block):
    text = block.split(" ", 1)
    count_hashes = len(text[0])
    tag = f"h{count_hashes}"

    children = __text_to_children_nodes(text[1])

    return ParentNode(tag, children)


def __markdown_paragraph_to_html(text):
    children = __text_to_children_nodes(text)
    return ParentNode("p", children)

def __markdown_code_to_html(block):
    text = block[3:-3].strip()

    children = __text_to_children_nodes(text)

    return ParentNode('code', children)

def __markdown_quote_to_html(block):
    text = __remove_initial_markdown_character(block)
    children = __text_to_children_nodes(text)

    return ParentNode('quote', children)

def __markdown_list_to_html(block, list_type):
    text = __remove_list_markdown(block)
    children = __text_to_list_items(text)

    return ParentNode(list_type, children)

def __text_to_children_nodes(text):
    text_nodes = text_to_text_nodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def __remove_initial_markdown_character(block):
    new_lines = []
    lines = block.split("\n")
    for line in lines:
        new_lines.append(line[1:].strip())

    return "\n".join(new_lines)

def __remove_list_markdown(block):
    new_lines = []
    lines = block.split("\n")
    for line in lines:
        new_lines.append(line.split(" ", 1)[1].strip())

    return "\n".join(new_lines)

def __text_to_list_items(text):
    lines = text.split("\n")
    children = []
    for line in lines:
        sub_children = __text_to_children_nodes(line)
        children.append(ParentNode('li', sub_children))

    return children


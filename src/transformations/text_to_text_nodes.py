import logging

from src.logger import logger
from src.logger.logger import error
from src.nodes import TextNode, TextType
from src.transformations.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_text_nodes(text):

    text = text.strip()
    nodes = [TextNode(text, TextType.TEXT)]
    text_delimiters = {
        TextType.BOLD: '**',
        TextType.ITALIC: '*',
        TextType.CODE: '`'
    }

    non_text_delimiters = {
        TextType.IMAGE: split_nodes_image,
        TextType.LINK: split_nodes_link,
    }

    processed_delimiter_nodes = nodes
    try:
        for text_type in text_delimiters:
            processed_delimiter_nodes = split_nodes_delimiter(processed_delimiter_nodes, text_delimiters[text_type], text_type)

        processed_nodes = processed_delimiter_nodes
        for text_type in non_text_delimiters:
            processed_nodes = non_text_delimiters[text_type](processed_nodes)
    except ValueError as e:
        error(f"[{__name__}] {str(e)}" )
        raise ValueError(f"[ERROR processing text in {__name__}] {str(e)}")

    return processed_nodes
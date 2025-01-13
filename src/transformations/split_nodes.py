from src.nodes import TextNode, TextType
from src.transformations.extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if not (node.text_type == TextType.TEXT):
            new_nodes.append(node)
            continue
        text = node.text
        while delimiter in text:
            start_index = text.find(delimiter)
            end_index = text.find(delimiter, start_index + len(delimiter))

            if end_index == -1:
                raise ValueError(
                    f"Invalid Markdown syntax: Unmatched delimiter '{delimiter}' found in input text: {text}"
                )

            before_text = text[:start_index]
            inside_text = text[start_index + len(delimiter):end_index]
            after_text = text[end_index + len(delimiter):]

            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            new_nodes.append(TextNode(inside_text, text_type))

            text = after_text

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_image(old_nodes):
    return __split_non_text_nodes(old_nodes, extract_markdown_images, TextType.IMAGE)


def split_nodes_link(old_nodes):
    return __split_non_text_nodes(old_nodes, extract_markdown_links, TextType.LINK)


def __split_non_text_nodes(old_nodes, extract_md_elements_func, text_type):
    new_nodes = []
    for node in old_nodes:
        if not (node.text_type == TextType.TEXT):
            new_nodes.append(node)
            continue
        text = node.text
        for elem in extract_md_elements_func(text):
            delimiter = __get_delimiter_string(text_type, elem)
            sections = text.split(delimiter, 1)
            before_text = sections[0]
            after_text = sections[1]

            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            new_nodes.append(TextNode(elem[0], text_type, elem[1]))

            text = after_text

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def __get_delimiter_string(text_type, md_element):
    link_delimiter = f"[{md_element[0]}]({md_element[1]})"
    match text_type:
        case TextType.IMAGE:
            delimiter = "!" + link_delimiter
        case _:
            delimiter = link_delimiter

    return delimiter

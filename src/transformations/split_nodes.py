from src.nodes import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        while delimiter in text:
            start_index = text.find(delimiter)
            end_index = text.find(delimiter, start_index + len(delimiter))

            if end_index == -1:
                raise ValueError(
                    f"Invalid Markdown syntax: Unmatched delimiter '{delimiter}' found in input text."
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

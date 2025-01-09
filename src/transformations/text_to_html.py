from src.nodes.text_node import TextNode, TextType
from src.nodes.leaf_node import LeafNode

def text_node_to_html_node(text_node):
    text = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text)
        case TextType.BOLD:
            return LeafNode('b', text)
        case TextType.ITALIC:
            return LeafNode('i', text)
        case TextType.CODE:
            return LeafNode('code', text)
        case TextType.LINK:
            return LeafNode('a', text, {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', '', {'src': text_node.url, 'alt': text})
        case _:
            raise Exception('No TextType match found')
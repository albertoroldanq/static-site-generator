from src.config.log_config import setup_logger
from src.nodes.text_node import TextNode, TextType
from src.transformations.text_to_text_nodes import text_to_text_nodes

setup_logger()

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.albertoroldanq.com")
    print(text_node)
# try:
#     text_to_text_nodes(" **bold*")
# except ValueError as e:
#     print(str(e))


if __name__ == "__main__":
    main()
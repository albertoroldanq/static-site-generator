import os.path

from config.config import STATIC_DIR, PUBLIC_DIR
from config.log_config import setup_logger
from src.nodes.text_node import TextNode, TextType
from src.site_load.override_directory import override_directory


BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
setup_logger()

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.albertoroldanq.com")
    print(text_node)
    try:
        override_directory(STATIC_DIR, PUBLIC_DIR)
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
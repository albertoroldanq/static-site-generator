import os.path

from config.config import STATIC_DIR, PUBLIC_DIR, INDEX_HTML_PATH, INDEX_MD_PATH, TEMPLATE_HTML_PATH, CONTENT_DIR
from config.log_config import setup_logger
from src.nodes.text_node import TextNode, TextType
from src.site_load.generate_page import generate_pages_recursive
from src.site_load.override_directory import override_directory


BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
setup_logger()

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.albertoroldanq.com")
    print(text_node)
    try:
        override_directory(STATIC_DIR, PUBLIC_DIR)
        generate_pages_recursive(CONTENT_DIR, TEMPLATE_HTML_PATH, PUBLIC_DIR)
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
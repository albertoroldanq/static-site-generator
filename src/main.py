from textnode import TextNode, TextType


def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.albertoroldanq.com")
    print(text_node)

if __name__ == "__main__":
    main()
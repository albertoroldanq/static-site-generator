from src.nodes import TextNode, TextType

def expected_results():
    text1 = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://albertoroldanq.com)"
    text2 = "This is *text* with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://albertoroldanq.com)"
    text3 = "This is *text* with an **bold** word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://albertoroldanq.com)"
    text4 = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) This is *text* with an **bold** word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://albertoroldanq.com)"
    text5 = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
    text6 = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://albertoroldanq.com)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://albertoroldanq.com)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://albertoroldanq.com)"
    text7 = " `code block` `code block` `code block`"

    return {
        text1: [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://albertoroldanq.com"),
        ],

        text2: [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.ITALIC),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://albertoroldanq.com"),
        ],

        text3: [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.ITALIC),
            TextNode(" with an ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://albertoroldanq.com"),
        ],
        text4: [
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" This is ", TextType.TEXT),
            TextNode("text", TextType.ITALIC),
            TextNode(" with an ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://albertoroldanq.com"),
        ],
        text5: [
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ],
        text6: [
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link", TextType.LINK, "https://albertoroldanq.com"),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link", TextType.LINK, "https://albertoroldanq.com"),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("link", TextType.LINK, "https://albertoroldanq.com"),
        ],
        text7: [
            TextNode(" ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ],
    }
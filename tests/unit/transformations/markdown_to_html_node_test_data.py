from src.nodes import HTMLNode, ParentNode


def unordered_list_data():
    return ParentNode(
        'ul',
        [
            ParentNode(
                "li",
                [
                    HTMLNode(None, "This is the first list item in a list block with a ", None, None),
                    HTMLNode('a', "link", None, {'href': 'https://test.com'})],
                None
            ),
            ParentNode(
                "li",
                [HTMLNode(None, "This is a list item", None, None)],
                None
            ),
            ParentNode(
                "li",
                [HTMLNode(None, "This is another list item", None, None)],
                None
            ),
        ],
        None
    )


def ordered_list_data():
    return ParentNode(
        'ol',
        [
            ParentNode(
                "li",
                [
                    HTMLNode(None, "This is the first list item in a list block with a ", None, None),
                    HTMLNode('a', "link", None, {'href': 'https://test.com'})
                ],
                None
            ),
            ParentNode(
                "li",
                [HTMLNode(None, "This is a list item", None, None)],
                None
            ),
            ParentNode(
                "li",
                [HTMLNode(None, "This is another list item", None, None)],
                None
            ),
        ],
        None
    )


def quote_data():
    return ParentNode("quote",
                      [
                          HTMLNode(None, "This is a quote with a ", None, None),
                          HTMLNode("a", "link", None, {"href": "https://test.com"})
                      ],
                      None
                      )


def code_data():
    return ParentNode("code",
                      [
                          HTMLNode(None, "This is a paragraph with a ", None, None),
                          HTMLNode("a", "link", None, {"href": "https://test.com"})
                      ],
                      None
                      )


def heading1_data():
    return ParentNode("h1",
                      [
                          HTMLNode(None, "This is a heading h1 with ", None, None),
                          HTMLNode("b", "bold text", None, None)
                      ],
                      None
                      )
def heading2_data():
    return ParentNode("h2",
                      [
                          HTMLNode(None, "This is a heading h2 with ", None, None),
                          HTMLNode("b", "bold text", None, None)
                      ],
                      None
                      )
def heading6_data():
    return ParentNode("h6",
                      [
                          HTMLNode(None, "This is a heading h6 with ", None, None),
                          HTMLNode("b", "bold text", None, None)
                      ],
                      None
                      )

def paragraph_data():
    return ParentNode("p",
                      [
                          HTMLNode(None, "This is a paragraph...", None, None)
                      ],
                      None
                      )

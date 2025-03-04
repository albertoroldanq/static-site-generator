import unittest

from src.transformations.extract_markdown import extract_markdown_images, extract_markdown_links
from tests.TestCase import TestCase


class TestExtractMarkdown(TestCase):

    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_links(self):
        text = "This is text with a link [to albertoroldanq](https://www.albertoroldanq.com) and [to github](https://www.github.com/albertoroldanq)"
        self.assertEqual(extract_markdown_links(text), [("to albertoroldanq", "https://www.albertoroldanq.com"), ("to github", "https://www.github.com/albertoroldanq")])

if __name__ == "__main__":
    unittest.main()
import os.path
import unittest

from src.site_load.generate_page import extract_title
from tests.TestCase import TestCase


class TestGeneratePage(TestCase):

    def test_extract_title_from_valid_document(self):

        tests_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        test_data_dir = os.path.join(tests_dir, "test_data")
        md_file_path = os.path.join(test_data_dir, "valid_markdown.md")
        with open(md_file_path) as file:
            md_content = file.read()

        title = extract_title(md_content)

        self.assertEqual("Tolkien Fan Club", title)

    def test_extract_title_from_document_with_no_h1(self):
        tests_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        test_data_dir = os.path.join(tests_dir, "test_data")
        md_file_path = os.path.join(test_data_dir, "markdown_with_no_h1.md")
        with open(md_file_path) as file:
            md_content = file.read()

        with self.assertRaises(Exception) as context:
            extract_title(md_content)
        self.assertEqual("No h1 found in markdown document", str(context.exception))


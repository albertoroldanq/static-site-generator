import os.path
import tempfile
import unittest

from src.site_load.generate_page import extract_title, generate_page, generate_pages_recursive
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


    def test_generate_page(self):
        test_content = "# Random Title"
        test_template = "<html><title>{{ Title }}<title/><body>{{ Content }}</body></html>"

        with tempfile.TemporaryDirectory() as content_dir:
            index_md_path = os.path.join(content_dir, "index.md")
            with open(index_md_path, "w") as f:
                f.write(test_content)

            with tempfile.TemporaryDirectory() as template_dir:
                template_html_path = os.path.join(template_dir, "template.html")
                with open(template_html_path, "w") as f:
                    f.write(test_template)

                with tempfile.TemporaryDirectory() as output_dir:
                    index_html_path = os.path.join(output_dir, "index.html")
                    result = generate_page(index_md_path, template_html_path, index_html_path)

                    with open(index_html_path) as f:
                        html = f.read()
                        self.assertEqual("<html><title>Random Title<title/><body><div><h1>Random Title</h1></div></body></html>", html)


    def test_generate_pages_recursive(self):
        with tempfile.TemporaryDirectory() as content_dir:
            with tempfile.TemporaryDirectory() as output_dir:
                os.makedirs(os.path.join(content_dir, "subfolder"))

                with open(os.path.join(content_dir, "index.md"), "w") as f:
                    f.write("# Main Page")
                with open(os.path.join(content_dir, "subfolder/page.md"), "w") as f:
                    f.write("# Sub Page")

                template_path = os.path.join(content_dir, "template.html")
                with open(template_path, "w") as f:
                    f.write("<html><body>{content}</body></html>")

                generate_pages_recursive(content_dir, template_path, output_dir)

                output_subfolder = os.path.join(output_dir, "subfolder")

                assert os.path.exists(os.path.join(output_dir, "index.html"))
                assert os.path.exists(os.path.join(output_subfolder, "page.html"))



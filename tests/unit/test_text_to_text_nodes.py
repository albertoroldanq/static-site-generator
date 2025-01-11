import unittest

from src.transformations.text_to_text_nodes import text_to_text_nodes
from tests.unit.text_to_text_node_data import expected_results


class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_test_nodes(self):

        results = expected_results()

        for text in results:
            expected_result = results[text]
            result = text_to_text_nodes(text)
            self.assertEqual(expected_result, result)

    def test_handling_invalid_markdown(self):

        invalid_md_text = " **bold*"

        exception_message = "[ERROR processing text in src.transformations.text_to_text_nodes] Invalid Markdown syntax: Unmatched delimiter '**' found in input text."

        with self.assertRaises(Exception) as context:
            text_to_text_nodes(invalid_md_text)
            self.assertIn("Invalid markdown detected", str(context.exception))
        self.assertEqual(exception_message, str(context.exception))

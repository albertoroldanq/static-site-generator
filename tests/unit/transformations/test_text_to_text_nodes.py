import unittest

from src.transformations.text_to_text_nodes import text_to_text_nodes
from tests.TestCase import TestCase
from tests.unit.transformations.text_to_text_node_data import expected_results


class TestTextToTextNodes(TestCase):

    def test_text_to_test_nodes(self):

        expected = expected_results()

        for text in expected:
            expected_result = expected[text]
            result = text_to_text_nodes(text)
            self.assertEqual(expected_result, result)

    def test_handling_invalid_markdown(self):

        invalid_md_text = " **bold*"

        exception_message = "[ERROR processing text in src.transformations.text_to_text_nodes] Invalid Markdown syntax: Unmatched delimiter '**' found in input text: **bold*"

        with self.assertRaises(Exception) as context:
            text_to_text_nodes(invalid_md_text)
            self.assertIn("Invalid markdown detected", str(context.exception))
        self.assertEqual(exception_message, str(context.exception))

if __name__ == "__main__":
    unittest.main()

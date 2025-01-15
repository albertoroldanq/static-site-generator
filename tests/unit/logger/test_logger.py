import unittest
import logging
import os

from tests.TestCase import TestCase


class TestLogger(TestCase):
    def setUp(self):
        super().setUp()

    def test_log_file_generation(self):
        test_message = "This is a test logs message."
        logging.info(test_message)

        assert os.path.exists(self.log_file_path), f"Log file {self.log_file_path} was not created"

        with open(self.log_file_path, 'r') as log_file:
            logs = log_file.read()
            assert test_message in logs, "The test logs message was not found in the logs file"

if __name__ == "__main__":
    unittest.main()
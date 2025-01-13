import unittest
import logging
import os
from datetime import datetime


class TestLogger(unittest.TestCase):
    def test_log_file_generation(self):


        script_directory = os.path.dirname(os.path.abspath(__file__))
        log_directory = os.path.abspath(script_directory + '../../../../storage/logs')
        log_file_path = os.path.join(log_directory, datetime.now().strftime("%Y-%m-%d") + '.log')

        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        logging.basicConfig(
            level=logging.DEBUG,
            format='[TEST] - %(asctime)s - %(levelname)s - %(message)s',
            filename=log_file_path,
            filemode='a'
        )

        test_message = "This is a test logs message."
        logging.info(test_message)

        assert os.path.exists(log_file_path), f"Log file {log_file_path} was not created"

        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
            assert test_message in logs, "The test logs message was not found in the logs file"

if __name__ == "__main__":
    unittest.main()
import logging
import os
import unittest
from datetime import datetime


def _setup_logger():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_directory = os.path.abspath(script_directory + '../../storage/logs')
    log_file_path = os.path.join(log_directory, datetime.now().strftime("%Y-%m-%d") + '.log')

    if not os.path.exists(script_directory):
        os.makedirs(script_directory)

    logging.basicConfig(
        level=logging.INFO,
        format='[TEST] - %(asctime)s - %(levelname)s - %(message)s',
        filename=log_file_path,
        filemode='a'
    )


class TestCase(unittest.TestCase):
    _setup_logger()
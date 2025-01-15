import logging
import os
import tempfile
import unittest
from datetime import datetime

from config.config import LOGS_DIR


def _setup_logger():
    logs_dir = LOGS_DIR
    log_file_path = os.path.join(logs_dir, datetime.now().strftime("%Y-%m-%d") + '.log')

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logging.basicConfig(
        level=logging.INFO,
        format='[TEST] - %(asctime)s - %(levelname)s - %(message)s',
        filename=log_file_path,
        filemode='a'
    )


class TestCase(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.storage_dir = os.path.join(self.test_dir, "storage")
        self.logs_dir = os.path.join(self.storage_dir, "logs")
        self.log_file_path = os.path.join(self.logs_dir, datetime.now().strftime("%Y-%m-%d") + '.log')

        os.mkdir(self.storage_dir)
        os.mkdir(self.logs_dir)



        logging.basicConfig(
            level=logging.INFO,
            format='[TEST] - %(asctime)s - %(levelname)s - %(message)s',
            filename=self.log_file_path,
            filemode='a'
        )
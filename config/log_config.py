import logging
import os
from datetime import datetime

from config.config import LOGS_DIR

def setup_logger():
    logs_directory = LOGS_DIR
    log_file_path = os.path.join(LOGS_DIR, datetime.now().strftime("%Y-%m-%d") + '.log')

    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file_path,
        filemode='a'
    )
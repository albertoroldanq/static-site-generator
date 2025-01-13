import logging
import os
from datetime import datetime


def setup_logger():

    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_directory = os.path.abspath(script_directory + '../../../storage/logs')

    log_file_path = os.path.join(log_directory, datetime.now().strftime("%Y-%m-%d") + '.log')

    if not os.path.exists(script_directory):
        os.makedirs(script_directory)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file_path,
        filemode='a'
    )

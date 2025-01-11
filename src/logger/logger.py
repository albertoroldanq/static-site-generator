import logging

def log(level, message):
    match level:
        case logging.DEBUG:
            logging.debug(message)
        case logging.INFO:
            logging.info(message)
        case logging.WARNING:
            logging.warning(message)
        case logging.ERROR:
            logging.error(message)
        case logging.CRITICAL:
            logging.critical(message)
        case _:
            raise ValueError("Unsupported logging level provided")
import logging

def __log(level, message):
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

def debug(message):
    __log(logging.DEBUG, message)

def info(message):
    __log(logging.INFO, message)

def warning(message):
    __log(logging.WARNING, message)

def error(message):
    __log(logging.ERROR, message)

def critical(message):
    __log(logging.CRITICAL, message)
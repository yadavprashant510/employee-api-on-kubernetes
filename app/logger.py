import logging
import sys

from pythonjsonlogger import jsonlogger

from app.config import Config


def get_logger(name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(Config.LOG_LEVEL)

    formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(message)s")

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)

    logger.addHandler(console)

    return logger

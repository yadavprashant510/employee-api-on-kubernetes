import logging

from app.config import Config


def get_logger(name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(Config.LOG_LEVEL)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s : %(message)s")

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(console)

    return logger

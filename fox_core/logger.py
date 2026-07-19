"""
FOX Asset Studio
Logger
"""

import logging

LOGGER_NAME = "FOX_ASSET_STUDIO"


def create_logger():

    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(levelname)s] %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


logger = create_logger()

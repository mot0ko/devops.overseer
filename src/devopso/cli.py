import logging
import logging.config

from devopso.core.configuration import Configuration

_LOGGING_CONFIGURATION = "resources/configs/logging.yml"
_APP_LOGGER_NAME = "devops-overseer"


def get_hello_string() -> str:
    return "The overseer is in the room"


def main():
    logging.config.dictConfig(
        Configuration.read_configuration(_LOGGING_CONFIGURATION, expand_strs=True)
    )
    logging.getLogger(_APP_LOGGER_NAME).info(get_hello_string())

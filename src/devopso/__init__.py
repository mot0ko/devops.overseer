import logging
import logging.config

from devopso.core.configuration import Configuration

_LOGGING_CONFIGURATION = "resources/configs/logging.yml"


def _configure_logging():
    """Configure logging once, at first import of the package."""
    logging.config.dictConfig(Configuration.read_configuration(_LOGGING_CONFIGURATION, expand_strs=True))


# Ensure configuration runs only once
if not logging.getLogger().hasHandlers():
    _configure_logging()

import logging
import logging.config
from importlib.resources import files
from pathlib import Path

_APP_LOGGER_NAME = "devops-overseer"
_BANNER_PATH = "resources/devops-overseer.banner"


def get_hello_string() -> str:
    return "The overseer is in the room"


def print_banner() -> None:
    content = Path(files("devopso").joinpath(_BANNER_PATH)).read_text(encoding="utf-8")
    print(content)


def main():
    print_banner()
    logging.getLogger(_APP_LOGGER_NAME).warning(get_hello_string())

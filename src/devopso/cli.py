import argparse
import logging
from importlib.resources import files
from pathlib import Path
from importlib.metadata import entry_points
from pprint import pprint

_APP_LOGGER_NAME = "devops-overseer"
_BANNER_PATH = "resources/devops-overseer.banner"

def get_hello_string() -> str:
    return "The overseer is in the room"

def print_banner() -> None:
    content = Path(files("devopso").joinpath(_BANNER_PATH)).read_text(encoding="utf-8")
    print(content)

def load_plugins(subparsers):
    for ep in entry_points(group="devopso.plugins"):
        plugin_fn = ep.load()
        plugin_fn(subparsers)

def main():
    print_banner()
    logging.getLogger(_APP_LOGGER_NAME).warning(get_hello_string())
    
    parser = argparse.ArgumentParser(prog="devopso")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    
    load_plugins(subparsers)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
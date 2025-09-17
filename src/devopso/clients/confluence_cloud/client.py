from typing import Any, Dict

from devopso.core.rest_client import RestClient


class ConfluenceCloud(RestClient):
    def __init__(self) -> None:
        super().__init__("resources/configs/clients/confluence-cloud.yml")

    @staticmethod
    def get_myself() -> Dict[str, Any]:
        return ConfluenceCloud().get("myself")

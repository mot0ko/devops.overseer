from typing import Any, Dict

from devopso.core.rest_client import RestClient


class ConfluenceCloud(RestClient):
    _CONFLUENCE_CLOUD_CONFIGURATION = "resources/configs/clients/confluence-cloud.yml"
    _ENDPOINT_MYSELF = "myself"

    def __init__(self) -> None:
        super().__init__(ConfluenceCloud._CONFLUENCE_CLOUD_CONFIGURATION)

    @staticmethod
    def get_myself() -> Dict[str, Any]:
        return ConfluenceCloud().get(ConfluenceCloud._ENDPOINT_MYSELF)

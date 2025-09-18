from typing import Any, Dict

from devopso.core.rest_client import RestClient


class ConfluenceCloud(RestClient):
    """
    Client for interacting with the Confluence Cloud REST API.

    This class extends the generic `RestClient` to provide
    Confluence Cloud–specific endpoints and configuration.
    """

    _CONFLUENCE_CLOUD_CONFIGURATION = "resources/configs/clients/confluence-cloud.yml"
    _ENDPOINT_MYSELF = "myself"

    def __init__(self) -> None:
        """
        Initialize the Confluence Cloud client.

        Loads the Confluence Cloud–specific configuration
        from the predefined YAML file.
        """
        super().__init__(ConfluenceCloud._CONFLUENCE_CLOUD_CONFIGURATION)

    @staticmethod
    def get_myself() -> Dict[str, Any]:
        """
        Retrieve details about the currently authenticated user.

        Returns:
            Dict[str, Any]: A dictionary containing information
            about the authenticated Confluence Cloud user,
            such as account ID, email, and profile details.
        """
        return ConfluenceCloud().get(ConfluenceCloud._ENDPOINT_MYSELF)

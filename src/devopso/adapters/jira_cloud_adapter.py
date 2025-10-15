from typing import Any, Dict
from pprint import pformat

from devopso.core.rest_adapter import RestAdapter
import devopso.clients.jira_cloud


class JiraCloud(RestAdapter):
    """Adapter class for interacting with the Jira Cloud REST API.

    This class wraps the generated `devopso.clients.jira_cloud` client,
    automatically configuring authentication and providing simplified
    static methods for common operations such as retrieving user information
    and groups.

    Attributes:
        _DEFAULT_PATH_CONFIGURATION (str): Default configuration file path for Jira Cloud client setup.
        client (devopso.clients.jira_cloud.ApiClient): Configured API client instance used for API calls.
    """

    _DEFAULT_PATH_CONFIGURATION = "resources/configs/clients/jira-cloud.yml"

    def __init__(self) -> None:
        """Initializes the JiraCloud adapter.

        Loads the REST adapter configuration, initializes the Jira Cloud
        API client using the configured base URL and authentication headers.
        """
        super().__init__(JiraCloud._DEFAULT_PATH_CONFIGURATION)

        configuration = devopso.clients.jira_cloud.Configuration(host=self.base_url)
        self.client = devopso.clients.jira_cloud.ApiClient(configuration)
        self.client.default_headers = self.client.default_headers | self._auth_header

    @staticmethod
    def get_myself():
        """Retrieve information about the currently authenticated Jira user.

        Returns:
            devopso.clients.jira_cloud.models.UserDetails | None:
                The user details object returned by the API, or ``None`` if an exception occurred.

        Logs:
            - Debug information with the formatted API response on success.
            - Error message if the API call fails.
        """
        api_response = None
        a = JiraCloud()
        try:
            api_response = devopso.clients.jira_cloud.MyselfApi(a.client).get_current_user(expand="groups")
            a.debug("The response of JiraCloud->get_myself:")
            a.debug(pformat(api_response))
        except Exception as e:
            a.error("Exception when calling JiraCloud->get_myself: %s" % e)
        return api_response
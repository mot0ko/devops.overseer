import base64
import logging
import logging.config
from importlib.resources import files
from pathlib import Path
from pprint import pformat, pprint

from nacl import encoding, public

import devopso.clients.github
from devopso.clients.github.models.actions_public_key import ActionsPublicKey
from devopso.clients.github.rest import ApiException

# import devopso.clients.confluence_cloud.client


_APP_LOGGER_NAME = "devops-overseer"
_BANNER_PATH = "resources/devops-overseer.banner"


def get_hello_string() -> str:
    return "The overseer is in the room"


def print_banner() -> None:
    content = Path(files("devopso").joinpath(_BANNER_PATH)).read_text(encoding="utf-8")
    print(content)

def encrypt_secret(public_key: str, secret_value: str) -> str:
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return base64.b64encode(encrypted).decode("utf-8")

def set_secret(owner: str, repo: str, secrets: dict) -> None:
    # Defining the host is optional and defaults to https://api.github.com
    # See configuration.py for a list of all supported configuration parameters.

    configuration = devopso.clients.github.Configuration(
        host = "https://api.github.com"
    )
    api_response = None
    
    with devopso.clients.github.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_client.user_agent = 'devops-overseer-RestClient/1.0'
        api_client.set_default_header('Authorization', 'Bearer your-token')
        
        api_instance = devopso.clients.github.ActionsApi(api_client)

        try:
            # Get a repository public key
            api_response = api_instance.actions_get_repo_public_key(owner, repo)
            logging.getLogger(_APP_LOGGER_NAME).warning("The response of ActionsApi->actions_get_repo_public_key:")
            logging.getLogger(_APP_LOGGER_NAME).warning(pformat(api_response))
        except Exception as e:
            logging.getLogger(_APP_LOGGER_NAME).warning("Exception when calling ActionsApi->actions_get_repo_public_key: %s" % e)
    
    if api_response:
        encrypt_key = api_response.key
        encrypt_key_id = api_response.key_id
        for secret_name, secret_value in secrets.items():
            actions_create_or_update_repo_secret_request = {"encrypted_value": encrypt_secret(encrypt_key, secret_value),"key_id": encrypt_key_id}

            try:
                # Create or update a repository secret
                api_response = api_instance.actions_create_or_update_repo_secret(owner, repo, secret_name, actions_create_or_update_repo_secret_request)
                logging.getLogger(_APP_LOGGER_NAME).warning("The response of ActionsApi->actions_create_or_update_repo_secret:")
                logging.getLogger(_APP_LOGGER_NAME).warning(pformat(api_response))
            except Exception as e:
                logging.getLogger(_APP_LOGGER_NAME).warning("Exception when calling ActionsApi->actions_create_or_update_repo_secret: %s" % e)


def main():
    print_banner()
    logging.getLogger(_APP_LOGGER_NAME).warning(get_hello_string())
    # mot0ko/ci.github-action.twine-upload
    set_secret("mot0ko", "ci.github-action.twine-upload", {'PYPI_USER' : '__token__', 'PYPI_PASS': 'asdfasdfasdf'} )

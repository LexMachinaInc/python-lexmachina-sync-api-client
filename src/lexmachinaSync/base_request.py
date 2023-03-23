import configparser
from pathlib import Path

import requests
from requests import JSONDecodeError

from .auth import Auth


class BaseRequest(Auth):
    def _get(self, version: str, path=None, args=None, params=None):
        config, config_file = self.config_reader()
        try:
            with requests.Session() as session:
                token = self.get_token()
                url = config.get("URLS", "base_url")
                headers = {"Authorization": f"Bearer {token}", "User-Agent": "lexmachina-python-client-0.0.2"}
                if args is None:
                    if version != "/":
                        url = f"{url}{version}/{path}"
                    else:
                        url = f"{url}{version}{path}"
                elif version != "/":
                    url = f"{url}{version}/{path}/{args}"
                else:
                    url = f"{url}{version}{path}/{args}"
                with session.get(url, headers=headers,
                                 params=params) as response:
                    return response
        except JSONDecodeError:
            return response.text

    def _post(self, version: str, path=None, data=None):
        with requests.Session() as session:
            config, config_file = self.config_reader()
            token = self.get_token()
            url = config.get("URLS", "base_url")
            headers = {"Authorization": f"Bearer {token}", "User-Agent": "lexmachina-python-client-0.0.2"}
            url = f"{url}{version}{path}"
            try:

                with session.post(
                        url, headers=headers, json=data
                ) as response:
                    return response.json()
            except JSONDecodeError:
                return response.text

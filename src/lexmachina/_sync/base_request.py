import configparser
from pathlib import Path

import requests
from requests import JSONDecodeError

from .auth import Auth


class BaseRequest(Auth):
    def _get(self, path=None, args=None, params=None):
        config, config_file = self.config_reader()
        with requests.Session() as session:
            url = config.get("URLS", "base_url")
            headers = {"Authorization": f"Bearer {self.get_token()}", "User-Agent": "lexmachina-python-client-0.0.2"}
            if args is None:
                url = f"{url}/{path}"
            else:
                url = f"{url}/{path}/{args}"
            try:
                with session.get(url, headers=headers,
                                 params=params) as response:
                    return response.json()
            except JSONDecodeError:
                return response.text

    def _post(self, path=None, data=None):
        config, config_file = self.config_reader()
        with requests.Session() as session:
            url = config.get("URLS", "base_url")
            headers = {"Authorization": f"Bearer {self.get_token()}", "User-Agent": "lexmachina-python-client-0.0.2"}
            url = f"{url}/{path}"
            try:
                with session.post(
                        url, headers=headers, json=data
                ) as response:
                    return response.json()
            except JSONDecodeError:
                return response.text

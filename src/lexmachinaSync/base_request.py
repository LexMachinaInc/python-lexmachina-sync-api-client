import requests
from requests import JSONDecodeError

from .auth import Auth


class BaseRequest(Auth):
    def _get(self, version: str = "beta", path=None, args=None, params=None):
        try:
            with requests.Session() as session:
                token = self.get_token()
                headers = {"Authorization": f"Bearer {token}", "User-Agent": "lexmachina-0.0.1"}
                if args is None:
                    url = f"https://api.lexmachina.com/{version}/{path}"
                else:
                    url = f"https://api.lexmachina.com/{version}/{path}/{args}"
                with session.get(url, headers=headers,
                                 params=params) as response:
                    return response.json()
        except JSONDecodeError:
            return response.text

    def _post(self, version: str = "beta", path=None, data=None):
        with requests.Session() as session:
            token = self.get_token()
            headers = {"Authorization": f"Bearer {token}", "User-Agent": "lexmachina-0.0.1"}
            url = f"https://api.lexmachina.com/{version}/{path}"
            try:

                with session.post(
                        url, headers=headers, json=data
                ) as response:
                    return response.json()
            except JSONDecodeError:
                return response.text

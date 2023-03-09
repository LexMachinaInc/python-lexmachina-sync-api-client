import requests
from requests import JSONDecodeError

from .auth import Auth


class BaseRequest(Auth):
    def _get(self, version: str = "/", path=None, args=None, params=None):
        try:
            with requests.Session() as session:
                token = self.get_token()
                headers = {"Authorization": f"Bearer {token}", "User-Agent": "lexmachina-python-client-0.0.2"}
                if args is None:
                    url = f"https://api.beta.lexmachina.com{version}{path}"
                else:
                    url = f"https://api.beta.lexmachina.com{version}{path}/{args}"
                with session.get(url, headers=headers,
                                 params=params) as response:
                    return response
        except JSONDecodeError:
            return response.text

    def _post(self, version: str = "/", path=None, data=None):
        with requests.Session() as session:
            token = self.get_token()
            headers = {"Authorization": f"Bearer {token}", "User-Agent": "lexmachina-python-client-0.0.2"}
            url = f"https://api.beta.lexmachina.com{version}{path}"
            print(url)
            try:

                with session.post(
                        url, headers=headers, json=data
                ) as response:
                    return response.json()
            except JSONDecodeError:
                return response.text

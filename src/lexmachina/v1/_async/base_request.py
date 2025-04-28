import json

import aiohttp
from aiohttp import ContentTypeError

from .auth import Auth


class BaseRequest(Auth):
    async def _get(self, path=None, args=None, params=None):
        config, config_file = self.config_reader()
        try:
            async with aiohttp.ClientSession() as session:
                url = config.get("URLS", "base_url")
                headers = {"Authorization": f"Bearer {await self._get_token()}", "User-Agent": "lexmachina-python-async-client-0.0.2"}
                if args is None:
                    url = f"{url}/{path}"
                else:
                    url = f"{url}/{path}/{args}"
                async with session.get(url, headers=headers,
                                       params=params) as response:
                    return await response.json()
        except ContentTypeError:
            return await response.text()

    async def _post(self, path=None, data=None):
        config, config_file = self.config_reader()
        async with aiohttp.ClientSession() as session:
            url = config.get("URLS", "base_url")
            headers = {"Authorization": f"Bearer {await self._get_token()}", "User-Agent": "lexmachina-python-async-client-0.0.2"}
            url = f"{url}/{path}"
            try:

                async with session.post(
                     url, headers=headers, json=data
                ) as response:
                    return await response.json()
            except ContentTypeError:
                return await response.text()

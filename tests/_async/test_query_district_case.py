import json
from configparser import ConfigParser

import pytest
import pprint

from src.lexmachina.client import LexMachinaClient


class TestQueryDistrictCase:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")

    @pytest.mark.asyncio
    async def test_query_district_case_default(self):
        response = await self.client.query_district_cases({})
        print(pprint.pformat(response))
        assert len(response.get("caseIds")) == 5

    @pytest.mark.asyncio
    async def test_query_district_case_page_size_100(self):
        response = await self.client.query_district_cases({'pageSize': 100})
        print(pprint.pformat(response))
        assert len(response.get("caseIds")) == 100
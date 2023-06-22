import json
from configparser import ConfigParser

import pytest
import pprint

from lexmachina import DistrictCaseQueryRequest
from lexmachina import LexMachinaAsyncClient as LexMachinaClient


class TestQueryDistrictCase:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")
    query = DistrictCaseQueryRequest()


    @pytest.mark.asyncio
    async def test_query_district_case_default(self):
        response = await self.client.query_district_case(query=self.query.set_damages_minimum_amount(100))
        assert len(response) == 5
    @pytest.mark.asyncio
    async def test_query_district_case_page_size_100(self):
        response = await self.client.query_district_case(query=self.query.set_page_size(100))
        assert len(response) == 100




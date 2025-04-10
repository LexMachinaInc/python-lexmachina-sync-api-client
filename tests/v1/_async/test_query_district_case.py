from configparser import ConfigParser

import pytest

from lexmachina import DistrictCaseQueryRequest
from lexmachina import LexMachinaAsyncClient as LexMachinaClient


client = LexMachinaClient("config.ini")
config = ConfigParser()
config.read("config.ini")


@pytest.mark.asyncio
async def test_query_district_case_default():
    query = DistrictCaseQueryRequest().set_damages_minimum_amount(100)
    response = await client.query_district_case(query)
    assert len(response) == 5

@pytest.mark.asyncio
async def test_query_district_case_page_size_100():
    query = DistrictCaseQueryRequest().set_page_size(100).include_case_tags("Voting")
    response = await client.query_district_case(query)
    assert len(response) == 100

@pytest.mark.asyncio
async def test_query_district_case_events():
    query = DistrictCaseQueryRequest().include_event_types("Filed")
    response = await client.query_district_case(query)
    assert len(response) == 5

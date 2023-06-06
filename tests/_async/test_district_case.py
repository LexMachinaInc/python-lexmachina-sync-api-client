import json
from configparser import ConfigParser

import pytest

from src.lexmachina.client import LexMachinaClient


class TestGetDistrictCase:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")
    INTEGER_FUZZ = json.loads(config.get("CONSTANTS", "INTEGER_FUZZ"))

    @pytest.mark.asyncio
    @pytest.mark.parametrize("cases", INTEGER_FUZZ)
    async def test_get_district_case_integer_fuzz(self, cases):

        response = await self.client.get_district_cases(cases=cases)
        assert response.get("detail") == "case_id not found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("cases", [66])
    async def test_get_district_case_positive(self, cases):
        response = await self.client.get_district_cases(cases=cases)
        assert response['caseId'] == cases

import json
from configparser import ConfigParser

import pytest

from src.lexmachina.client import LexMachinaClient


class TestGetAttorneys:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")
    INTEGER_FUZZ = json.loads(config.get("CONSTANTS", "INTEGER_FUZZ"))

    @pytest.mark.asyncio
    @pytest.mark.parametrize("attorney_id", INTEGER_FUZZ)
    async def test_get_attorney_integer_fuzz(self, attorney_id):
        response = await self.client.get_attorneys(attorneys=attorney_id)
        assert response.get("detail") == "No attorney matching provided attorney ID was found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("attorney_id", [INTEGER_FUZZ])
    async def test_get_attorney_integer_fuzz(self, attorney_id):
        response = await self.client.get_attorneys(attorneys=attorney_id)
        assert response.get("detail") == "No attorneys matching provided attorney IDs were found"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("attorney_id", [110161257, 43337, 14974596])
    async def test_get_attorney_positive(self, attorney_id):
        response = await self.client.get_attorneys(attorneys=attorney_id)
        assert response['attorneyId'] == attorney_id

    @pytest.mark.asyncio
    @pytest.mark.parametrize("q", ["Justin"])
    async def test_search_attorney_positive(self, q):
        response = await self.client.search_attorneys(q=q)
        assert any(i['name'] == 'Justin M. Brownstone' for i in response['attorneys'])

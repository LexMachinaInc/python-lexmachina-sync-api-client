import pytest

from src.lexmachina._async.client import LexMachinaAsyncClient as LexMachinaClient


class TestListCaseTags:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_case_types(self):
        response = await self.client.list_case_types("FederalDistrict")
        assert "Bankruptcy" in response[0]['caseTypes']
        assert "Tax" in response[0]['caseTypes']

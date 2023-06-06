import pytest

from src.lexmachina._async.client import LexMachinaAsyncClient as LexMachinaClient


class TestListEvents:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_events(self):
        response = await self.client.list_events("FederalDistrict")
        assert "Markman Hearing" in response['events']

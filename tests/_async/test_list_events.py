import pytest

from src.lexmachina.client import LexMachinaClient


class TestListEvents:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_events(self):
        response = await self.client.list_events()
        assert "Markman Hearing" in response

import pytest

from src.lexmachina._async.client import LexMachinaAsyncClient as LexMachinaClient


class TestHealth:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_health(self):
        response = await self.client.health()
        assert response == "Feelin' fine." or response == "Database failure"

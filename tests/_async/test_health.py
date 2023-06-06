import pytest

from src.lexmachina.client import LexMachinaClient


class TestHealth:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_health(self):
        response = await self.client.health()
        assert response == "Feelin' fine." or response == "Database failure"

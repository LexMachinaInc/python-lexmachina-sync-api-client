import pytest

from src.lexmachina.client import LexMachinaClient


class TestListDamages:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_damages(self):
        response = await self.client.list_damages()
        assert "Prejudgment Interest" in response['General']
        assert "Statutory Damages (Copyright)" in response['Copyright']
        assert "Special Damages" in response['False Claims']

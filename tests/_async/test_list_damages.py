import pytest

from src.lexmachina._async.client import LexMachinaAsyncClient as LexMachinaClient


class TestListDamages:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_damages(self):
        response = await self.client.list_damages_federal()
        assert "Prejudgment Interest" in response['damagesByPraticeArea']['General']
        assert "Statutory Damages (Copyright)" in response['damagesByPraticeArea']['Copyright']
        assert "Special Damages (False Claims)" in response['damagesByPraticeArea']['False Claims']

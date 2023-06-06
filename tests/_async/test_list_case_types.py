import pytest

from src.lexmachina.client import LexMachinaClient


class TestListCaseTags:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_case_types(self):
        response = await self.client.list_case_types()
        assert "Bankruptcy" in response
        assert "Tax" in response

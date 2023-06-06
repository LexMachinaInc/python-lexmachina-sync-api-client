import pytest

from src.lexmachina._async.client import LexMachinaAsyncClient as LexMachinaClient


class TestListCaseTags:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_case_tags(self):
        response = await self.client.list_case_tags()
        assert "Design Patent" in response
        assert "Jury Trial" in response

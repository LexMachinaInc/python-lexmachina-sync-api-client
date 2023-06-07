import pytest

from src.lexmachina._async.client import LexMachinaAsyncClient as LexMachinaClient


class TestListJudmentSources:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_judgment_sources(self):
        response = await self.client.list_judgment_sources_federal()
        assert "No Type Specified" in response['damages']
        assert "Consent Judgment" in response['remedies']
        assert "Judgment as a Matter of Law" in response['findings']

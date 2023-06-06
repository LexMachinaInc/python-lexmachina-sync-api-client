import pytest

from src.lexmachina.client import LexMachinaClient


class TestListJudmentSources:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_judgment_sources(self):
        response = await self.client.list_judgment_sources()
        assert "No Type Specified" in response['damages']
        assert "Consent Judgment" in response['remedies']
        assert "Judgment as a Matter of Law" in response['findings']

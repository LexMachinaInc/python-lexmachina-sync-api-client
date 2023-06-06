import pytest

from src.lexmachina.client import LexMachinaClient


class TestListCaseResolutions:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_case_resolutions(self):
        response = await self.client.list_case_resolutions()
        assert any(case['summary'] == 'Claimant Win' for case in response)
        assert any(case['specific'] == 'Trial' for case in response)
        assert any(case['summary'] == 'Procedural' for case in response)

import pytest

from lexmachina import LexMachinaAsyncClient as LexMachinaClient


class TestListCaseResolutions:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_case_resolutions(self):
        response = await self.client.list_case_resolutions("FederalDistrict")
        assert any(case['summary'] == 'Claimant Win' for case in response['caseResolutions'])
        assert any(case['specific'] == 'Trial' for case in response['caseResolutions'])
        assert any(case['summary'] == 'Procedural' for case in response['caseResolutions'])


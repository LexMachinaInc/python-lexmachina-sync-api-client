import pytest

from lexmachina import LexMachinaAsyncClient as LexMachinaClient


class TestListCourts:
    client = LexMachinaClient("config.ini")

    @pytest.mark.asyncio
    async def test_list_courts(self):
        response = await self.client.list_courts("FederalDistrict")
        assert any(court['type'] == 'FederalDistrict' for court in response)
        assert any(court['name'] == 'U.S. District Court for the District of Oregon' for court in response)
        assert any(court['abbreviation'] == 'ohsd' for court in response)

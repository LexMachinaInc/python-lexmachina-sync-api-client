from lexmachina._sync.client import LexMachinaClient


class TestListCourts:
    client = LexMachinaClient("config.ini")

    def test_list_courts(self):
        response = self.client.list_courts()
        assert any(court['type'] == 'FederalDistrict' for court in response)
        assert any(court['name'] == 'U.S. District Court for the District of Oregon' for court in response)
        assert any(court['abbreviation'] == 'ohsd' for court in response)

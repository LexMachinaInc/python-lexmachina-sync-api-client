from lexmachina import LexMachinaClient


class TestListEvents:
    client = LexMachinaClient("config.ini")

    def test_list_events_federal(self):
        response = self.client.list_events("FederalDistrict")
        assert "Markman Hearing" in response['events']

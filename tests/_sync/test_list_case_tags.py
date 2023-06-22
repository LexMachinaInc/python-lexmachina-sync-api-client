from lexmachina import LexMachinaClient


class TestListCaseTags:
    client = LexMachinaClient("config.ini")

    def test_list_case_tags_federal(self):
        response = self.client.list_case_tags("FederalDistrict")
        assert "Design Patent" in response[0]['caseTags']
        assert "Jury Trial" in response[0]['caseTags']

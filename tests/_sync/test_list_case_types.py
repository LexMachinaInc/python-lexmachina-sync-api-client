from lexmachina._sync.client import LexMachinaClient


class TestListCaseTags:
    client = LexMachinaClient("config.ini")

    def test_list_case_types_federal(self):
        response = self.client.list_case_types("FederalDistrict")
        assert "Bankruptcy" in response[0]['caseTypes']
        assert "Tax" in response[0]['caseTypes']

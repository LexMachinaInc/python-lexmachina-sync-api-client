from lexmachina import LexMachinaClient


class TestListCaseResolutions:
    client = LexMachinaClient("config.ini")

    def test_list_case_resolutions_federal(self):
        response = self.client.list_case_resolutions(court_type="FederalDistrict")
        assert any(case['summary'] == 'Claimant Win' for case in response['caseResolutions'])
        assert any(case['specific'] == 'Trial' for case in response['caseResolutions'])
        assert any(case['summary'] == 'Procedural' for case in response['caseResolutions'])

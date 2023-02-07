from configparser import ConfigParser
from src.lexmachinaSync.client import LexMachinaClient


class TestQueryDistrictCase:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")

    def test_query_district_case_default(self):
        response = self.client.query_district_cases({})
        assert len(response.get("caseIds")) == 5

    def test_query_district_case_page_size_100(self):
        response = self.client.query_district_cases({'pageSize': 100})
        assert len(response.get("caseIds")) == 100

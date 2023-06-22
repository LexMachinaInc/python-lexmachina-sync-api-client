from configparser import ConfigParser
from lexmachina import LexMachinaClient
from lexmachina import DistrictCaseQueryRequest


class TestQueryDistrictCase:
    client = LexMachinaClient("config.ini")
    query = DistrictCaseQueryRequest()
    config = ConfigParser()
    config.read("config.ini")

    def test_query_district_case_default(self):
        response = self.client.query_district_case(query=self.query.set_damages_minimum_amount(100))
        assert len(response) == 5

    def test_query_district_case_page_size_100(self):
        response = self.client.query_district_case(query=self.query.set_page_size(100))
        assert len(response) == 100

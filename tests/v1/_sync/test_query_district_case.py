from configparser import ConfigParser
from lexmachina import LexMachinaClient
from lexmachina import DistrictCaseQueryRequest



client = LexMachinaClient("config.ini")    
config = ConfigParser()
config.read("config.ini")

def test_query_district_case_default():
    query = DistrictCaseQueryRequest().set_damages_minimum_amount(100)
    response = client.query_district_case(query)
    assert len(response) == 5

def test_query_district_case_page_size_100():
    query = DistrictCaseQueryRequest().set_page_size(100).include_case_tags("COVID-19")
    response = client.query_district_case(query)
    assert len(response) == 100

def test_query_district_case_events():
    query = DistrictCaseQueryRequest().include_event_types("Filed")
    response = client.query_district_case(query)
    assert len(response) == 5

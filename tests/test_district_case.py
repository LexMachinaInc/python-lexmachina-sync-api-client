import json
from configparser import ConfigParser

import pytest

from src.lexmachinaSync.client import LexMachinaClient


class TestGetDistrictCase:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")
    INTEGER_FUZZ = json.loads(config.get("CONSTANTS", "INTEGER_FUZZ"))

    @pytest.mark.parametrize("cases", INTEGER_FUZZ)
    def test_get_district_case_integer_fuzz(self, cases):
        response = self.client.get_district_cases(cases=cases)
        assert response.get("detail") == "case_id not found"

    @pytest.mark.parametrize("cases", [66])
    def test_get_district_case_positive(self, cases):
        response = self.client.get_district_cases(cases=cases)
        assert response['caseId'] == cases

import json
from configparser import ConfigParser

import pytest

from lexmachina import LexMachinaClient


class TestGetLawFirms:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")
    INTEGER_FUZZ = json.loads(config.get("CONSTANTS", "INTEGER_FUZZ"))

    @pytest.mark.parametrize("law_firms", INTEGER_FUZZ)
    def test_get_law_firms_integer_fuzz(self, law_firms):
        response = self.client.get_law_firms(law_firms=law_firms)
        assert response.get("detail") == "No law firm matching provided law firm ID was found"

    @pytest.mark.parametrize("law_firms", [INTEGER_FUZZ])
    def test_get_law_firms_integer_fuzz(self, law_firms):
        response = self.client.get_law_firms(law_firms=law_firms)
        assert response.get("detail") == "No law firms matching provided law firm IDs were found"

    @pytest.mark.parametrize("law_firms", [920, 604, 10239533])
    def test_get_law_firms_positive(self, law_firms):
        response = self.client.get_law_firms(law_firms=law_firms)
        assert response['lawFirmId'] == law_firms

    @pytest.mark.parametrize("q", ["Quinn"])
    def test_search_law_firms(self, q):
        response = self.client.search_law_firms(q=q)
        assert any(i['name'] == 'Quinn Emanuel Urquhart & Sullivan' for i in response['lawFirms'])

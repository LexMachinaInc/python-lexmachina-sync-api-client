import json
from configparser import ConfigParser

import pytest

from lexmachina._sync.client import LexMachinaClient


class TestGetParties:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")
    INTEGER_FUZZ = json.loads(config.get("CONSTANTS", "INTEGER_FUZZ"))

    @pytest.mark.parametrize("parties", INTEGER_FUZZ)
    def test_get_parties_integer_fuzz(self, parties):
        response = self.client.get_parties(parties=parties)
        assert response.get("detail") == "No party matching provided party ID was found"

    @pytest.mark.parametrize("parties", [INTEGER_FUZZ])
    def test_get_parties_integer_fuzz(self, parties):
        response = self.client.get_parties(parties=parties)
        assert response.get("detail") == "No parties matching provided party IDs were found"

    @pytest.mark.parametrize("parties", [2273, 58589403, 73224])
    def test_get_parties_positive(self, parties):
        response = self.client.get_parties(parties=parties)
        assert response['partyId'] == parties

    @pytest.mark.parametrize("q", ["Apple"])
    def test_search_parties(self, q):
        response = self.client.search_parties(q=q)
        assert any(i['name'] == 'Apple Computer, Inc.' for i in response['parties'])

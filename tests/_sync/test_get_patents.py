import json
from configparser import ConfigParser

import pytest

from lexmachina import LexMachinaClient


class TestGetPatents:
    client = LexMachinaClient("config.ini")
    config = ConfigParser()
    config.read("config.ini")
    INTEGER_FUZZ = json.loads(config.get("CONSTANTS", "INTEGER_FUZZ"))

    @pytest.mark.parametrize("patents", INTEGER_FUZZ)
    def test_get_patents_integer_fuzz(self, patents):
        response = self.client.get_patents(patents=patents)
        assert response.get("detail") == "No patent matching provided patent number was found"

    @pytest.mark.parametrize("patents", [INTEGER_FUZZ])
    def test_get_patents_integer_fuzz(self, patents):
        response = self.client.get_patents(patents=patents)
        assert response.get("detail") == "No patents matching provided patent numbers were found"

    @pytest.mark.parametrize("patents", [6904359, 6714859, 5668543])
    def test_get_patents_positive(self, patents):
        response = self.client.get_patents(patents=patents)
        assert response['number'] == str(patents)

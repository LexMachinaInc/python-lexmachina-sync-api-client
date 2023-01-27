import pytest

from src.lexmachinaSync.client import LexMachinaClient


class TestListDamages:
    client = LexMachinaClient("config.ini")

    def test_list_damages(self):
        response = self.client.list_damages()
        assert "Prejudgment Interest" in response['General']
        assert "Statutory Damages (Copyright)" in response['Copyright']
        assert "Special Damages" in response['False Claims']

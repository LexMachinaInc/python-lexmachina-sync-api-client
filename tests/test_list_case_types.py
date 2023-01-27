import pytest

from src.lexmachinaSync.client import LexMachinaClient


class TestListCaseTags:
    client = LexMachinaClient("config.ini")

    def test_list_case_types(self):
        response = self.client.list_case_types()
        assert "Bankruptcy" in response
        assert "Tax" in response

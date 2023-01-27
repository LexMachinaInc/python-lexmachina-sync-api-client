import pytest

from src.lexmachinaSync.client import LexMachinaClient


class TestListEvents:
    client = LexMachinaClient("config.ini")

    def test_list_events(self):
        response = self.client.list_events()
        assert "Markman Hearing" in response

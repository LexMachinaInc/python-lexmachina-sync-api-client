from lexmachina._sync.client import LexMachinaClient


class TestHealth:
    client = LexMachinaClient("config.ini")

    def test_health(self):
        response = self.client.health()
        assert response == "Feelin' fine." or response == "Database failure"

from lexmachina._sync.client import LexMachinaClient


class TestListDamages:
    client = LexMachinaClient("config.ini")

    def test_list_damages_federal(self):
        response = self.client.list_damages_federal_district()
        assert "Prejudgment Interest" in response['damagesByPraticeArea']['General']
        assert "Statutory Damages (Copyright)" in response['damagesByPraticeArea']['Copyright']
        assert "Special Damages (False Claims)" in response['damagesByPraticeArea']['False Claims']

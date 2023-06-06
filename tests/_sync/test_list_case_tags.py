from lexmachina._sync.client import LexMachinaClient


class TestListCaseTags:
    client = LexMachinaClient("config.ini")

    def test_list_case_tags(self):
        response = self.client.list_case_tags()
        assert "Design Patent" in response
        assert "Jury Trial" in response

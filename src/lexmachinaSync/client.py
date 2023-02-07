from typing import List

from .base_request import BaseRequest
from .query_district_cases import QueryDistrictCase


class LexMachinaClient(BaseRequest):
    def __init__(self, config_file_path=None, client_id=None, client_secret=None):
        super().__init__(config_file_path, client_id, client_secret)
        self.config_file_path = config_file_path
        self.client_id = client_id
        self.client_secret = client_secret
        self.query = QueryDistrictCase(config=self.config_file_path)

    def get_district_cases(self, cases: int):
        response = self.get(path='district-cases', args=cases)
        return response

    def query_district_case(self, query, options=None):
        return self.query.query_district_case(query, options)

    def get_parties(self, parties: List[str]):
        if isinstance(parties, list):
            response = self.get(path='parties', params={"partyIds": parties})
        else:
            response = self.get(path='parties', args=parties)
        return response

    def search_parties(self, q: str, page_number: int = 1, page_size: int = 500):
        response = self.get(path='search-parties', params={"q": q,
                                                           "pageNumber": page_number,
                                                           "pageSize": page_size})
        return response

    def get_attorneys(self, attorneys: List[int]):
        if isinstance(attorneys, list):
            response = self.get(path='attorneys', params={"attorneyIds": attorneys})
        else:
            response = self.get(path='attorneys', args=attorneys)
        return response

    def search_attorneys(self, q: str, page_number: int = 1, page_size: int = 500):
        response = self.get(path='search-attorneys', params={"q": q,
                                                             "pageNumber": page_number,
                                                             "pageSize": page_size})
        return response

    def get_law_firms(self, law_firms: List[int]):
        if isinstance(law_firms, list):
            response = self.get(path='law-firms', params={"lawFirmIds": law_firms})
        else:
            response = self.get(path='law-firms', args=law_firms)
        return response

    def search_law_firms(self, q: str, page_number: int = 1, page_size: int = 500):
        response = self.get(path='search-law-firms', params={"q": q,
                                                             "pageNumber": page_number,
                                                             "pageSize": page_size})
        return response

    def get_federal_judges(self, federal_judges: List[int]):
        if isinstance(federal_judges, list):
            response = self.get(path='federal-judges', params={"federalJudgeIds": federal_judges})
        else:
            response = self.get(path='federal-judges', args=federal_judges)
        return response

    def get_magistrate_judges(self, magistrate_judges: str):
        response = self.get(path='magistrate-judges', args=magistrate_judges)
        return response

    def search_judges(self, q: str):
        response = self.get(path='search-judges', params={"q": q})
        return response

    def get_patents(self, patents: List[str]):
        if isinstance(patents, list):
            response = self.get(path='patents', params={"patentNumbers": patents})
        else:
            response = self.get(path='patents', args=patents)
        return response

    def list_case_resolutions(self):
        return self.list(path='list-case-resolutions')

    def list_case_tags(self):
        return self.list(path='list-case-tags')

    def list_case_types(self):
        return self.list(path='list-case-types')

    def list_courts(self):
        return self.list(path='list-courts')

    def list_damages(self):
        return self.list(path='list-damages')

    def list_events(self):
        return self.list(path='list-events')

    def list_judgment_sources(self):
        return self.list(path='list-judgment-sources')

    def list(self, path):
        response = self.get(path=path)
        return response

    def health(self):
        response = self.get(path="health")
        return response

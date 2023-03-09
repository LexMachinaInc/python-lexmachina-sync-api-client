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
        """
        
        :param cases: int of a case ID
        :return: JSON case structure
        """
        response = self._get(path='district-cases', args=cases)
        return response.json()

    def query_district_case(self, query, options=None, page_size=100):
        return self.query.query_district_case(query, options, page_size)

    def get_parties(self, parties: List[str]):
        """

        :param parties: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(parties, list):
            response = self._get(path='parties', params={"partyIds": parties})
        else:
            response = self._get(path='parties', args=parties)
        return response.json()

    def search_parties(self, q: str, page_number: int = 1, page_size: int = 500):
        """

        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        response = self._get(path='search-parties', params={"q": q,
                                                           "pageNumber": page_number,
                                                           "pageSize": page_size})
        return response.json()

    def get_attorneys(self, attorneys: List[int]):
        """
        :param attorneys: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(attorneys, list):
            response = self._get(path='attorneys', params={"attorneyIds": attorneys})
        else:
            response = self._get(path='attorneys', args=attorneys)
        return response.json()

    def search_attorneys(self, q: str, page_number: int = 1, page_size: int = 500):
        """
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        response = self._get(path='search-attorneys', params={"q": q,
                                                             "pageNumber": page_number,
                                                             "pageSize": page_size})
        return response.json()

    def get_law_firms(self, law_firms: List[int]):
        """
        :param law_firms: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(law_firms, list):
            response = self._get(path='law-firms', params={"lawFirmIds": law_firms})
        else:
            response = self._get(path='law-firms', args=law_firms)
        return response.json()

    def search_law_firms(self, q: str, page_number: int = 1, page_size: int = 500) -> str:
        """
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        response = self._get(path='search-law-firms', params={"q": q,
                                                             "pageNumber": page_number,
                                                             "pageSize": page_size})
        return response.json()

    def get_federal_judges(self, federal_judges: List[int]) -> str:
        """
        :param federal_judges: provide a single value or a list of values
        :return: JSON string
        """
        if isinstance(federal_judges, list):
            response = self._get(path='federal-judges', params={"federalJudgeIds": federal_judges})
        else:
            response = self._get(path='federal-judges', args=federal_judges)
        return response.json()

    def get_magistrate_judges(self, magistrate_judges: str) -> str:
        response = self._get(path='magistrate-judges', args=magistrate_judges)
        return response.json()

    def search_judges(self, q: str) -> str:
        response = self._get(path='search-judges', params={"q": q})
        return response.json()

    def get_patents(self, patents: List[str]) -> str:
        """
        :param patents: provide a single value or a list of values
        :return: JSON
        """
        if isinstance(patents, list):
            response = self._get(path='patents', params={"patentNumbers": patents})
        else:
            response = self._get(path='patents', args=patents)
        return response.json()

    def list_case_resolutions(self) -> str:
        return self._list(path='list-case-resolutions')

    def list_case_tags(self) -> str:
        return self._list(path='list-case-tags')

    def list_case_types(self) -> str:
        return self._list(path='list-case-types')

    def list_courts(self) -> str:
        return self._list(path='list-courts')

    def list_damages(self) -> str:
        return self._list(path='list-damages')

    def list_events(self) -> str:
        return self._list(path='list-events')

    def list_judgment_sources(self) -> str:
        return self._list(path='list-judgment-sources')

    def _list(self, path):
        response = self._get(path=path)
        return response.json()

    def health(self):
        response = self._get(path="health")
        return response.text
    def open_api(self):
        response = self._get(path="openapi.json")
        return response.json()

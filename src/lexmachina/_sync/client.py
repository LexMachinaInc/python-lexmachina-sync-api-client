from typing import List

from .base_request import BaseRequest
from .query_district_cases import QueryDistrictCase


class LexMachinaClient(BaseRequest):
    def __init__(self, config_file_path=None, client_id=None, client_secret=None):
        super().__init__(config_file_path, client_id, client_secret)
        self._config_file_path = config_file_path
        self._client_id = client_id
        self._client_secret = client_secret
        self.query = QueryDistrictCase(config=self._config_file_path)

    def get_district_cases(self, cases: int) -> dict:
        """
        
        :param cases: int of a case ID
        :return: JSON case structure
        """
        return self._get(path='district-cases', args=cases).json()

    def get_state_cases(self, cases: int) -> dict:
        return self._get(path="state-cases", args=cases)

    def query_district_case(self, query, options=None, page_size=100):
        return self.query.query_district_case(query, options, page_size)

    def get_parties(self, parties: List[str]) -> dict:
        """

        :param parties: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(parties, list):
            response = self._get(path='parties', params={"partyIds": parties})
        else:
            response = self._get(path='parties', args=parties)
        return response.json()

    def search_parties(self, q: str, page_number: int = 1, page_size: int = 500) -> dict:
        """

        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        return self._get(path='search-parties', params={"q": q,
                                                            "pageNumber": page_number,
                                                            "pageSize": page_size}).json()

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

    def search_attorneys(self, q: str, page_number: int = 1, page_size: int = 500) -> dict:
        """
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        return self._get(path='search-attorneys', params={"q": q,
                                                              "pageNumber": page_number,
                                                              "pageSize": page_size}).json()

    def get_law_firms(self, law_firms: List[int]) -> dict:
        """
        :param law_firms: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(law_firms, list):
            response = self._get(path='law-firms', params={"lawFirmIds": law_firms})
        else:
            response = self._get(path='law-firms', args=law_firms)
        return response.json()

    def search_law_firms(self, q: str, page_number: int = 1, page_size: int = 500) -> dict:
        """
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        return self._get(path='search-law-firms', params={"q": q,
                                                              "pageNumber": page_number,
                                                              "pageSize": page_size}).json()

    def get_federal_judges(self, federal_judges: List[int]) -> dict:
        """
        :param federal_judges: provide a single value or a list of values
        :return: JSON string
        """
        if isinstance(federal_judges, list):
            response = self._get(path='federal-judges', params={"federalJudgeIds": federal_judges})
        else:
            response = self._get(path='federal-judges', args=federal_judges)
        return response.json()

    def get_magistrate_judges(self, magistrate_judges: str) -> dict:
        return self._get(path='magistrate-judges', args=magistrate_judges).json()

    def search_judges(self, q: str) -> dict:
        return  self._get(path='search-judges', params={"q": q}).json()

    def get_patents(self, patents: List[str]) -> dict:
        """
        :param patents: provide a single value or a list of values
        :return: JSON
        """
        if isinstance(patents, list):
            response = self._get(path='patents', params={"patentNumbers": patents})
        else:
            response = self._get(path='patents', args=patents)
        return response.json()

    def list_case_resolutions(self) -> dict:
        return self._list(path='list-case-resolutions')

    def list_case_tags(self) -> dict:
        return self._list(path='list-case-tags')

    def list_case_types(self) -> dict:
        return self._list(path='list-case-types')

    def list_courts(self) -> dict:
        return self._list(path='list-courts')

    def list_damages(self) -> dict:
        return self._list(path='list-damages')

    def list_events(self) -> dict:
        return self._list(path='list-events')

    def list_judgment_sources(self) -> dict:
        return self._list(path='list-judgment-sources')

    def _list(self, path) -> dict:
        return self._get(path=path).json()

    def health(self) -> str:
        return self._get(path="health").text

    def open_api(self) -> dict:
        return self._get(path="openapi.json").json()

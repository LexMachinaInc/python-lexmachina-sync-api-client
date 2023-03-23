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

    def get_district_cases(self, cases: int, version: str = "/") -> dict:
        """
        
        :param cases: int of a case ID
        :param version: str such as '/' or '/sandbox'
        :return: JSON case structure
        """
        response = self._get(path='district-cases', args=cases, version=version)
        return response.json()

    def query_district_case(self, query, options=None, page_size=100, version: str = "/"):
        return self.query.query_district_case(query, options, page_size, version)

    def get_parties(self, parties: List[str], version: str = "/") -> dict:
        """

        :param version: str value such as '/' or '/sandbox'
        :param parties: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(parties, list):
            response = self._get(path='parties', version=version, params={"partyIds": parties})
        else:
            response = self._get(path='parties', args=parties, version=version)
        return response.json()

    def search_parties(self, q: str, page_number: int = 1, page_size: int = 500, version: str = "/") -> dict:
        """

        :param version: str value such as '/' or '/sandbox'
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        response = self._get(path='search-parties', version=version, params={"q": q,
                                                            "pageNumber": page_number,
                                                            "pageSize": page_size})
        return response.json()

    def get_attorneys(self, attorneys: List[int], version: str = "/"):
        """
        :param version:  str value such as '/' or '/sandbox'
        :param attorneys: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(attorneys, list):
            response = self._get(path='attorneys', version=version, params={"attorneyIds": attorneys})
        else:
            response = self._get(path='attorneys', version=version, args=attorneys)
        return response.json()

    def search_attorneys(self, q: str, page_number: int = 1, page_size: int = 500, version: str = "/") -> dict:
        """
        :param version: str value such as '/' or '/sandbox'
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        response = self._get(path='search-attorneys', version=version, params={"q": q,
                                                              "pageNumber": page_number,
                                                              "pageSize": page_size})
        return response.json()

    def get_law_firms(self, law_firms: List[int], version: str = "/") -> dict:
        """
        :param version: str value such as '/' or '/sandbox'
        :param law_firms: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(law_firms, list):
            response = self._get(path='law-firms', version=version, params={"lawFirmIds": law_firms})
        else:
            response = self._get(path='law-firms', version=version, args=law_firms)
        return response.json()

    def search_law_firms(self, q: str, page_number: int = 1, page_size: int = 500, version: str = "/") -> dict:
        """
        :param version: str value such as '/' or '/sandbox'
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        response = self._get(path='search-law-firms', version=version, params={"q": q,
                                                              "pageNumber": page_number,
                                                              "pageSize": page_size})
        return response.json()

    def get_federal_judges(self, federal_judges: List[int], version: str = "/") -> dict:
        """
        :param version: str value such as '/' or '/sandbox'
        :param federal_judges: provide a single value or a list of values
        :return: JSON string
        """
        if isinstance(federal_judges, list):
            response = self._get(path='federal-judges', version=version, params={"federalJudgeIds": federal_judges})
        else:
            response = self._get(path='federal-judges', version=version, args=federal_judges)
        return response.json()

    def get_magistrate_judges(self, magistrate_judges: str, version: str = "/") -> dict:

        response = self._get(path='magistrate-judges', version=version, args=magistrate_judges)
        return response.json()

    def search_judges(self, q: str, version: str = "/") -> dict:

        response = self._get(path='search-judges', version=version, params={"q": q})
        return response.json()

    def get_patents(self, patents: List[str], version: str = "/") -> dict:
        """
        :param version: str value such as '/' or '/sandbox'
        :param patents: provide a single value or a list of values
        :return: JSON
        """
        if isinstance(patents, list):
            response = self._get(path='patents', version=version, params={"patentNumbers": patents})
        else:
            response = self._get(path='patents', version=version, args=patents)
        return response.json()

    def list_case_resolutions(self, version: str = "/") -> dict:
        return self._list(path='list-case-resolutions', version=version)

    def list_case_tags(self, version: str = "/") -> dict:
        return self._list(path='list-case-tags', version=version)

    def list_case_types(self, version: str = "/") -> dict:
        return self._list(path='list-case-types', version=version)

    def list_courts(self, version: str = "/") -> dict:
        return self._list(path='list-courts', version=version)

    def list_damages(self, version: str = "/") -> dict:
        return self._list(path='list-damages', version=version)

    def list_events(self, version: str = "/") -> dict:
        return self._list(path='list-events', version=version)

    def list_judgment_sources(self, version: str = "/") -> dict:
        return self._list(path='list-judgment-sources', version=version)

    def _list(self, path, version: str) -> dict:
        response = self._get(path=path, version=version)
        return response.json()

    def health(self, url, version: str = "/") -> str:
        response = self._get(path="health", version=version)
        return response.text

    def open_api(self, version: str = "/") -> dict:
        response = self._get(path="openapi.json", version=version)
        return response.json()

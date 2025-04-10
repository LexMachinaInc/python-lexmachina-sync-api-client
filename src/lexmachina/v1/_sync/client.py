from typing import List
import configparser

from .base_request import BaseRequest
from .query_cases import QueryCase


class LexMachinaClient(BaseRequest):
    def __init__(self, config_file_path=None, client_id=None, client_secret=None):
        super().__init__(config_file_path, client_id, client_secret)

        if config_file_path:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            client_id = config['CREDENTIALS']['client_id']
            client_secret = config['CREDENTIALS']['client_secret']

        self._config_file_path = config_file_path
        self._client_id = client_id
        self._client_secret = client_secret
        self.query = QueryCase(config=self._config_file_path)

    def get_district_cases(self, cases: int) -> dict:
        """

        :param cases: int of a case ID
        :return: JSON case structure
        """
        return self._get(path='district-cases', args=cases)

    def get_appeals_cases(self, cases: int) -> dict:
        return self._get(path='appeals-cases', args=cases)

    def get_state_cases(self, cases: int) -> dict:
        return self._get(path="state-cases", args=cases)

    def query_state_cases(self, query, options=None, page_size=100):
        return self.query.query_case(query=query, options=options, page_size=page_size, endpoint='state-cases')

    def query_district_case(self, query, options=None, page_size=100):
        return self.query.query_case(query=query, options=options, page_size=page_size, endpoint='district-cases')

    def query_appeals_case(self, query, options=None, page_size=100):
        return self.query.query_case(query=query, options=options, page_size=page_size, endpoint='appeals-cases')

    def get_parties(self, parties: List[str]) -> dict:
        """

        :param parties: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(parties, list):
            response = self._get(path='parties', params={"partyIds": parties})
        else:
            response = self._get(path='parties', args=parties)
        return response

    def search_parties(self, q: str, page_number: int = 1, page_size: int = 500) -> dict:
        """

        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        return self._get(path='search-parties', params={"q": q,
                                                        "pageNumber": page_number,
                                                        "pageSize": page_size})

    def get_attorneys(self, attorneys: List[int]):
        """
        :param attorneys: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(attorneys, list):
            response = self._get(path='attorneys', params={"attorneyIds": attorneys})
        else:
            response = self._get(path='attorneys', args=attorneys)
        return response

    def search_attorneys(self, q: str, page_number: int = 1, page_size: int = 500) -> dict:
        """
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        return self._get(path='search-attorneys', params={"q": q,
                                                          "pageNumber": page_number,
                                                          "pageSize": page_size})

    def get_law_firms(self, law_firms: list[int]) -> dict:
        """
        :param law_firms: provide a single value or a list of values
        :return: JSON string with a name and partyID
        """
        if isinstance(law_firms, list):
            response = self._get(path='law-firms', params={"lawFirmIds": law_firms})
        else:
            response = self._get(path='law-firms', args=law_firms)
        return response

    def search_law_firms(self, q: str, page_number: int = 1, page_size: int = 500) -> dict:
        """
        :param q: search string
        :param page_number: what page number to return
        :param page_size: how many results to return per page
        :return: JSON
        """
        return self._get(path='search-law-firms', params={"q": q,
                                                          "pageNumber": page_number,
                                                          "pageSize": page_size})

    def get_federal_judges(self, federal_judges: List[int]) -> dict:
        """
        :param federal_judges: provide a single value or a list of values
        :return: JSON string
        """
        if isinstance(federal_judges, list):
            response = self._get(path='federal-judges', params={"federalJudgeIds": federal_judges})
        else:
            response = self._get(path='federal-judges', args=federal_judges)
        return response

    def get_state_judges(self, state_judges: List[int]) -> dict:
        """
        :param state_judges: provide a single value or a list of values
        :return: JSON string
        """
        if isinstance(state_judges, list):
            response = self._get(path='state-judges', params={"stateJudgeIds": state_judges})
        else:
            response = self._get(path='state-judges', args=state_judges)
        return response

    def get_magistrate_judges(self, magistrate_judges: str) -> dict:
        return self._get(path='magistrate-judges', args=magistrate_judges)

    def search_judges(self, q: str) -> dict:
        return self._get(path='search-judges', params={"q": q})

    def get_patents(self, patents: List[str]) -> dict:
        """
        :param patents: provide a single value or a list of values
        :return: JSON
        """
        if isinstance(patents, list):
            response = self._get(path='patents', params={"patentNumbers": patents})
        else:
            response = self._get(path='patents', args=patents)
        return response

    def list_case_resolutions(self, court_type) -> dict:
        return self._list(path=f'list-case-resolutions/{court_type}')

    def list_case_tags(self, court_type) -> dict:
        return self._list(path=f'list-case-tags/{court_type}')

    def list_case_types(self, court_type) -> dict:
        return self._list(path=f'list-case-types/{court_type}')

    def list_courts(self, court_type) -> dict:
        return self._list(path=f'list-courts/{court_type}')

    def list_damages_federal_district(self) -> dict:
        return self._list(path='list-damages/FederalDistrict')

    def list_damages_state(self) -> dict:
        return self._list(path='list-damages/State')

    def list_events(self, court_type) -> dict:
        return self._list(path=f'list-events/{court_type}')

    def list_federal_district_judgment_sources(self) -> dict:
        return self._list(path='list-judgment-sources/FederalDistrict')

    def list_state_judgment_events(self) -> dict:
        return self._list(path='list-judgment-events/State')

    def list_originating_venues_federal(self):
        return self._list(path='list-originating-venues/FederalAppeals')

    def list_appellate_decisions_federal(self):
        return self._list(path='list-appellate-decisions/FederalDistrict')

    def list_supreme_court_decisions_federal(self):
        return self._list(path='list-supreme-court-decisions/FederalAppeals')

    def _list(self, path) -> dict:
        return self._get(path=path)

    def health(self) -> str:
        return self._get(path="health")

    def open_api(self) -> dict:
        return self._get(path="openapi.json")
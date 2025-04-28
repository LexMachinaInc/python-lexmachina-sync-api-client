from typing import List
import configparser

from .base_request import BaseRequest
from .query_cases import QueryCase


class LexMachinaAsyncClient(BaseRequest):
    def __init__(self, config_file_path=None, client_id=None, client_secret=None):
        if config_file_path:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            client_id = config['CREDENTIALS']['client_id']
            client_secret = config['CREDENTIALS']['client_secret']

        super().__init__(config_file_path, client_id, client_secret)
        self._config_file_path = config_file_path
        self._client_id = client_id
        self._client_secret = client_secret
        self.query = QueryCase(config=self._config_file_path)

    async def get_district_cases(self, cases: int):
        return await self._get(path='district-cases', args=cases)

    async def get_state_cases(self, cases: int) -> dict:
        return await self._get(path="state-cases", args=cases)


    async def get_appeals_cases(self, cases: int) -> dict:
        return await self._get(path='appeals-cases', args=cases)
    async def query_state_cases_case(self, query, options=None, page_size=100):
        return await self.query.query_case(query=query, options=options, page_size=page_size, endpoint='state-cases')

    async def query_district_case(self, query, options=None, page_size=100):
        return await self.query.query_case('district-cases', query, options, page_size)

    async def query_appeals_case(self, query, options=None, page_size=100):
        return await self.query.query_case('appeals-cases', query, options, page_size)

    async def get_parties(self, parties: List[str]):
        if isinstance(parties, list):
            response = await self._get(path='parties', params={"partyIds": parties})
        else:
            response = await self._get(path='parties', args=parties)
        return response

    async def search_parties(self, q: str, page_number: int = 1, page_size: int = 500):
        return await self._get(path='search-parties', params={"q": q,
                                                              "pageNumber": page_number,
                                                              "pageSize": page_size})

    async def get_attorneys(self, attorneys: List[int]):
        if isinstance(attorneys, list):
            response = await self._get(path='attorneys', params={"attorneyIds": attorneys})
        else:
            response = await self._get(path='attorneys', args=attorneys)
        return response

    async def search_attorneys(self, q: str, page_number: int = 1, page_size: int = 500):
        response = await self._get(path='search-attorneys', params={"q": q,
                                                                    "pageNumber": page_number,
                                                                    "pageSize": page_size})
        return response

    async def get_law_firms(self, law_firms: List[int]):
        if isinstance(law_firms, list):
            response = await self._get(path='law-firms', params={"lawFirmIds": law_firms})
        else:
            response = await self._get(path='law-firms', args=law_firms)
        return response

    async def search_law_firms(self, q: str, page_number: int = 1, page_size: int = 500):
        return await self._get(path='search-law-firms', params={"q": q,
                                                                "pageNumber": page_number,
                                                                "pageSize": page_size})

    async def get_federal_judges(self, federal_judges: List[int]):
        if isinstance(federal_judges, list):
            response = await self._get(path='federal-judges', params={"federalJudgeIds": federal_judges})
        else:
            response = await self._get(path='federal-judges', args=federal_judges)
        return response

    async def get_state_judges(self, state_judges: List[int]):
        if isinstance(state_judges, list):
            response = await self._get(path='state-judges', params={"stateJudgeIds": state_judges})
        else:
            response = await self._get(path='state-judges', args=state_judges)
        return response

    async def get_magistrate_judges(self, magistrate_judges: str):
        return await self._get(path='magistrate-judges', args=magistrate_judges)

    async def search_judges(self, q: str):
        return await self._get(path='search-judges', params={"q": q})

    async def get_patents(self, patents: List[str]):
        if isinstance(patents, list):
            response = await self._get(path='patents', params={"patentNumbers": patents})
        else:
            response = await self._get(path='patents', args=patents)
        return response

    async def list_case_resolutions(self, court_type):
        return await self._list(path=f'list-case-resolutions/{court_type}')

    async def list_case_tags(self, court_type):
        return await self._list(path=f'list-case-tags/{court_type}')

    async def list_case_types(self, court_type):
        return await self._list(path=f'list-case-types/{court_type}')

    async def list_courts(self, court_types):
        return await self._list(path=f'list-courts/{court_types}')

    async def list_damages_federal(self):
        return await self._list(path='list-damages/FederalDistrict')

    async def list_damages_state(self):
        return await self._list(path='list-damages/State')


    async def list_events(self, court_type):
        return await self._list(path=f'list-events/{court_type}')

    async def list_judgment_sources_federal(self):
        return await self._list(path='list-judgment-sources/FederalDistrict')

    async def list_judgment_events_state(self):
        return await self._list(path='list-judgment-events/State')

    async def list_originating_venues_federal(self):
        return await self._list(path='list-originating-venues/FederalAppeals')

    async def list_appellate_decisions_federal(self):
        return await self._list(path='list-appellate-decisions/FederalDistrict')

    async def list_supreme_court_decisions_federal(self):
        return await self._list(path='list-supreme-court-decisions/FederalAppeals')

    async def _list(self, path):
        return await self._get(path=path)

    async def health(self):
        return await self._get(path="health")
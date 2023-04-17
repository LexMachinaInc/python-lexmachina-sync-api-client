from typing import List

from .base_request import BaseRequest
from .query_district_cases import QueryDistrictCase


class LexMachinaAsyncClient(BaseRequest):
    def __init__(self, config_file_path=None, client_id=None, client_secret=None):
        super().__init__(config_file_path, client_id, client_secret)
        self._config_file_path = config_file_path
        self._client_id = client_id
        self._client_secret = client_secret
        self.query = QueryDistrictCase(config=self._config_file_path)

    async def get_district_cases(self, cases: int):
        return await self._get(path='district-cases', args=cases)

    async def get_state_cases(self, cases: int) -> dict:
        return await self._get(path="state-cases", args=cases)

    async def query_district_case(self, query, options=None, page_size=100):
        return await self.query.query_district_case(query, options, page_size)

    async def get_parties(self, parties: List[str]):
        if isinstance(parties, list):
            response = await self._get(path='parties', params={"partyIds": parties})
        else:
            response = await self._get(path='parties', args=parties)
        return await response

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

    async def list_case_resolutions(self):
        return await self._list(path='list-case-resolutions')

    async def list_case_tags(self):
        return await self._list(path='list-case-tags')

    async def list_case_types(self):
        return await self._list(path='list-case-types')

    async def list_courts(self):
        return await self._list(path='list-courts')

    async def list_damages(self):
        return await self._list(path='list-damages')

    async def list_events(self):
        return await self._list(path='list-events')

    async def list_judgment_sources(self):
        return await self._list(path='list-judgment-sources')

    async def _list(self, path):
        return await self._get(path=path)

    async def health(self):
        return await self._get(path="health")

from .base_request import BaseRequest


class QueryDistrictCase:
    def __init__(self, config=None):
        self.district_case_query = BaseRequest(config)

    async def query_one_page(self, query):
        response = await self.district_case_query._post(path="query-district-cases", data=query)
        if response:
            return response.get("caseIds")
        return []

    async def query_all_pages(self, query, page_size):
        cases = []
        if page_size > 100:
            raise ValueError("Page size must be <= 100")
        query.set_page_size(page_size)
        query_results = query.execute()
        while True:
            page_cases = await self.query_one_page(query_results)
            if page_cases:
                cases.extend(page_cases)
                query.next_page()
            if not page_cases:
                break
        return cases

    async def query_district_case(self, query, options, page_size):
        query_results = query.execute()
        if options and options['pageThrough']:
            return await self.query_all_pages(query, page_size)
        else:
            return await self.query_one_page(query_results)

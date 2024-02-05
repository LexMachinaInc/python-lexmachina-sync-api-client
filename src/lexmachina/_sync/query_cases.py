from .base_request import BaseRequest


class QueryCase:
    def __init__(self, config=None):
        self.case_query = BaseRequest(config)

    def query_one_page(self, query, endpoint):
        if endpoint == 'district-cases':
            response = self.case_query._post(path="query-district-cases", data=query)
        elif endpoint == 'state-cases':
            response = self.case_query._post(path="query-state-cases", data=query)
        elif endpoint == 'appeals-cases':
            response = self.case_query._post(path="query-appeals-cases", data=query)
        if response:
            return response.get("cases")
        return []

    def query_all_pages(self, query, endpoint, page_size):
        cases = []
        if page_size > 100:
            raise ValueError("Page size must be <= 100")
        query.set_page_size(page_size)
        query_results = query.execute()
        while True:
            page_cases = self.query_one_page(query_results, endpoint)
            if page_cases:
                cases.extend(page_cases)
                query.next_page()
            if not page_cases:
                break
        return cases

    def query_case(self, query, endpoint, options, page_size):
        query_results = query.execute()
        if options and options['pageThrough']:
            return self.query_all_pages(query, endpoint, page_size)
        else:
            return self.query_one_page(query_results, endpoint)

from .base_request import BaseRequest


class QueryDistrictCase:
    def __init__(self, config=None):
        self.district_case_query = BaseRequest(config)

    def query_one_page(self, query):
        response = self.district_case_query.post(path="/query-district-cases", data=query)
        if response:
            return response.get("caseIds")
        return []

    def query_all_pages(self, query):
        query_results = query.execute()
        cases = []
        query.set_page_size(10)
        while True:
            page_cases = self.query_one_page(query_results)
            cases.extend(page_cases)
            query.next_page()
            if not page_cases:
                break
        return cases

    def query_district_case(self, query, options):
        query_results = query.execute()
        if options and options['pageThrough']:
            return self.query_all_pages(query)
        else:
            return self.query_one_page(query_results)




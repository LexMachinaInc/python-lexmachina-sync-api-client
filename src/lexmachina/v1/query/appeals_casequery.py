from datetime import datetime


def empty(x):
    return x is None or x == {} or x == [] or x == ''

class AppealsCaseQueryRequest:

    def __init__(self):
        self._query_template = {
                "courts": {
                    "include": [
                    ],
                    "exclude": [
                    ]
                },
                "caseStatus": "",
                "caseTags": {
                    "include": [
                    ],
                    "exclude": [
                    ]
                },
                "dates": {
                    "filed": {
                        "onOrAfter": "",
                        "onOrBefore": ""
                    },
                    "terminated": {
                        "onOrAfter": "",
                        "onOrBefore": ""
                    },
                    "lastDocket": {
                        "onOrAfter": "",
                        "onOrBefore": ""
                    }
                },
                "judges": {
                    "include": [
                    ],
                    "exclude": [
                    ]
                },
                "lawFirms": {
                    "include": [
                    ],
                    "exclude": [
                    ],
                    "includeAppellant": [
                    ],
                    "excludeAppellant": [
                    ],
                    "includeAppellee": [
                    ],
                    "excludeAppellee": [
                    ],
                    "includeRespondent": [
                    ],
                    "excludeRespondent": [
                    ],
                    "includeThirdParty": [
                    ],
                    "excludeThirdParty": [
                    ],
                    "includePetitionerMovant": [
                    ],
                    "excludePetitionerMovant": [
                    ]
                },
                "attorneys": {
                    "include": [
                    ],
                    "exclude": [
                    ],
                    "includeAppellant": [
                    ],
                    "excludeAppellant": [
                    ],
                    "includeAppellee": [
                    ],
                    "excludeAppellee": [
                    ],
                    "includeRespondent": [
                    ],
                    "excludeRespondent": [
                    ],
                    "includeThirdParty": [
                    ],
                    "excludeThirdParty": [
                    ],
                    "includePetitionerMovant": [
                    ],
                    "excludePetitionerMovant": [
                    ]
                },
                "parties": {
                    "include": [
                    ],
                    "exclude": [
                    ],
                    "includeAppellant": [
                    ],
                    "excludeAppellant": [
                    ],
                    "includeAppellee": [
                    ],
                    "excludeAppellee": [
                    ],
                    "includeRespondent": [
                    ],
                    "excludeRespondent": [
                    ],
                    "includeThirdParty": [
                    ],
                    "excludeThirdParty": [
                    ],
                    "includePetitionerMovant": [
                    ],
                    "excludePetitionerMovant": [
                    ]
                },
                "originatingVenues": {
                    "include": [
                    ],
                    "exclude": [
                    ]
                },
                "originatingCases": {
                    "includeDistrictCaseIds": [
                    ],
                    "excludeDistrictCaseIds": [
                    ],
                    "includeOriginatingJudges": {
                        "districtFederalJudges": {
                            "include": [
                            ],
                            "exclude": [
                            ]
                        }
                    },
                    "originatingDistrictCaseCriteria": {
                        "courts": {
                            "include": [
                            ],
                            "exclude": [
                            ]
                        },
                        "caseTypes": {
                            "include": [
                            ],
                            "exclude": [
                            ]
                        }
                    }
                },
                "resolutions": {
                    "include": [
                    ],
                    "exclude": [
                    ]
                },
                "supremeCourtDecisions": {
                    "include": [
                    ],
                    "exclude": [
                    ]
                },
                "ordering": "ByFirstFiled",
                "page": 1,
                "pageSize": 5
            }

    def _remove_empty_elements(self, data):
        if not isinstance(data, dict) and not isinstance(data, list):
            return data
        elif isinstance(data, list):
            return [v for v in (self._remove_empty_elements(v) for v in data) if not empty(v)]
        else:
            return {k: v for k, v in ((k, self._remove_empty_elements(v)) for k, v in data.items()) if not empty(v)}

    def validate_date(self, date):
        try:
            datetime.fromisoformat(date)
        except ValueError:
            raise ValueError("Incorrect date format, dates should be 'YYYY-MM-DD'")
        return True

    def set_date(self, date, field, operator):
        '''

        :param date: provide a date in iso format: 2023-01-01
        :param field: examples include 'onOrAfter', 'onOrBefore,
        :param operator: choose from 'filed', 'terminated', 'trial', 'lastDocket'
        :return:
        '''
        valid_date = self.validate_date(date)
        if isinstance(field, str):
            new_field = self._query_template['dates'][field]
            if valid_date:
                new_field[operator] = date
        else:
            new_field = field
        if valid_date:
            new_field[operator] = date

        return self

    def set_page(self, page):
        self._query_template['page'] = page
        return self

    def next_page(self):
        self._query_template['page'] += 1
        return self

    def set_page_size(self, size):
        self._query_template['pageSize'] = size
        return self

    def get_page(self):
        return self._query_template['page']

    def include_courts(self, *args):
        """
        :param args: include an arbitrary number of court ids
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        """
        [self._query_template['courts']['include'].append(value) for value in args]
        return self

    def exclude_courts(self, *args):
        '''
        :param args: exclude an arbitrary number of court ids
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['courts']['exclude'].append(value) for value in args]
        return self

    def include_resolutions(self, summary, specific):
        """
        :param summary: Include a resolution summary
        :param specific: Include specific resolution info
        These can be found with the '/list-case-resolutions endpoint.
        This function can be chained with other functions
        :return: CaseQueryRequest object
        """
        resolution = {"summary": summary, "specific": specific}
        self._query_template['resolutions']['include'].append(resolution)
        return self

    def exclude_resolutions(self, summary, specific):
        """
        :param summary: Exclude a resolution summary
        :param specific: Exclude specific resolution info
        These can be found with the '/list-case-resolutions endpoint.
        This function can be chained with other functions
        :return: CaseQueryRequest object
        """
        resolution = {"summary": summary, "specific": specific}
        self._query_template['resolutions']['exclude'].append(resolution)
        return self

    def include_judges(self, *args):
        '''
        :param args: include an arbitrary number of judge ids
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['judges']['include'].append(value) for value in args]
        return self

    def exclude_judges(self, *args):
        '''
        :param args: exclude an arbitrary number of judge ids
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['judges']['exclude'].append(value) for value in args]
        return self


    def include_law_firms(self, *args):
        '''
         :param args: include an arbitrary number of lawfirm ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['lawFirms']['include'].append(value) for value in args]

        return self

    def exclude_law_firms(self, *args):
        '''
         :param args: exclude an arbitrary number of lawfirm ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['lawFirms']['exclude'].append(value) for value in args]
        return self

    def lawfirms_include_plaintiffs(self, *args):
        '''
         :param args: include an arbitrary number of plaintiff ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['lawFirms']['includePlaintiff'].append(value) for value in args]
        return self

    def lawfirms_exclude_plaintiffs(self, *args):
        '''
         :param args: exclude an arbitrary number of plaintiff ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['lawFirms']['excludePlaintiff'].append(value) for value in args]
        return self

    def lawfirms_include_defendant(self, *args):
        '''
         :param args: include an arbitrary number of defendant ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['lawFirms']['includeDefendant'].append(value) for value in args]
        return self

    def lawfirms_exclude_defendant(self, *args):
        '''
         :param args: exclude an arbitrary number of defendant ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['lawfirms']['excludeDefendant'].append(value) for value in args]
        return self

    def lawfirms_include_third_party(self, *args):
        '''
         :param args: include an arbitrary number of third party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['lawFirms']['includeThirdParty'].append(value) for value in args]
        return self

    def lawfirms_exclude_third_party(self, *args):
        '''
         :param args: exclude an arbitrary number of third party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['lawFirms']['excludeThirdParty'].append(value) for value in args]
        return self

    def include_parties(self, *args):
        '''
         :param args: include an arbitrary number of party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['parties']['include'].append(value) for value in args]
        return self

    def exclude_parties(self, *args):
        '''
         :param args: exclude an arbitrary number of party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['parties']['exclude'].append(value) for value in args]
        return self

    def parties_include_plaintiff(self, *args):
        '''
         :param args: include an arbitrary number of plaintiff party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['parties']['includePlaintiff'].append(value) for value in args]
        return self

    def parties_exclude_plaintiff(self, *args):
        '''
         :param args: exclude an arbitrary number of plaintiff party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''

        [self._query_template['parties']['excludePlaintiff'].append(value) for value in set(args)]
        return self

    def parties_include_defendant(self, *args):
        '''
         :param args: include an arbitrary number of defendant party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['parties']['includeDefendant'].append(value) for value in args]
        return self

    def parties_exclude_defendant(self, *args):
        '''
         :param args: exclude an arbitrary number of defendant party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['parties']['excludeDefendant'].append(value) for value in args]
        return self

    def parties_include_third_party(self, *args):
        """
         :param args: include an arbitrary number of third-party party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         """
        [self._query_template['parties']['includeThirdParty'].append(value) for value in args]
        return self

    def parties_exclude_third_party(self, *args):
        """
         :param args: exclude an arbitrary number of third-party party ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         """

        [self._query_template['parties']['excludeThirdParty'].append(value) for value in args]
        return self

    def parties_include_petitioner_movant(self, *args):
        [self._query_template['parties']['includePetitionerMovant'].append(value) for value in args]
        return self


    def parties_exclude_petitioner_movant(self, *args):
        [self._query_template['parties']['excludePetitionerMovant'].append(value) for value in args]
        return self

    def include_originating_venues(self, *args):
        [self._query_template['originatingVenues']['include'].append(value) for value in args]
        return self

    def exclude_originating_venues(self, *args):
        [self._query_template['originatingVenues']['exclude'].append(value) for value in args]
        return self

    def include_originating_cases(self, *args):
        [self._query_template['originatingCases']['includeDistrictCaseIds'].append(value) for value in args]
        return self

    def exclude_originating_cases(self, *args):
        [self._query_template['originatingCases']['excludeDistrictCaseIds'].append(value) for value in args]
        return self

    def include_originating_judges(self, *args):
        [self._query_template['originatingCases']['includeOriginatingJudges']['districtFederalJudges']['include'].append(
            value) for value in args]
        return self

    def exclude_originating_judges(self, *args):
        [self._query_template['originatingCases']['includeOriginatingJudges']['districtFederalJudges']['exclude'].append(
            value) for value in args]
        return self

    def include_originating_district_case_courts(self, *args):
        [self._query_template['originatingCases']['originatingDistrictCaseCriteria']['courts']['include'].append(value) for
         value in args]
        return self

    def exclude_originating_district_case_courts(self, *args):
        [self._query_template['originatingCases']['originatingDistrictCaseCriteria']['courts']['exclude'].append(value) for
         value in args]
        return self

    def include_originating_district_case_types(self, *args):
        [self._query_template['originatingCases']['originatingDistrictCaseCriteria']['caseTypes']['include'].append(value) for
         value in args]
        return self

    def exclude_originating_district_case_types(self, *args):
        [self._query_template['originatingCases']['originatingDistrictCaseCriteria']['caseTypes']['exclude'].append(value) for
        value in args]
        return self

    def execute(self):
        self._query_template = self._remove_empty_elements(self._query_template)
        return self._query_template
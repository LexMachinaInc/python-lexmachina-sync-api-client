from datetime import datetime


def empty(x):
    return x is None or x == {} or x == [] or x == ''


class DistrictCaseQueryRequest:
    def __init__(self):
        self._query_template = {
            'caseStatus': '',
            "caseTypes": {"include": [], "exclude": []},
            'caseTags': {'include': [], 'exclude': []},
            "dates": {
                "filed": {"onOrAfter": "", "onOrBefore": ""},
                'terminated': {'onOrAfter': '', 'onOrBefore': ''},
                'trial': {'onOrAfter': '', 'onOrBefore': ''},
                'lastDocket': {'onOrAfter': '', 'onOrBefore': ''}
            },
            'judges': {'include': [], 'exclude': []},
            'magistrates': {'include': [], 'exclude': []},
            'events': {'include': [], 'exclude': []},
            'lawFirms': {'include': [], 'exclude': [], 'includePlaintiff': [], 'excludePlaintiff': [],
                         'includeDefendant': [], 'excludeDefendant': [], 'includeThirdParty': [],
                         'excludeThirdParty': []},
            'parties': {'include': [], 'exclude': [], 'includePlaintiff': [], 'excludePlaintiff': [],
                        'includeDefendant': [], 'excludeDefendant': [], 'includeThirdParty': [],
                        'excludeThirdParty': []},
            'courts': {'include': [], 'exclude': []},
            'resolutions': {'include': [], 'exclude': []},
            'findings': [{'judgmentSource': {'include': [], 'exclude': []}, 'nameType': {'include': [], 'exclude': []},
                          'date': {'onOrAfter': '', 'onOrBefore': ''}, 'awardedToParties': [],
                          'awardedAgainstParties': [], 'patentInvalidityReasons': {'include': []}}],
            'remedies': [{'judgmentSource': {'include': [], 'exclude': []}, 'nameType': {'include': [], 'exclude': []},
                          'date': {'onOrAfter': '', 'onOrBefore': ''}, 'awardedToParties': [],
                          'awardedAgainstParties': []}],
            'damages': [{'judgmentSource': {'include': [], 'exclude': []}, 'nameType': {'include': [], 'exclude': []},
                         'date': {'onOrAfter': '', 'onOrBefore': ''}, 'awardedToParties': [],
                         'awardedAgainstParties': [], 'minimumAmount': ''}],
            'patents': {'include': [], 'exclude': []},
            'mdl': {'include': [], 'exclude': []},
            'ordering': 'ByFirstFiled',
            'page': 1,
            'pageSize': 5
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

    def include_case_types(self, *args):
        '''
        :param args: include an arbitrary number of case types
        list of case types can be found using the /list-case-types endpoint.
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['caseTypes']['include'].append(value) for value in args]
        return self

    def exclude_case_types(self, *args):
        '''
        :param args: exclude an arbitrary number of case types
        list of case types can be found using the /list-case-types endpoint.
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['caseTypes']['exclude'].append(value) for value in args]
        return self

    def include_case_tags(self, *args):
        '''
        :param args: include an arbitrary number of case tags
        list of case tags can be found using the /list-case-tags endpoint.
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['caseTags']['include'].append(value) for value in args]
        return self

    def exclude_case_tags(self, *args):
        '''
        :param args: exclude an arbitrary number of case tags
        list of case tags can be found using the /list-case-tags endpoint.
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['caseTags']['exclude'].append(value) for value in args]
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

    def include_courts(self, *args):
        """
        :param args: include an arbitrary number of court ids
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        """
        [self._query_template['courts']['include'].append(value) for value in args]
        return self

    def exclude_courts(self, *args):
        """
        :param args: exclude an arbitrary number of court ids
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        """
        [self._query_template['courts']['exclude'].append(value) for value in args]
        return self

    def include_magistrates(self, *args):
        '''
        :param args: include an arbitrary number of magistrate ids
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['magistrates']['include'].append(value) for value in args]
        return self

    def exclude_magistrates(self, *args):
        '''
        :param args: exclude an arbitrary number of magistrate ids
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['magistrates']['exclude'].append(value) for value in args]
        return self

    def include_event_types(self, *args):
        '''
        :param args: include an arbitrary number of event types.
        These types can be found with the '/list-events' endpoint
        This function can be chained with other functions.
        :return: CaseQueryRequest object
        '''
        [self._query_template['events']['include'].append(value) for value in args]
        return self

    def exclude_event_types(self, *args):
        '''
         :param args: exclude an arbitrary number of event types.
         These types can be found with the '/list-events' endpoint
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         '''
        [self._query_template['events']['exclude'].append(value) for value in args]
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

    def findings_include_awarded_to_parties(self, *args):
        """
           :param args: include an arbitrary number of party ids.
           This function can be chained with other functions.
           :return: CaseQueryRequest object
           """
        [self._query_template['findings'][0]['awardedToParties'].append(value) for value in args]
        return self

    def findings_includes_awarded_against_parties(self, *args):
        """
           :param args: exclude an arbitrary number of party ids.
           This function can be chained with other functions.
           :return: CaseQueryRequest object
           """
        [self._query_template['findings'][0]['awardedAgainstParties'].append(value) for value in args]
        return self

    def findings_include_judgment_source(self, *args):
        """
           :param args: include an arbitrary number of judgment source ids.
           This function can be chained with other functions.
           :return: CaseQueryRequest object
           """
        [self._query_template['findings'][0]['judgmentSource']['include'].append(value) for value in args]
        return self

    def findings_exclude_judgment_source(self, *args):
        """
           :param args: exclude an arbitrary number of third-party party ids.
           This function can be chained with other functions.
           :return: CaseQueryRequest object
           """
        [self._query_template['findings'][0]['judgmentSource']['exclude'].append(value) for value in args]
        return self

    def findings_include_patent_invalidity_reasons(self, *args):
        [self._query_template['findings'][0]['patentInvalidityReasons']['include'].append(value) for value in args]
        return self

    def include_remedies_awarded_to_parties(self, *args):
        [self._query_template['remedies'][0]['awardedToParties'].append(value) for value in args]
        return self

    def include_remedies_awarded_against_parties(self, *args):
        [self._query_template['remedies'][0]['awardedAgainstParties'].append(value) for value in args]
        return self

    def include_remedies_judgment_source(self, *args):
        [self._query_template['remedies'][0]['judgmentSource']['include'].append(value) for value in args]
        return self

    def exclude_remedies_judgment_source(self, *args):
        [self._query_template['remedies'][0]['judgmentSource']['exclude'].append(value) for value in args]
        return self

    def include_remedies_name_type(self, name, type):
        name_type = {'name': name, 'type': type}
        self._query_template['remedies'][0]['nameType']['include'].append(name_type)
        return self

    def exclude_remedies_name_type(self, name, type):
        name_type = {'name': name, 'type': type}
        self._query_template['remedies'][0]['nameType']['exclude'].append(name_type)
        return self

    def add_remedies_date(self, date, operator):
        """
        :param date: date in format YYYY-MM-DD
        :param operator: options are onOrBefore or onOrAfter. Choose to set date to either value.
        :return: CaseQueryRequest
        """
        self.set_date(date, self._query_template['remedies'][0]['date'], operator)
        return self

    def set_damages_minimum_amount(self, amount):
        """
        :param amount: provide a minimum amount of damages.
        This function can be chained with other functions
        :return: CaseQueryRequest
        """
        if amount <= 0 or isinstance(amount, str):
            raise ValueError("Damages amount must be a number greater than 0")
        self._query_template['damages'][0]['minimumAmount'] = amount
        return self

    def include_patents(self, *args):
        """
         :param args: include an arbitrary number of patent ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         """
        [self._query_template['patents']['include'].append(value) for value in args]
        return self

    def exclude_patents(self, *args):
        """
         :param args: exclude an arbitrary number of patent ids.
         This function can be chained with other functions.
         :return: CaseQueryRequest object
         """
        [self._query_template['patents']['exclude'].append(value) for value in args]
        return self

    def include_mdl(self, *args):
        [self._query_template['mdl']['include'].append(value) for value in args]
        return self

    def exclude_mdl(self, *args):
        [self._query_template['mdl']['exclude'].append(value) for value in args]
        return self

    def execute(self):
        self._query_template = self._remove_empty_elements(self._query_template)
        return self._query_template

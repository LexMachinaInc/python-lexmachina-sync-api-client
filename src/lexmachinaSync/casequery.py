import datetime

from .base_request import BaseRequest
from datetime import datetime


def empty(x):
    return x is None or x == {} or x == [] or x == ''


class CaseQueryRequest(dict):
    def __init__(self):
        super().__init__()
        self.query_template = {
            'caseStatus': '',
            'caseTypes': {'include': [], 'exclude': []},
            'caseTags': {'include': [], 'exclude': []},
            'dates': {
                'filed': {'onOrAfter': '', 'onOrBefore': ''},
                'terminated': {'onOrAfter': '', 'onOrBefore': ''},
                'trial': {'onOrAfter': '', 'onOrBefore': ''},
                'lastDocket': {'onOrAfter': '', 'onOrBefore': ''}
            },
            'judges': {'include': [], 'exclude': []},
            'magistrates': {'include': [], 'exclude': []},
            'events': {'includeEventTypes': [], 'excludeEventTypes': []},
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
                         'awardedAgainstParties': [], 'minimumAmount': 0}],
            'patents': {'include': [], 'exclude': []},
            'mdl': {'include': [], 'exclude': []},
            'ordering': 'ByFirstFiled',
            'page': 1,
            'pageSize': 5
        }

    def remove_empty_elements(self, data):
        if not isinstance(data, dict) and not isinstance(data, list):
            return data
        elif isinstance(data, list):
            return [v for v in (self.remove_empty_elements(v) for v in data) if not empty(v)]
        else:
            return {k: v for k, v in ((k, self.remove_empty_elements(v)) for k, v in data.items()) if not empty(v)}

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
            new_field = self.query_template['dates'][field]
            if valid_date:
                new_field[operator] = date
        else:
            new_field = field
        if valid_date:
            new_field[operator] = date

        return self

    def set_page(self, page):
        self.query_template['page'] = page
        return self

    def next_page(self):
        self.query_template['page'] += 1
        return self

    def set_page_size(self, size):
        self.query_template['pageSize'] = size
        return self

    def include_case_types(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['caseTypes']['include'].append(value)
        else:
            self.query_template['caseTypes']['include'].append(args)
        return self

    def include_case_tags(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['caseTags']['include'].append(value)
        else:
            self.query_template['caseTags']['include'].append(args)
        return self

    def include_judges(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['judges']['include'].append(value)
        else:
            self.query_template['judges']['include'].append(args)
        return self

    def exclude_judges(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['judges']['exclude'].append(value)
        else:
            self.query_template['judges']['exclude'].append(args)
        return self

    def include_courts(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['courts']['include'].append(value)
        else:
            self.query_template['courts']['include'].append(args)
        return self

    def exclude_courts(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['courts']['exclude'].append(value)
        else:
            self.query_template['courts']['exclude'].append(args)
        return self

    def include_magistrates(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['magistrates']['include'].append(value)
        else:
            self.query_template['magistrates']['include'].append(args)

    def exclude_magistrates(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['magistrates']['exclude'].append(value)
        else:
            self.query_template['magistrates']['exclude'].append(args)
        return self

    def include_event_types(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['events']['includeEventTypes'].append(value)
        else:
            self.query_template['events']['includeEventTypes'].append(args)
        return self

    def exclude_event_types(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['events']['excludeEventTypes'].append(value)
        else:
            self.query_template['events']['excludeEventTypes'].append(args)
        return self

    def include_law_firms(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['lawFirms']['include'].append(value)
        else:
            self.query_template['lawFirms']['include'].append(args)

        return self

    def exclude_law_firms(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['lawFirms']['exclude'].append(value)
        else:
            self.query_template['lawFirms']['exclude'].append(args)
        return self

    def lawfirms_include_plantiffs(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['lawFirms']['includePlaintiff'].append(value)
        else:
            self.query_template['lawFirms']['includePlaintiff'].append(args)
        return self

    def lawfirms_exclude_plantiffs(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['lawFirms']['excludePlaintiff'].append(value)
        else:
            self.query_template['lawFirms']['excludePlaintiff'].append(args)
        return self

    def lawfirms_include_defendent(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['lawFirms']['includeDefendant'].append(value)
        else:
            self.query_template['lawFirms']['includeDefendant'].append(args)
        return self

    def lawfirms_exclude_defendant(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['lawfirms']['excludeDefendant'].append(value)
        else:
            self.query_template['lawfirms']['excludeDefendant'].append(args)
        return self

    def lawfirms_include_third_party(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['lawFirms']['includeThirdParty'].append(value)
        else:
            self.query_template['lawFirms']['includeThirdParty'].append(args)
        return self

    def lawfirms_exclude_third_party(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['lawFirms']['excludeThirdParty'].append(value)
        else:
            self.query_template['lawFirms']['excludeThirdParty'].append(args)
        return self

    def include_parties(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['parties']['include'].append(value)
        else:
            self.query_template['parties']['include'].append(args)
        return self

    def exclude_parties(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['parties']['exclude'].append(value)
        else:
            self.query_template['parties']['exclude'].append(args)
        return self

    def parties_include_plantiff(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['parties']['includePlaintiff'].append(value)
        else:
            self.query_template['parties']['includePlaintiff'].append(args)
        return self

    def parties_exclude_plantiff(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['parties']['excludePlaintiff'].append(value)
        else:
            self.query_template['parties']['excludePlaintiff'].append(args)
        return self

    def parties_include_defendant(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['parties']['includeDefendant'].append(value)
        else:
            self.query_template['parties']['includeDefendant'].append(args)
        return self

    def parties_exclude_defendant(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['parties']['excludeDefendant'].append(value)
        else:
            self.query_template['parties']['excludeDefendant'].append(args)
        return self

    def parties_include_third_party(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['parties']['includeThirdParty'].append(value)
        else:
            self.query_template['parties']['includeThirdParty'].append(args)
        return self

    def parties_exclude_third_party(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['parties']['excludeThirdParty'].append(value)
        else:
            self.query_template['parties']['excludeThirdParty'].append(args)
        return self

    def include_resolutions(self, summary, specific):
        resolution = {"summary": summary, "specific": specific}
        self.query_template['resolutions']['include'].append(resolution)
        return self

    def exclude_resolutions(self, summary, specific):
        resolution = {"summary": summary, "specific": specific}
        self.query_template['resolutions']['exclude'].append(resolution)
        return self

    def findings_include_awarded_to_parties(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['findings'][0]['awardedToParties'].append(value)
        else:
            self.query_template['findings'][0]['awardedToParties'].append(args)
        return self

    def findings_includes_awarded_against_parties(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['findings'][0]['awardedAgainstParties'].append(value)
        else:
            self.query_template['findings'][0]['awardedAgainstParties'].append(args)
        return self

    def findings_include_judgment_source(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['rineintw'][0]['judgmentSource']['include'].append(value)
        else:
            self.query_template['findings'][0]['judgmentSource']['include'].append(args)

    def findings_exclude_judgment_source(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['rineintw'][0]['judgmentSource']['exclude'].append(value)
        else:
            self.query_template['findings'][0]['judgmentSource']['exclude'].append(args)

    def findings_include_patent_invalidity_reasons(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['findings'][0]['patentInvalidityReasons']['include'].append(value)
        else:
            self.query_template['findings'][0]['patentInvalidityReasons']['include'].append(args)
        return self

    def include_remedies_awarded_to_parties(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['remedies'][0]['awardedToParties'].append(value)
        else:
            self.query_template['remedies'][0]['awardedToParties'].append(args)
        return self

    def include_remedies_awarded_against_parties(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['remedies'][0]['awardedAgainstParties'].append(value)
        else:
            self.query_template['remedies'][0]['awardedAgainstParties'].append(args)
        return self

    def include_remedies_judgment_source(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['remedies'][0]['judgmentSource']['include'].append(value)
        else:
            self.query_template['remedies'][0]['judgmentSource']['include'].append(args)
        return self

    def exclude_remedies_judgment_source(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['remedies'][0]['judgmentSource']['exclude'].append(value)
        else:
            self.query_template['remedies'][0]['judgmentSource']['exclude'].append(args)
        return self

    def include_remedies_name_type(self, name, type):
        name_type = {'name': name, 'type': type}
        self.query_template['remedies'][0]['nameType']['include'].append(name_type)
        return self

    def exclude_remedies_name_type(self, name, type):
        name_type = {'name': name, 'type': type}
        self.query_template['remedies'][0]['nameType']['exclude'].append(name_type)
        return self

    def add_remedies_date(self, value, operator):
        self.set_date(value, self.query_template['remedies'][0]['date'], operator)
        return self

    def set_damages_minimum_amount(self, amount):
        if amount <= 0 or isinstance(amount, str):
            raise ValueError("Damages amount must be a number greater than 0")
        self.query_template['damages'][0]['minimumAmount'] = amount
        return self

    def include_patents(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['patents']['include'].append(value)
        else:
            self.query_template['patents']['include'].append(args)

    def exclude_patents(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['patents']['exclude'].append(value)
        else:
            self.query_template['patents']['exclude'].append(args)

    def include_mdl(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['mdl']['include'].append(value)
        else:
            self.query_template['mdl']['include'].append(args)
        return self

    def exclude_mdl(self, *args):
        if isinstance(args, tuple):
            for value in args:
                self.query_template['mdl']['exclude'].append(value)
        else:
            self.query_template['mdl']['exclude'].append(args)
        return self

    def execute(self):
        self.query_template = self.remove_empty_elements(self.query_template)
        return self.query_template

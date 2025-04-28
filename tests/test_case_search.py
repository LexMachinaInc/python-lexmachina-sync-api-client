"""Tests use a live client and expect a BEARER_TOKEN environment variable."""

import lexmachina
import os
import pytest


@pytest.fixture(scope="module")
def api_client():
    configuration = lexmachina.Configuration(
        host="https://api.lexmachina.com", access_token=os.environ["BEARER_TOKEN"]
    )
    api_client = lexmachina.ApiClient(configuration)
    yield api_client


@pytest.fixture(scope="module")
def fed_cases_api(api_client):
    yield lexmachina.FederalDistrictCasesApi(api_client)


@pytest.fixture(scope="module")
def state_cases_api(api_client):
    yield lexmachina.StateCasesApi(api_client)


def test_fed_case_number_search(fed_cases_api):
    case_search_results = fed_cases_api.find_district_case_by_number(
        case_numbers=["1:11-cv-11681-NMG"], court="mad"
    )
    case_result = case_search_results[0]
    assert 0 < len(case_result.matches) < 5
    assert 2000026401 in [match.district_case_id for match in case_result.matches]


def test_fed_case_query(fed_cases_api):
    query = {
        "caseStatus": "Terminated",
        "courts": {"include": ["mad"]},
        "dates": {
            "filed": {"onOrAfter": "2011-09-21"},
            "terminated": {"onOrBefore": "2018-02-08"},
        },
        "case_types": {"include": ["Patent"]},
        "parties": {"include": [11374]},
        "ordering": "ByFirstFiled",
        "page": 1,
        "pageSize": 5,
    }
    fed_case_query = lexmachina.DistrictCaseQuery.from_dict(query)
    fed_case_query_result = fed_cases_api.query_district_cases(fed_case_query)
    assert 1 < len(fed_case_query_result.cases) < 5
    case_ids = [case_ref.district_case_id for case_ref in fed_case_query_result.cases]
    assert 2000026401 in case_ids


def test_get_fed_case(fed_cases_api):
    case_data = fed_cases_api.get_district_case(2000026401)
    law_firm_names = [firm.name for firm in case_data.law_firms]
    assert "Morrison & Foerster" in law_firm_names


def test_state_case_query(state_cases_api):
    query = {
        "caseStatus": "Terminated",
        "courts": {"include": ["Court of Chancery"], "state": "DE"},
        "dates": {
            "filed": {"onOrAfter": "2015-01-17"},
            "terminated": {"onOrBefore": "2025-03-07"},
        },
        "case_types": {"include": ["Corporation Law"]},
        "parties": {"include": [33526317]},
        "ordering": "ByFirstFiled",
        "page": 1,
        "pageSize": 5,
    }
    state_case_query = lexmachina.StateCaseQuery.from_dict(query)
    state_case_query_result = state_cases_api.query_state_cases(state_case_query)
    assert 1 <= len(state_case_query_result.cases) < 5
    state_case_ids = [
        case_ref.state_case_id for case_ref in state_case_query_result.cases
    ]
    assert 2034871656 in state_case_ids


def test_get_state_case(state_cases_api):
    case_data = state_cases_api.get_state_case(2034871656)
    law_firm_names = [firm.name for firm in case_data.law_firms]
    assert "Skadden, Arps, Slate, Meagher & Flom" in law_firm_names

# lexmachina.CaseQueryApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_appeals_cases**](CaseQueryApi.md#query_appeals_cases) | **POST** /query-appeals-cases | Query Appeals Cases
[**query_district_cases**](CaseQueryApi.md#query_district_cases) | **POST** /query-district-cases | Query District Cases
[**query_state_cases**](CaseQueryApi.md#query_state_cases) | **POST** /query-state-cases | Query State Cases


# **query_appeals_cases**
> AppealsCaseQueryResult query_appeals_cases(appeals_case_query)

Query Appeals Cases

Queries federal appeals court cases.

- **data**: the appeals case query

See [https://developer.lexmachina.com/posts/query/appeals_query_usage/](https://developer.lexmachina.com/posts/query/appeals_query_usage/) for query formation.

The results will contain a list of cases, each with a specificed url and Lex Machina appealsCaseId.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.appeals_case_query import AppealsCaseQuery
from lexmachina.models.appeals_case_query_result import AppealsCaseQueryResult
from lexmachina.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lexmachina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lexmachina.Configuration(
    host = "https://api.lexmachina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = lexmachina.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lexmachina.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lexmachina.CaseQueryApi(api_client)
    appeals_case_query = {"originatingVenues": {"include": ["Originating Venue: Court of Federal Claims"]}} # AppealsCaseQuery | 

    try:
        # Query Appeals Cases
        api_response = api_instance.query_appeals_cases(appeals_case_query)
        print("The response of CaseQueryApi->query_appeals_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseQueryApi->query_appeals_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appeals_case_query** | [**AppealsCaseQuery**](AppealsCaseQuery.md)|  | 

### Return type

[**AppealsCaseQueryResult**](AppealsCaseQueryResult.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not found |  -  |
**422** | Error - 422 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_district_cases**
> DistrictCaseQueryResult query_district_cases(district_case_query)

Query District Cases

Queries federal district court cases.

- **data**: the district case query

See [https://developer.lexmachina.com/posts/query/query_usage_portal_post/](https://developer.lexmachina.com/posts/query/query_usage_portal_post/] for query formation.

The results will contain a list of cases, each with a specificed url and Lex Machina districtCaseId.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.district_case_query import DistrictCaseQuery
from lexmachina.models.district_case_query_result import DistrictCaseQueryResult
from lexmachina.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lexmachina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lexmachina.Configuration(
    host = "https://api.lexmachina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = lexmachina.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lexmachina.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lexmachina.CaseQueryApi(api_client)
    district_case_query = {"courts": {"include": ["njd"]}, "caseTypes": {"include": ["Contracts"]}, "dates": {"filed": {"onOrAfter": "2019-01-01", "onOrBefore": "2019-12-31"}, "terminated": {"onOrAfter": "2021-01-01", "onOrBefore": "2021-12-31"}}, "page": 1, "pageSize": 3} # DistrictCaseQuery | 

    try:
        # Query District Cases
        api_response = api_instance.query_district_cases(district_case_query)
        print("The response of CaseQueryApi->query_district_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseQueryApi->query_district_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_case_query** | [**DistrictCaseQuery**](DistrictCaseQuery.md)|  | 

### Return type

[**DistrictCaseQueryResult**](DistrictCaseQueryResult.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not found |  -  |
**422** | Error - 422 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_state_cases**
> StateCaseQueryResult query_state_cases(state_case_query)

Query State Cases

Queries enhanced state court cases.

- **data**: the state case query

See [https://developer.lexmachina.com/posts/query/state_query_usage/](https://developer.lexmachina.com/posts/query/state_query_usage/) for query formation.

The results will contain a list of cases, each with a specificed url and Lex Machina stateCaseId.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.state_case_query import StateCaseQuery
from lexmachina.models.state_case_query_result import StateCaseQueryResult
from lexmachina.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lexmachina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lexmachina.Configuration(
    host = "https://api.lexmachina.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = lexmachina.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lexmachina.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lexmachina.CaseQueryApi(api_client)
    state_case_query = lexmachina.StateCaseQuery() # StateCaseQuery | 

    try:
        # Query State Cases
        api_response = api_instance.query_state_cases(state_case_query)
        print("The response of CaseQueryApi->query_state_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseQueryApi->query_state_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_case_query** | [**StateCaseQuery**](StateCaseQuery.md)|  | 

### Return type

[**StateCaseQueryResult**](StateCaseQueryResult.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Expired or Missing Access Token |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


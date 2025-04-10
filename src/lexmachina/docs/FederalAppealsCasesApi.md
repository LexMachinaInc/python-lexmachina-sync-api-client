# lexmachina.FederalAppealsCasesApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_appeals_case**](FederalAppealsCasesApi.md#get_appeals_case) | **GET** /appeals-cases/{appeals_case_id} | Get Appeals Case
[**list_appealability_rulings**](FederalAppealsCasesApi.md#list_appealability_rulings) | **GET** /list-appealability-rulings | List Appealability Rulings
[**list_appellate_decisions**](FederalAppealsCasesApi.md#list_appellate_decisions) | **GET** /list-appellate-decisions/FederalDistrict | List Appellate Decisions
[**list_originating_venues**](FederalAppealsCasesApi.md#list_originating_venues) | **GET** /list-originating-venues/FederalAppeals | List Originating Venues
[**list_supreme_court_decisions**](FederalAppealsCasesApi.md#list_supreme_court_decisions) | **GET** /list-supreme-court-decisions/FederalAppeals | List Supreme Court Decisions
[**query_appeals_cases**](FederalAppealsCasesApi.md#query_appeals_cases) | **POST** /query-appeals-cases | Query Appeals Cases


# **get_appeals_case**
> AppealsCaseData get_appeals_case(appeals_case_id)

Get Appeals Case

Gets data for a single federal appeals circuit court case.

- **appeals_case_id**: the Lex Machina appealsCaseId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.appeals_case_data import AppealsCaseData
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
    api_instance = lexmachina.FederalAppealsCasesApi(api_client)
    appeals_case_id = 56 # int | 

    try:
        # Get Appeals Case
        api_response = api_instance.get_appeals_case(appeals_case_id)
        print("The response of FederalAppealsCasesApi->get_appeals_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->get_appeals_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appeals_case_id** | **int**|  | 

### Return type

[**AppealsCaseData**](AppealsCaseData.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not found |  -  |
**422** | Error - 422 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_appealability_rulings**
> object list_appealability_rulings()

List Appealability Rulings

Lists appealability rulings for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
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
    api_instance = lexmachina.FederalAppealsCasesApi(api_client)

    try:
        # List Appealability Rulings
        api_response = api_instance.list_appealability_rulings()
        print("The response of FederalAppealsCasesApi->list_appealability_rulings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->list_appealability_rulings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Expired or Missing Access Token |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_appellate_decisions**
> List[Optional[str]] list_appellate_decisions()

List Appellate Decisions

Lists appellate decisions for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
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
    api_instance = lexmachina.FederalAppealsCasesApi(api_client)

    try:
        # List Appellate Decisions
        api_response = api_instance.list_appellate_decisions()
        print("The response of FederalAppealsCasesApi->list_appellate_decisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->list_appellate_decisions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Optional[str]]**

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Expired or Missing Access Token |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_originating_venues**
> OriginatingVenuesList list_originating_venues()

List Originating Venues

Lists originating venues for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.originating_venues_list import OriginatingVenuesList
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
    api_instance = lexmachina.FederalAppealsCasesApi(api_client)

    try:
        # List Originating Venues
        api_response = api_instance.list_originating_venues()
        print("The response of FederalAppealsCasesApi->list_originating_venues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->list_originating_venues: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OriginatingVenuesList**](OriginatingVenuesList.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Expired or Missing Access Token |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supreme_court_decisions**
> List[Optional[str]] list_supreme_court_decisions()

List Supreme Court Decisions

Lists decisions from the Supreme Court for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
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
    api_instance = lexmachina.FederalAppealsCasesApi(api_client)

    try:
        # List Supreme Court Decisions
        api_response = api_instance.list_supreme_court_decisions()
        print("The response of FederalAppealsCasesApi->list_supreme_court_decisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->list_supreme_court_decisions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Optional[str]]**

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Expired or Missing Access Token |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = lexmachina.FederalAppealsCasesApi(api_client)
    appeals_case_query = {"originatingVenues": {"include": ["Originating Venue: Court of Federal Claims"]}} # AppealsCaseQuery | 

    try:
        # Query Appeals Cases
        api_response = api_instance.query_appeals_cases(appeals_case_query)
        print("The response of FederalAppealsCasesApi->query_appeals_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->query_appeals_cases: %s\n" % e)
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


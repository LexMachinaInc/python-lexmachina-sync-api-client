# openapi_client.FederalAppealsCasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_appeals_case_appeals_cases_appeals_case_id_get**](FederalAppealsCasesApi.md#get_appeals_case_appeals_cases_appeals_case_id_get) | **GET** /appeals-cases/{appeals_case_id} | Get Appeals Case
[**list_appealability_rulings_list_appealability_rulings_get**](FederalAppealsCasesApi.md#list_appealability_rulings_list_appealability_rulings_get) | **GET** /list-appealability-rulings | List Appealability Rulings
[**list_appellate_decisions_list_appellate_decisions_federal_district_get**](FederalAppealsCasesApi.md#list_appellate_decisions_list_appellate_decisions_federal_district_get) | **GET** /list-appellate-decisions/FederalDistrict | List Appellate Decisions
[**list_originating_venues_list_originating_venues_federal_appeals_get**](FederalAppealsCasesApi.md#list_originating_venues_list_originating_venues_federal_appeals_get) | **GET** /list-originating-venues/FederalAppeals | List Originating Venues
[**list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get**](FederalAppealsCasesApi.md#list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get) | **GET** /list-supreme-court-decisions/FederalAppeals | List Supreme Court Decisions
[**query_appeals_cases_query_appeals_cases_post**](FederalAppealsCasesApi.md#query_appeals_cases_query_appeals_cases_post) | **POST** /query-appeals-cases | Query Appeals Cases


# **get_appeals_case_appeals_cases_appeals_case_id_get**
> AppealsCaseData get_appeals_case_appeals_cases_appeals_case_id_get(appeals_case_id)

Get Appeals Case

Gets data for a single federal appeals circuit court case.  - **appeals_case_id**: the Lex Machina appealsCaseId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.appeals_case_data import AppealsCaseData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FederalAppealsCasesApi(api_client)
    appeals_case_id = 56 # int | 

    try:
        # Get Appeals Case
        api_response = api_instance.get_appeals_case_appeals_cases_appeals_case_id_get(appeals_case_id)
        print("The response of FederalAppealsCasesApi->get_appeals_case_appeals_cases_appeals_case_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->get_appeals_case_appeals_cases_appeals_case_id_get: %s\n" % e)
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

# **list_appealability_rulings_list_appealability_rulings_get**
> object list_appealability_rulings_list_appealability_rulings_get()

List Appealability Rulings

Lists appealability rulings for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FederalAppealsCasesApi(api_client)

    try:
        # List Appealability Rulings
        api_response = api_instance.list_appealability_rulings_list_appealability_rulings_get()
        print("The response of FederalAppealsCasesApi->list_appealability_rulings_list_appealability_rulings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->list_appealability_rulings_list_appealability_rulings_get: %s\n" % e)
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

# **list_appellate_decisions_list_appellate_decisions_federal_district_get**
> List[Optional[str]] list_appellate_decisions_list_appellate_decisions_federal_district_get()

List Appellate Decisions

Lists appellate decisions for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FederalAppealsCasesApi(api_client)

    try:
        # List Appellate Decisions
        api_response = api_instance.list_appellate_decisions_list_appellate_decisions_federal_district_get()
        print("The response of FederalAppealsCasesApi->list_appellate_decisions_list_appellate_decisions_federal_district_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->list_appellate_decisions_list_appellate_decisions_federal_district_get: %s\n" % e)
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

# **list_originating_venues_list_originating_venues_federal_appeals_get**
> OriginatingVenuesList list_originating_venues_list_originating_venues_federal_appeals_get()

List Originating Venues

Lists originating venues for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.originating_venues_list import OriginatingVenuesList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FederalAppealsCasesApi(api_client)

    try:
        # List Originating Venues
        api_response = api_instance.list_originating_venues_list_originating_venues_federal_appeals_get()
        print("The response of FederalAppealsCasesApi->list_originating_venues_list_originating_venues_federal_appeals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->list_originating_venues_list_originating_venues_federal_appeals_get: %s\n" % e)
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

# **list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get**
> List[Optional[str]] list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get()

List Supreme Court Decisions

Lists decisions from the Supreme Court for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FederalAppealsCasesApi(api_client)

    try:
        # List Supreme Court Decisions
        api_response = api_instance.list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get()
        print("The response of FederalAppealsCasesApi->list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get: %s\n" % e)
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

# **query_appeals_cases_query_appeals_cases_post**
> AppealsCaseQueryResult query_appeals_cases_query_appeals_cases_post(appeals_case_query)

Query Appeals Cases

Queries federal appeals court cases.  - **data**: the appeals case query  See [https://developer.lexmachina.com/posts/query/appeals_query_usage/](https://developer.lexmachina.com/posts/query/appeals_query_usage/) for query formation.  The results will contain a list of cases, each with a specificed url and Lex Machina appealsCaseId.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.appeals_case_query import AppealsCaseQuery
from openapi_client.models.appeals_case_query_result import AppealsCaseQueryResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FederalAppealsCasesApi(api_client)
    appeals_case_query = {"originatingVenues": {"include": ["Originating Venue: Court of Federal Claims"]}} # AppealsCaseQuery | 

    try:
        # Query Appeals Cases
        api_response = api_instance.query_appeals_cases_query_appeals_cases_post(appeals_case_query)
        print("The response of FederalAppealsCasesApi->query_appeals_cases_query_appeals_cases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalAppealsCasesApi->query_appeals_cases_query_appeals_cases_post: %s\n" % e)
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


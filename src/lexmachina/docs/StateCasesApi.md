# lexmachina.StateCasesApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_state_case**](StateCasesApi.md#get_state_case) | **GET** /state-cases/{state_case_id} | Get State Case
[**get_state_docket_entry**](StateCasesApi.md#get_state_docket_entry) | **GET** /state-docket-entries/{state_docket_entry_id} | Get State Docket Entry
[**query_state_cases**](StateCasesApi.md#query_state_cases) | **POST** /query-state-cases | Query State Cases


# **get_state_case**
> StateCaseData get_state_case(state_case_id, docket_retrieval=docket_retrieval)

Get State Case

Gets data for a single enhanced state case.

- **case_id**: the Lex Machina stateCaseId
- **docket_retrieval**: docket retreival mode

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.state_case_data import StateCaseData
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
    api_instance = lexmachina.StateCasesApi(api_client)
    state_case_id = 56 # int | 
    docket_retrieval = 'docket_retrieval_example' # str | 'all' to retrieve docket entries for the case, if not provided no docket entries will be retrieved. (optional)

    try:
        # Get State Case
        api_response = api_instance.get_state_case(state_case_id, docket_retrieval=docket_retrieval)
        print("The response of StateCasesApi->get_state_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StateCasesApi->get_state_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_case_id** | **int**|  | 
 **docket_retrieval** | **str**| &#39;all&#39; to retrieve docket entries for the case, if not provided no docket entries will be retrieved. | [optional] 

### Return type

[**StateCaseData**](StateCaseData.md)

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

# **get_state_docket_entry**
> StateDocketEntryResult get_state_docket_entry(state_docket_entry_id)

Get State Docket Entry

Gets data for a single docket entry.

- **state_docket_entry_id**: the Lex Machina stateDocketEntryId.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.state_docket_entry_result import StateDocketEntryResult
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
    api_instance = lexmachina.StateCasesApi(api_client)
    state_docket_entry_id = 56 # int | 

    try:
        # Get State Docket Entry
        api_response = api_instance.get_state_docket_entry(state_docket_entry_id)
        print("The response of StateCasesApi->get_state_docket_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StateCasesApi->get_state_docket_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_docket_entry_id** | **int**|  | 

### Return type

[**StateDocketEntryResult**](StateDocketEntryResult.md)

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
    api_instance = lexmachina.StateCasesApi(api_client)
    state_case_query = lexmachina.StateCaseQuery() # StateCaseQuery | 

    try:
        # Query State Cases
        api_response = api_instance.query_state_cases(state_case_query)
        print("The response of StateCasesApi->query_state_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StateCasesApi->query_state_cases: %s\n" % e)
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


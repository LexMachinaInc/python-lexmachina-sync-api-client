# openapi_client.StateCasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_state_case_state_cases_state_case_id_get**](StateCasesApi.md#get_state_case_state_cases_state_case_id_get) | **GET** /state-cases/{state_case_id} | Get State Case
[**query_state_cases_query_state_cases_post**](StateCasesApi.md#query_state_cases_query_state_cases_post) | **POST** /query-state-cases | Query State Cases


# **get_state_case_state_cases_state_case_id_get**
> StateCaseData get_state_case_state_cases_state_case_id_get(state_case_id)

Get State Case

Gets data for a single enhanced state case.  - **case_id**: the Lex Machina stateCaseId - **docket_retrieval**: docket retreival mode

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.state_case_data import StateCaseData
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
    api_instance = openapi_client.StateCasesApi(api_client)
    state_case_id = 56 # int | 

    try:
        # Get State Case
        api_response = api_instance.get_state_case_state_cases_state_case_id_get(state_case_id)
        print("The response of StateCasesApi->get_state_case_state_cases_state_case_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StateCasesApi->get_state_case_state_cases_state_case_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_case_id** | **int**|  | 

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
**401** | Expired or Missing Access Token |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_state_cases_query_state_cases_post**
> StateCaseQueryResult query_state_cases_query_state_cases_post(state_case_query)

Query State Cases

Queries enhanced state court cases.  - **data**: the state case query  See [https://developer.lexmachina.com/posts/query/state_query_usage/](https://developer.lexmachina.com/posts/query/state_query_usage/) for query formation.  The results will contain a list of cases, each with a specificed url and Lex Machina stateCaseId.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.state_case_query import StateCaseQuery
from openapi_client.models.state_case_query_result import StateCaseQueryResult
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
    api_instance = openapi_client.StateCasesApi(api_client)
    state_case_query = openapi_client.StateCaseQuery() # StateCaseQuery | 

    try:
        # Query State Cases
        api_response = api_instance.query_state_cases_query_state_cases_post(state_case_query)
        print("The response of StateCasesApi->query_state_cases_query_state_cases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StateCasesApi->query_state_cases_query_state_cases_post: %s\n" % e)
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


# lawmachine.AttorneysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attorney_attorneys_attorney_id_get**](AttorneysApi.md#get_attorney_attorneys_attorney_id_get) | **GET** /attorneys/{attorney_id} | Get Attorney
[**get_attorneys_attorneys_get**](AttorneysApi.md#get_attorneys_attorneys_get) | **GET** /attorneys | Get Attorneys
[**search_attorneys_search_attorneys_get**](AttorneysApi.md#search_attorneys_search_attorneys_get) | **GET** /search-attorneys | Search Attorneys


# **get_attorney_attorneys_attorney_id_get**
> ResponseGetAttorneyAttorneysAttorneyIdGet get_attorney_attorneys_attorney_id_get(attorney_id)

Get Attorney

Gets data for a single attorney.  - **attorney_id**: the Lex Machina attorneyId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.response_get_attorney_attorneys_attorney_id_get import ResponseGetAttorneyAttorneysAttorneyIdGet
from lawmachine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lawmachine.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = lawmachine.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lawmachine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lawmachine.AttorneysApi(api_client)
    attorney_id = 56 # int | 

    try:
        # Get Attorney
        api_response = api_instance.get_attorney_attorneys_attorney_id_get(attorney_id)
        print("The response of AttorneysApi->get_attorney_attorneys_attorney_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttorneysApi->get_attorney_attorneys_attorney_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_id** | **int**|  | 

### Return type

[**ResponseGetAttorneyAttorneysAttorneyIdGet**](ResponseGetAttorneyAttorneysAttorneyIdGet.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attorneys_attorneys_get**
> List[GetAttorneysAttorneysGet200ResponseInner] get_attorneys_attorneys_get(attorney_ids)

Get Attorneys

Gets data for one or more attorneys.  - **attorneyIds**: the Lex Machina attorneyIds  If any of the the attorneyIds given are not the current lexmachina attorneyId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.get_attorneys_attorneys_get200_response_inner import GetAttorneysAttorneysGet200ResponseInner
from lawmachine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lawmachine.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = lawmachine.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lawmachine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lawmachine.AttorneysApi(api_client)
    attorney_ids = [56] # List[int] | 

    try:
        # Get Attorneys
        api_response = api_instance.get_attorneys_attorneys_get(attorney_ids)
        print("The response of AttorneysApi->get_attorneys_attorneys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttorneysApi->get_attorneys_attorneys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetAttorneysAttorneysGet200ResponseInner]**](GetAttorneysAttorneysGet200ResponseInner.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_attorneys_search_attorneys_get**
> AttorneySearchResults search_attorneys_search_attorneys_get(q, page_number=page_number, page_size=page_size)

Search Attorneys

Searches for attorneys.  - **q**: the query string - **page_number**: page number of the results - **page_size**:  results per page  This is a case-insensitive search that will match anywhere within the name of the attorney.  The results will have page and totalCount fields as well as a convenience link via the field nextPage.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.attorney_search_results import AttorneySearchResults
from lawmachine.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lawmachine.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JwtAccessBearer
configuration = lawmachine.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lawmachine.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lawmachine.AttorneysApi(api_client)
    q = 'q_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 1 # int |  (optional) (default to 1)

    try:
        # Search Attorneys
        api_response = api_instance.search_attorneys_search_attorneys_get(q, page_number=page_number, page_size=page_size)
        print("The response of AttorneysApi->search_attorneys_search_attorneys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttorneysApi->search_attorneys_search_attorneys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 1]

### Return type

[**AttorneySearchResults**](AttorneySearchResults.md)

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


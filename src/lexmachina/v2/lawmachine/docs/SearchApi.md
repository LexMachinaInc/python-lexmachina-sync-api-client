# lawmachine.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seach_law_firms_search_law_firms_get**](SearchApi.md#seach_law_firms_search_law_firms_get) | **GET** /search-law-firms | Seach Law Firms
[**search_attorneys_search_attorneys_get**](SearchApi.md#search_attorneys_search_attorneys_get) | **GET** /search-attorneys | Search Attorneys
[**search_judges_search_judges_get**](SearchApi.md#search_judges_search_judges_get) | **GET** /search-judges | Search Judges
[**search_parties_search_parties_get**](SearchApi.md#search_parties_search_parties_get) | **GET** /search-parties | Search Parties


# **seach_law_firms_search_law_firms_get**
> LawFirmSearchResult seach_law_firms_search_law_firms_get(q, page_number=page_number, page_size=page_size)

Seach Law Firms

Searches for law firms.  - **q**: the query string - **page_number**: page number of the results - **page_size**:  results per page  This is a case-insensitive search that will match anywhere within the name of the firm.  The results will have page and totalCount fields as well as a convenience link via the field nextPage.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.law_firm_search_result import LawFirmSearchResult
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
    api_instance = lawmachine.SearchApi(api_client)
    q = 'q_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 1 # int |  (optional) (default to 1)

    try:
        # Seach Law Firms
        api_response = api_instance.seach_law_firms_search_law_firms_get(q, page_number=page_number, page_size=page_size)
        print("The response of SearchApi->seach_law_firms_search_law_firms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->seach_law_firms_search_law_firms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 1]

### Return type

[**LawFirmSearchResult**](LawFirmSearchResult.md)

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
    api_instance = lawmachine.SearchApi(api_client)
    q = 'q_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 1 # int |  (optional) (default to 1)

    try:
        # Search Attorneys
        api_response = api_instance.search_attorneys_search_attorneys_get(q, page_number=page_number, page_size=page_size)
        print("The response of SearchApi->search_attorneys_search_attorneys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_attorneys_search_attorneys_get: %s\n" % e)
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

# **search_judges_search_judges_get**
> JudgeSearchResult search_judges_search_judges_get(q)

Search Judges

Searches for attorneys.  - **q**: the query string  This matches from the beginning of the last name. The search query \"hof\" will match the name \"Hoffman\" but will not match \"Schofield\".

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.judge_search_result import JudgeSearchResult
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
    api_instance = lawmachine.SearchApi(api_client)
    q = 'q_example' # str | 

    try:
        # Search Judges
        api_response = api_instance.search_judges_search_judges_get(q)
        print("The response of SearchApi->search_judges_search_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_judges_search_judges_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 

### Return type

[**JudgeSearchResult**](JudgeSearchResult.md)

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

# **search_parties_search_parties_get**
> PartySearchResults search_parties_search_parties_get(q, page_number=page_number, page_size=page_size)

Search Parties

Searches for parties.  - **q**: the query string - **page_number**: page number of the results - **page_size**:  results per page  This is a case-insensitive search that will match anywhere within the name of the party.  The results will have page and totalCount fields as well as a convenience link via the field nextPage.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.party_search_results import PartySearchResults
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
    api_instance = lawmachine.SearchApi(api_client)
    q = 'q_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 1 # int |  (optional) (default to 1)

    try:
        # Search Parties
        api_response = api_instance.search_parties_search_parties_get(q, page_number=page_number, page_size=page_size)
        print("The response of SearchApi->search_parties_search_parties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_parties_search_parties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 1]

### Return type

[**PartySearchResults**](PartySearchResults.md)

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


# lawmachine.PartiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_parties_parties_get**](PartiesApi.md#get_parties_parties_get) | **GET** /parties | Get Parties
[**get_party_parties_party_id_get**](PartiesApi.md#get_party_parties_party_id_get) | **GET** /parties/{party_id} | Get Party
[**search_parties_search_parties_get**](PartiesApi.md#search_parties_search_parties_get) | **GET** /search-parties | Search Parties


# **get_parties_parties_get**
> List[GetPartiesPartiesGet200ResponseInner] get_parties_parties_get(party_ids)

Get Parties

Gets data for one or more parties.  - **partyIds**: the Lex Machina partyIds  If any of the the partyIds given are not the current lexmachina partyId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.get_parties_parties_get200_response_inner import GetPartiesPartiesGet200ResponseInner
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
    api_instance = lawmachine.PartiesApi(api_client)
    party_ids = [56] # List[int] | 

    try:
        # Get Parties
        api_response = api_instance.get_parties_parties_get(party_ids)
        print("The response of PartiesApi->get_parties_parties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartiesApi->get_parties_parties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetPartiesPartiesGet200ResponseInner]**](GetPartiesPartiesGet200ResponseInner.md)

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

# **get_party_parties_party_id_get**
> ResponseGetPartyPartiesPartyIdGet get_party_parties_party_id_get(party_id)

Get Party

Gets data for a single party.  - **party_id**: the Lex Machina partyId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.response_get_party_parties_party_id_get import ResponseGetPartyPartiesPartyIdGet
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
    api_instance = lawmachine.PartiesApi(api_client)
    party_id = 56 # int | 

    try:
        # Get Party
        api_response = api_instance.get_party_parties_party_id_get(party_id)
        print("The response of PartiesApi->get_party_parties_party_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartiesApi->get_party_parties_party_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_id** | **int**|  | 

### Return type

[**ResponseGetPartyPartiesPartyIdGet**](ResponseGetPartyPartiesPartyIdGet.md)

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
    api_instance = lawmachine.PartiesApi(api_client)
    q = 'q_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 1 # int |  (optional) (default to 1)

    try:
        # Search Parties
        api_response = api_instance.search_parties_search_parties_get(q, page_number=page_number, page_size=page_size)
        print("The response of PartiesApi->search_parties_search_parties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartiesApi->search_parties_search_parties_get: %s\n" % e)
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


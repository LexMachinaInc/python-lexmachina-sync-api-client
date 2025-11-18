# lexmachina.PartiesApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_parties**](PartiesApi.md#get_parties) | **GET** /parties | Get Parties
[**get_party**](PartiesApi.md#get_party) | **GET** /parties/{party_id} | Get Party
[**get_party_groups**](PartiesApi.md#get_party_groups) | **GET** /party-groups | Get Party Groups
[**search_parties**](PartiesApi.md#search_parties) | **GET** /search-parties | Search Parties


# **get_parties**
> List[GetParties200ResponseInner] get_parties(party_ids)

Get Parties

Gets data for one or more parties.

- **partyIds**: the Lex Machina partyIds

If any of the the partyIds given are not the current lexmachina partyId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.get_parties200_response_inner import GetParties200ResponseInner
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
    api_instance = lexmachina.PartiesApi(api_client)
    party_ids = [56] # List[int] | 

    try:
        # Get Parties
        api_response = api_instance.get_parties(party_ids)
        print("The response of PartiesApi->get_parties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartiesApi->get_parties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetParties200ResponseInner]**](GetParties200ResponseInner.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not found |  -  |
**401** | Invalid or expired token |  -  |
**422** | Error - 422 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party**
> ResponseGetPartyPartiesPartyIdGet get_party(party_id)

Get Party

Gets data for a single party.

- **party_id**: the Lex Machina partyId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.response_get_party_parties_party_id_get import ResponseGetPartyPartiesPartyIdGet
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
    api_instance = lexmachina.PartiesApi(api_client)
    party_id = 56 # int | 

    try:
        # Get Party
        api_response = api_instance.get_party(party_id)
        print("The response of PartiesApi->get_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartiesApi->get_party: %s\n" % e)
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
**404** | Not found |  -  |
**422** | Error - 422 |  -  |
**401** | Invalid or expired token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_party_groups**
> List[PartyGroup] get_party_groups()

Get Party Groups

Gets a list of all party groups the user has created.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.party_group import PartyGroup
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
    api_instance = lexmachina.PartiesApi(api_client)

    try:
        # Get Party Groups
        api_response = api_instance.get_party_groups()
        print("The response of PartiesApi->get_party_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartiesApi->get_party_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PartyGroup]**](PartyGroup.md)

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

# **search_parties**
> PartySearchResults search_parties(q, page_number=page_number, page_size=page_size)

Search Parties

Searches for parties.

- **q**: the query string
- **page_number**: page number of the results
- **page_size**:  results per page

This is a case-insensitive search that will match anywhere within the name of the party.

The results will have page and totalCount fields as well as a convenience link via the field nextPage.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.party_search_results import PartySearchResults
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
    api_instance = lexmachina.PartiesApi(api_client)
    q = 'q_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 1 # int |  (optional) (default to 1)

    try:
        # Search Parties
        api_response = api_instance.search_parties(q, page_number=page_number, page_size=page_size)
        print("The response of PartiesApi->search_parties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartiesApi->search_parties: %s\n" % e)
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
**422** | Error - 422 |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


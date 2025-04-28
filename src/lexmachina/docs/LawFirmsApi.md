# lexmachina.LawFirmsApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_law_firm**](LawFirmsApi.md#get_law_firm) | **GET** /law-firms/{law_firm_id} | Get Law Firm
[**get_law_firms**](LawFirmsApi.md#get_law_firms) | **GET** /law-firms | Get Law Firms
[**seach_law_firms**](LawFirmsApi.md#seach_law_firms) | **GET** /search-law-firms | Seach Law Firms


# **get_law_firm**
> ResponseGetLawFirmLawFirmsLawFirmIdGet get_law_firm(law_firm_id)

Get Law Firm

Gets data for a single law firm.

- **law_firm_id**: the Lex Machina lawFirmID

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.response_get_law_firm_law_firms_law_firm_id_get import ResponseGetLawFirmLawFirmsLawFirmIdGet
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
    api_instance = lexmachina.LawFirmsApi(api_client)
    law_firm_id = 56 # int | 

    try:
        # Get Law Firm
        api_response = api_instance.get_law_firm(law_firm_id)
        print("The response of LawFirmsApi->get_law_firm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LawFirmsApi->get_law_firm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **law_firm_id** | **int**|  | 

### Return type

[**ResponseGetLawFirmLawFirmsLawFirmIdGet**](ResponseGetLawFirmLawFirmsLawFirmIdGet.md)

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

# **get_law_firms**
> List[GetLawFirms200ResponseInner] get_law_firms(law_firm_ids)

Get Law Firms

Gets data for one or more law firms.

- **lawFirmIds**: the Lex Machina lawFirmIds

If any of the the lawFirmIds given are not the current lexmachina lawFirmId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.get_law_firms200_response_inner import GetLawFirms200ResponseInner
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
    api_instance = lexmachina.LawFirmsApi(api_client)
    law_firm_ids = [56] # List[int] | 

    try:
        # Get Law Firms
        api_response = api_instance.get_law_firms(law_firm_ids)
        print("The response of LawFirmsApi->get_law_firms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LawFirmsApi->get_law_firms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **law_firm_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetLawFirms200ResponseInner]**](GetLawFirms200ResponseInner.md)

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

# **seach_law_firms**
> LawFirmSearchResult seach_law_firms(q, page_number=page_number, page_size=page_size)

Seach Law Firms

Searches for law firms.

- **q**: the query string
- **page_number**: page number of the results
- **page_size**:  results per page

This is a case-insensitive search that will match anywhere within the name of the firm.

The results will have page and totalCount fields as well as a convenience link via the field nextPage.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.law_firm_search_result import LawFirmSearchResult
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
    api_instance = lexmachina.LawFirmsApi(api_client)
    q = 'q_example' # str | 
    page_number = 1 # int |  (optional) (default to 1)
    page_size = 1 # int |  (optional) (default to 1)

    try:
        # Seach Law Firms
        api_response = api_instance.seach_law_firms(q, page_number=page_number, page_size=page_size)
        print("The response of LawFirmsApi->seach_law_firms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LawFirmsApi->seach_law_firms: %s\n" % e)
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


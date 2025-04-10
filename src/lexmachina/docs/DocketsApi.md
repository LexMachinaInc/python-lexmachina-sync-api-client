# lexmachina.DocketsApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_docket_entry**](DocketsApi.md#get_district_docket_entry) | **GET** /docket-entries/{docket_entry_id} | Get District Docket Entry
[**get_itc_document_entry**](DocketsApi.md#get_itc_document_entry) | **GET** /itc-document-entries/{usitc_document_id} | Get Itc Document Entry
[**get_state_docket_entry**](DocketsApi.md#get_state_docket_entry) | **GET** /state-docket-entries/{state_docket_entry_id} | Get State Docket Entry


# **get_district_docket_entry**
> DocketEntryResult get_district_docket_entry(docket_entry_id)

Get District Docket Entry

Gets data for a single docket entry.

- **docket_entry_id**: the Lex Machina docketEntryId.

Data returned for a docket will vary in format based on context, only the ids and urls for the relevant data will included.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.docket_entry_result import DocketEntryResult
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
    api_instance = lexmachina.DocketsApi(api_client)
    docket_entry_id = 56 # int | 

    try:
        # Get District Docket Entry
        api_response = api_instance.get_district_docket_entry(docket_entry_id)
        print("The response of DocketsApi->get_district_docket_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocketsApi->get_district_docket_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docket_entry_id** | **int**|  | 

### Return type

[**DocketEntryResult**](DocketEntryResult.md)

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

# **get_itc_document_entry**
> ITCDocumentData get_itc_document_entry(usitc_document_id)

Get Itc Document Entry

Gets data for a single US ITC document.

- **usitc_document_id**: The document id.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.itc_document_data import ITCDocumentData
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
    api_instance = lexmachina.DocketsApi(api_client)
    usitc_document_id = 56 # int | 

    try:
        # Get Itc Document Entry
        api_response = api_instance.get_itc_document_entry(usitc_document_id)
        print("The response of DocketsApi->get_itc_document_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocketsApi->get_itc_document_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usitc_document_id** | **int**|  | 

### Return type

[**ITCDocumentData**](ITCDocumentData.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

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
    api_instance = lexmachina.DocketsApi(api_client)
    state_docket_entry_id = 56 # int | 

    try:
        # Get State Docket Entry
        api_response = api_instance.get_state_docket_entry(state_docket_entry_id)
        print("The response of DocketsApi->get_state_docket_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocketsApi->get_state_docket_entry: %s\n" % e)
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


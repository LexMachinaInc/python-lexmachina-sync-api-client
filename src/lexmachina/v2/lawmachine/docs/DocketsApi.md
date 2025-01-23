# lawmachine.DocketsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_docket_entry_docket_entries_docket_entry_id_get**](DocketsApi.md#get_docket_entry_docket_entries_docket_entry_id_get) | **GET** /docket-entries/{docket_entry_id} | Get Docket Entry
[**get_itc_document_entry_itc_document_entries_usitc_document_id_get**](DocketsApi.md#get_itc_document_entry_itc_document_entries_usitc_document_id_get) | **GET** /itc-document-entries/{usitc_document_id} | Get Itc Document Entry


# **get_docket_entry_docket_entries_docket_entry_id_get**
> DocketEntryResult get_docket_entry_docket_entries_docket_entry_id_get(docket_entry_id)

Get Docket Entry

Gets data for a single docket entry.  - **docket_entry_id**: the Lex Machina docketEntryId.  Data returned for a docket will vary in format based on context, only the ids and urls for the relevant data will included.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.docket_entry_result import DocketEntryResult
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
    api_instance = lawmachine.DocketsApi(api_client)
    docket_entry_id = 56 # int | 

    try:
        # Get Docket Entry
        api_response = api_instance.get_docket_entry_docket_entries_docket_entry_id_get(docket_entry_id)
        print("The response of DocketsApi->get_docket_entry_docket_entries_docket_entry_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocketsApi->get_docket_entry_docket_entries_docket_entry_id_get: %s\n" % e)
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

# **get_itc_document_entry_itc_document_entries_usitc_document_id_get**
> ITCDocumentData get_itc_document_entry_itc_document_entries_usitc_document_id_get(usitc_document_id)

Get Itc Document Entry

Gets data for a single US ITC document.  - **usitc_document_id**: The document id.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.itc_document_data import ITCDocumentData
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
    api_instance = lawmachine.DocketsApi(api_client)
    usitc_document_id = 56 # int | 

    try:
        # Get Itc Document Entry
        api_response = api_instance.get_itc_document_entry_itc_document_entries_usitc_document_id_get(usitc_document_id)
        print("The response of DocketsApi->get_itc_document_entry_itc_document_entries_usitc_document_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocketsApi->get_itc_document_entry_itc_document_entries_usitc_document_id_get: %s\n" % e)
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


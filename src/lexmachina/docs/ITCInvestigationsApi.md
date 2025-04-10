# lexmachina.ITCInvestigationsApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_itc_investigation**](ITCInvestigationsApi.md#get_itc_investigation) | **GET** /itc-investigations/{itc_investigation_id} | Get Itc Investigation


# **get_itc_investigation**
> ITCInvestigationData get_itc_investigation(itc_investigation_id, document_retrieval=document_retrieval)

Get Itc Investigation

Gets data for a single US ITC investigation.

- **itc_investigation_id**: the ITC investigation number
- **docket_retrieval**: docket retreival mode

The investigation number format should exclude the leading "337-TA-"

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.itc_investigation_data import ITCInvestigationData
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
    api_instance = lexmachina.ITCInvestigationsApi(api_client)
    itc_investigation_id = 'itc_investigation_id_example' # str | 
    document_retrieval = 'document_retrieval_example' # str | 'all' to retrieve all documents for the investigation, if not provided documents will not be returned. (optional)

    try:
        # Get Itc Investigation
        api_response = api_instance.get_itc_investigation(itc_investigation_id, document_retrieval=document_retrieval)
        print("The response of ITCInvestigationsApi->get_itc_investigation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ITCInvestigationsApi->get_itc_investigation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itc_investigation_id** | **str**|  | 
 **document_retrieval** | **str**| &#39;all&#39; to retrieve all documents for the investigation, if not provided documents will not be returned. | [optional] 

### Return type

[**ITCInvestigationData**](ITCInvestigationData.md)

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


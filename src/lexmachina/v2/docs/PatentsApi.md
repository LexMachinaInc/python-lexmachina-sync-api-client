# openapi_client.PatentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_patent_patents_patent_number_get**](PatentsApi.md#get_patent_patents_patent_number_get) | **GET** /patents/{patent_number} | Get Patent
[**get_patents_patents_get**](PatentsApi.md#get_patents_patents_get) | **GET** /patents | Get Patents


# **get_patent_patents_patent_number_get**
> PatentData get_patent_patents_patent_number_get(patent_number)

Get Patent

Gets data for a single uspto patent.  - **patent_number**: the patent number

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.patent_data import PatentData
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
    api_instance = openapi_client.PatentsApi(api_client)
    patent_number = 'patent_number_example' # str | 

    try:
        # Get Patent
        api_response = api_instance.get_patent_patents_patent_number_get(patent_number)
        print("The response of PatentsApi->get_patent_patents_patent_number_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentsApi->get_patent_patents_patent_number_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patent_number** | **str**|  | 

### Return type

[**PatentData**](PatentData.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Patent Not Found |  -  |
**401** | Expired or Missing Access Token |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_patents_patents_get**
> List[PatentData] get_patents_patents_get(patent_numbers)

Get Patents

Gets data for one or more uspto patents.  - **patentNumbers**: the patent numbers

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.patent_data import PatentData
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
    api_instance = openapi_client.PatentsApi(api_client)
    patent_numbers = ['patent_numbers_example'] # List[Optional[str]] | 

    try:
        # Get Patents
        api_response = api_instance.get_patents_patents_get(patent_numbers)
        print("The response of PatentsApi->get_patents_patents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentsApi->get_patents_patents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patent_numbers** | [**List[Optional[str]]**](str.md)|  | 

### Return type

[**List[PatentData]**](PatentData.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Patent Not Found |  -  |
**401** | Expired or Missing Access Token |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


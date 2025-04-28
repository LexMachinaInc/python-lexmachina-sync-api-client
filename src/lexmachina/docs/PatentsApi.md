# lexmachina.PatentsApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_patent**](PatentsApi.md#get_patent) | **GET** /patents/{patent_number} | Get Patent
[**get_patents**](PatentsApi.md#get_patents) | **GET** /patents | Get Patents


# **get_patent**
> PatentData get_patent(patent_number)

Get Patent

Gets data for a single uspto patent.

- **patent_number**: the patent number

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.patent_data import PatentData
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
    api_instance = lexmachina.PatentsApi(api_client)
    patent_number = 'patent_number_example' # str | 

    try:
        # Get Patent
        api_response = api_instance.get_patent(patent_number)
        print("The response of PatentsApi->get_patent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentsApi->get_patent: %s\n" % e)
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

# **get_patents**
> List[PatentData] get_patents(patent_numbers)

Get Patents

Gets data for one or more uspto patents.

- **patentNumbers**: the patent numbers

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.patent_data import PatentData
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
    api_instance = lexmachina.PatentsApi(api_client)
    patent_numbers = ['patent_numbers_example'] # List[Optional[str]] | 

    try:
        # Get Patents
        api_response = api_instance.get_patents(patent_numbers)
        print("The response of PatentsApi->get_patents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentsApi->get_patents: %s\n" % e)
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


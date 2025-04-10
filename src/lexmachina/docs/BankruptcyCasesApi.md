# lexmachina.BankruptcyCasesApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bankruptcy_case**](BankruptcyCasesApi.md#get_bankruptcy_case) | **GET** /bankruptcy-cases/{bankruptcy_case_id} | Get Bankruptcy Case


# **get_bankruptcy_case**
> BankruptcyCaseData get_bankruptcy_case(bankruptcy_case_id)

Get Bankruptcy Case

Gets data for a single federal bankruptcy court case.

- **bankruptcy_case_id**: the Lex Machina bankruptcyCaseId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.bankruptcy_case_data import BankruptcyCaseData
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
    api_instance = lexmachina.BankruptcyCasesApi(api_client)
    bankruptcy_case_id = 56 # int | 

    try:
        # Get Bankruptcy Case
        api_response = api_instance.get_bankruptcy_case(bankruptcy_case_id)
        print("The response of BankruptcyCasesApi->get_bankruptcy_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankruptcyCasesApi->get_bankruptcy_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankruptcy_case_id** | **int**|  | 

### Return type

[**BankruptcyCaseData**](BankruptcyCaseData.md)

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


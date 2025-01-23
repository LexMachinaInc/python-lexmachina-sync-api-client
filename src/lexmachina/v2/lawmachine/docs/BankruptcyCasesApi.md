# lawmachine.BankruptcyCasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bankruptcy_case_bankruptcy_cases_bankruptcy_case_id_get**](BankruptcyCasesApi.md#get_bankruptcy_case_bankruptcy_cases_bankruptcy_case_id_get) | **GET** /bankruptcy-cases/{bankruptcy_case_id} | Get Bankruptcy Case


# **get_bankruptcy_case_bankruptcy_cases_bankruptcy_case_id_get**
> BankruptcyCaseData get_bankruptcy_case_bankruptcy_cases_bankruptcy_case_id_get(bankruptcy_case_id)

Get Bankruptcy Case

Gets data for a single federal bankruptcy court case.  - **bankruptcy_case_id**: the Lex Machina bankruptcyCaseId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.bankruptcy_case_data import BankruptcyCaseData
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
    api_instance = lawmachine.BankruptcyCasesApi(api_client)
    bankruptcy_case_id = 56 # int | 

    try:
        # Get Bankruptcy Case
        api_response = api_instance.get_bankruptcy_case_bankruptcy_cases_bankruptcy_case_id_get(bankruptcy_case_id)
        print("The response of BankruptcyCasesApi->get_bankruptcy_case_bankruptcy_cases_bankruptcy_case_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankruptcyCasesApi->get_bankruptcy_case_bankruptcy_cases_bankruptcy_case_id_get: %s\n" % e)
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


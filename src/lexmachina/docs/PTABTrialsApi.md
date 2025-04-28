# lexmachina.PTABTrialsApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ptab_trial**](PTABTrialsApi.md#get_ptab_trial) | **GET** /ptab-trials/{ptab_trial_id} | Get Ptab Trial


# **get_ptab_trial**
> PTABTrialData get_ptab_trial(ptab_trial_id)

Get Ptab Trial

Gets data for a single PTAB trial.

- **ptab_trial_id**: the Lex Machina PTAB Trial id

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.ptab_trial_data import PTABTrialData
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
    api_instance = lexmachina.PTABTrialsApi(api_client)
    ptab_trial_id = 56 # int | 

    try:
        # Get Ptab Trial
        api_response = api_instance.get_ptab_trial(ptab_trial_id)
        print("The response of PTABTrialsApi->get_ptab_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PTABTrialsApi->get_ptab_trial: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptab_trial_id** | **int**|  | 

### Return type

[**PTABTrialData**](PTABTrialData.md)

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


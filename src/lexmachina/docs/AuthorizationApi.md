# lexmachina.AuthorizationApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth2_token**](AuthorizationApi.md#oauth2_token) | **POST** /oauth2/token | Oauth2 Token


# **oauth2_token**
> object oauth2_token(client_id=client_id, client_secret=client_secret, grant_type=grant_type)

Oauth2 Token

Generates a shot lived bearer token used to authenticate an application to the rest of the API.

- **client_id**: client id from the application
- **client_secret**: client secret from the application
- **grant_type**: only "client_credentials" are supported at this time

See [https://law.lexmachina.com/api-settings](https://law.lexmachina.com/api-settings) for application management.

### Example


```python
import lexmachina
from lexmachina.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lexmachina.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lexmachina.Configuration(
    host = "https://api.lexmachina.com"
)


# Enter a context with an instance of the API client
with lexmachina.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lexmachina.AuthorizationApi(api_client)
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)
    grant_type = 'client_credentials' # str |  (optional) (default to 'client_credentials')

    try:
        # Oauth2 Token
        api_response = api_instance.oauth2_token(client_id=client_id, client_secret=client_secret, grant_type=grant_type)
        print("The response of AuthorizationApi->oauth2_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->oauth2_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 
 **grant_type** | **str**|  | [optional] [default to &#39;client_credentials&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


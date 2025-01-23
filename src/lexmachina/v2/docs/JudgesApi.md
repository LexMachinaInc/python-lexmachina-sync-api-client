# openapi_client.JudgesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get**](JudgesApi.md#get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get) | **GET** /bankruptcy-judges/{bankruptcy_judge_id} | Get Bankruptcy Judge
[**get_bankruptcy_judges_bankruptcy_judges_get**](JudgesApi.md#get_bankruptcy_judges_bankruptcy_judges_get) | **GET** /bankruptcy-judges | Get Bankruptcy Judges
[**get_federal_judge_federal_judges_federal_judge_id_get**](JudgesApi.md#get_federal_judge_federal_judges_federal_judge_id_get) | **GET** /federal-judges/{federal_judge_id} | Get Federal Judge
[**get_federal_judges_federal_judges_get**](JudgesApi.md#get_federal_judges_federal_judges_get) | **GET** /federal-judges | Get Federal Judges
[**get_magistrate_magistrate_judges_magistrate_judge_id_get**](JudgesApi.md#get_magistrate_magistrate_judges_magistrate_judge_id_get) | **GET** /magistrate-judges/{magistrate_judge_id} | Get Magistrate
[**get_magistrates_magistrate_judges_get**](JudgesApi.md#get_magistrates_magistrate_judges_get) | **GET** /magistrate-judges | Get Magistrates
[**get_state_judge_state_judges_state_judge_id_get**](JudgesApi.md#get_state_judge_state_judges_state_judge_id_get) | **GET** /state-judges/{state_judge_id} | Get State Judge
[**get_state_judges_state_judges_get**](JudgesApi.md#get_state_judges_state_judges_get) | **GET** /state-judges | Get State Judges
[**search_judges_search_judges_get**](JudgesApi.md#search_judges_search_judges_get) | **GET** /search-judges | Search Judges


# **get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get**
> BankruptcyJudgeData get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get(bankruptcy_judge_id)

Get Bankruptcy Judge

Gets data for a single federal bankruptcy judge.  - **bankruptcy_judge_id**: the Lex Machina bankruptcyJudgeId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.bankruptcy_judge_data import BankruptcyJudgeData
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
    api_instance = openapi_client.JudgesApi(api_client)
    bankruptcy_judge_id = 56 # int | 

    try:
        # Get Bankruptcy Judge
        api_response = api_instance.get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get(bankruptcy_judge_id)
        print("The response of JudgesApi->get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankruptcy_judge_id** | **int**|  | 

### Return type

[**BankruptcyJudgeData**](BankruptcyJudgeData.md)

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

# **get_bankruptcy_judges_bankruptcy_judges_get**
> List[BankruptcyJudgeData] get_bankruptcy_judges_bankruptcy_judges_get(bankruptcy_judge_ids)

Get Bankruptcy Judges

Gets data for one or more federal bankruptcy judges.  - **attorneyIds**: the Lex Machina bankruptcyJudgeIds

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.bankruptcy_judge_data import BankruptcyJudgeData
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
    api_instance = openapi_client.JudgesApi(api_client)
    bankruptcy_judge_ids = [56] # List[int] | 

    try:
        # Get Bankruptcy Judges
        api_response = api_instance.get_bankruptcy_judges_bankruptcy_judges_get(bankruptcy_judge_ids)
        print("The response of JudgesApi->get_bankruptcy_judges_bankruptcy_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_bankruptcy_judges_bankruptcy_judges_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankruptcy_judge_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[BankruptcyJudgeData]**](BankruptcyJudgeData.md)

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

# **get_federal_judge_federal_judges_federal_judge_id_get**
> FederalJudgeData get_federal_judge_federal_judges_federal_judge_id_get(federal_judge_id)

Get Federal Judge

Gets data for a single federal Article III judge.  - **judge_id**: the judge id

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.federal_judge_data import FederalJudgeData
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
    api_instance = openapi_client.JudgesApi(api_client)
    federal_judge_id = 56 # int | 

    try:
        # Get Federal Judge
        api_response = api_instance.get_federal_judge_federal_judges_federal_judge_id_get(federal_judge_id)
        print("The response of JudgesApi->get_federal_judge_federal_judges_federal_judge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_federal_judge_federal_judges_federal_judge_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **federal_judge_id** | **int**|  | 

### Return type

[**FederalJudgeData**](FederalJudgeData.md)

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

# **get_federal_judges_federal_judges_get**
> List[FederalJudgeData] get_federal_judges_federal_judges_get(federal_judge_ids)

Get Federal Judges

Gets data for one or more federal Article III judges.  - **judgeIds**: the judge Ids

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.federal_judge_data import FederalJudgeData
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
    api_instance = openapi_client.JudgesApi(api_client)
    federal_judge_ids = [56] # List[int] | 

    try:
        # Get Federal Judges
        api_response = api_instance.get_federal_judges_federal_judges_get(federal_judge_ids)
        print("The response of JudgesApi->get_federal_judges_federal_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_federal_judges_federal_judges_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **federal_judge_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[FederalJudgeData]**](FederalJudgeData.md)

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

# **get_magistrate_magistrate_judges_magistrate_judge_id_get**
> MagistrateJudgeData get_magistrate_magistrate_judges_magistrate_judge_id_get(magistrate_judge_id)

Get Magistrate

Gets data for a single federal magistrate judge.  - **magistrate_judge_id**: the Lex Machina magistrateJudgeId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.magistrate_judge_data import MagistrateJudgeData
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
    api_instance = openapi_client.JudgesApi(api_client)
    magistrate_judge_id = 56 # int | 

    try:
        # Get Magistrate
        api_response = api_instance.get_magistrate_magistrate_judges_magistrate_judge_id_get(magistrate_judge_id)
        print("The response of JudgesApi->get_magistrate_magistrate_judges_magistrate_judge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_magistrate_magistrate_judges_magistrate_judge_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **magistrate_judge_id** | **int**|  | 

### Return type

[**MagistrateJudgeData**](MagistrateJudgeData.md)

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

# **get_magistrates_magistrate_judges_get**
> List[MagistrateJudgeData] get_magistrates_magistrate_judges_get(magistrate_judge_ids)

Get Magistrates

Gets data for a one or more federal magistrate judges.  - **magistrateJudgeIds**: the Lex Machina magistrateJudgeIds

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.magistrate_judge_data import MagistrateJudgeData
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
    api_instance = openapi_client.JudgesApi(api_client)
    magistrate_judge_ids = [56] # List[int] | 

    try:
        # Get Magistrates
        api_response = api_instance.get_magistrates_magistrate_judges_get(magistrate_judge_ids)
        print("The response of JudgesApi->get_magistrates_magistrate_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_magistrates_magistrate_judges_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **magistrate_judge_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[MagistrateJudgeData]**](MagistrateJudgeData.md)

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

# **get_state_judge_state_judges_state_judge_id_get**
> StateJudgeData get_state_judge_state_judges_state_judge_id_get(state_judge_id)

Get State Judge

Gets data on a single state judge.  - **state_judge_id**: the Lex Machina stateJudgeId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.state_judge_data import StateJudgeData
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
    api_instance = openapi_client.JudgesApi(api_client)
    state_judge_id = 56 # int | 

    try:
        # Get State Judge
        api_response = api_instance.get_state_judge_state_judges_state_judge_id_get(state_judge_id)
        print("The response of JudgesApi->get_state_judge_state_judges_state_judge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_state_judge_state_judges_state_judge_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_judge_id** | **int**|  | 

### Return type

[**StateJudgeData**](StateJudgeData.md)

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

# **get_state_judges_state_judges_get**
> List[StateJudgeData] get_state_judges_state_judges_get(state_judge_ids)

Get State Judges

Gets data on one or more single state judges.  - **stateJudgeIds**: the Lex Machina stateJudgeIds

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.state_judge_data import StateJudgeData
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
    api_instance = openapi_client.JudgesApi(api_client)
    state_judge_ids = [56] # List[int] | 

    try:
        # Get State Judges
        api_response = api_instance.get_state_judges_state_judges_get(state_judge_ids)
        print("The response of JudgesApi->get_state_judges_state_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_state_judges_state_judges_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_judge_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[StateJudgeData]**](StateJudgeData.md)

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

# **search_judges_search_judges_get**
> JudgeSearchResult search_judges_search_judges_get(q)

Search Judges

Searches for attorneys.  - **q**: the query string  This matches from the beginning of the last name. The search query \"hof\" will match the name \"Hoffman\" but will not match \"Schofield\".

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.judge_search_result import JudgeSearchResult
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
    api_instance = openapi_client.JudgesApi(api_client)
    q = 'q_example' # str | 

    try:
        # Search Judges
        api_response = api_instance.search_judges_search_judges_get(q)
        print("The response of JudgesApi->search_judges_search_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->search_judges_search_judges_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 

### Return type

[**JudgeSearchResult**](JudgeSearchResult.md)

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


# lexmachina.JudgesApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bankruptcy_judge**](JudgesApi.md#get_bankruptcy_judge) | **GET** /bankruptcy-judges/{bankruptcy_judge_id} | Get Bankruptcy Judge
[**get_bankruptcy_judges**](JudgesApi.md#get_bankruptcy_judges) | **GET** /bankruptcy-judges | Get Bankruptcy Judges
[**get_federal_judge**](JudgesApi.md#get_federal_judge) | **GET** /federal-judges/{federal_judge_id} | Get Federal Judge
[**get_federal_judges**](JudgesApi.md#get_federal_judges) | **GET** /federal-judges | Get Federal Judges
[**get_magistrate**](JudgesApi.md#get_magistrate) | **GET** /magistrate-judges/{magistrate_judge_id} | Get Magistrate
[**get_magistrates**](JudgesApi.md#get_magistrates) | **GET** /magistrate-judges | Get Magistrates
[**get_state_judge**](JudgesApi.md#get_state_judge) | **GET** /state-judges/{state_judge_id} | Get State Judge
[**get_state_judges**](JudgesApi.md#get_state_judges) | **GET** /state-judges | Get State Judges
[**search_judges**](JudgesApi.md#search_judges) | **GET** /search-judges | Search Judges


# **get_bankruptcy_judge**
> BankruptcyJudgeData get_bankruptcy_judge(bankruptcy_judge_id)

Get Bankruptcy Judge

Gets data for a single federal bankruptcy judge.

- **bankruptcy_judge_id**: the Lex Machina bankruptcyJudgeId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.bankruptcy_judge_data import BankruptcyJudgeData
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
    api_instance = lexmachina.JudgesApi(api_client)
    bankruptcy_judge_id = 56 # int | 

    try:
        # Get Bankruptcy Judge
        api_response = api_instance.get_bankruptcy_judge(bankruptcy_judge_id)
        print("The response of JudgesApi->get_bankruptcy_judge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_bankruptcy_judge: %s\n" % e)
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

# **get_bankruptcy_judges**
> List[BankruptcyJudgeData] get_bankruptcy_judges(bankruptcy_judge_ids)

Get Bankruptcy Judges

Gets data for one or more federal bankruptcy judges.

- **attorneyIds**: the Lex Machina bankruptcyJudgeIds

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.bankruptcy_judge_data import BankruptcyJudgeData
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
    api_instance = lexmachina.JudgesApi(api_client)
    bankruptcy_judge_ids = [56] # List[int] | 

    try:
        # Get Bankruptcy Judges
        api_response = api_instance.get_bankruptcy_judges(bankruptcy_judge_ids)
        print("The response of JudgesApi->get_bankruptcy_judges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_bankruptcy_judges: %s\n" % e)
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

# **get_federal_judge**
> FederalJudgeData get_federal_judge(federal_judge_id)

Get Federal Judge

Gets data for a single federal Article III judge.

- **judge_id**: the judge id

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.federal_judge_data import FederalJudgeData
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
    api_instance = lexmachina.JudgesApi(api_client)
    federal_judge_id = 56 # int | 

    try:
        # Get Federal Judge
        api_response = api_instance.get_federal_judge(federal_judge_id)
        print("The response of JudgesApi->get_federal_judge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_federal_judge: %s\n" % e)
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

# **get_federal_judges**
> List[FederalJudgeData] get_federal_judges(federal_judge_ids)

Get Federal Judges

Gets data for one or more federal Article III judges.

- **judgeIds**: the judge Ids

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.federal_judge_data import FederalJudgeData
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
    api_instance = lexmachina.JudgesApi(api_client)
    federal_judge_ids = [56] # List[int] | 

    try:
        # Get Federal Judges
        api_response = api_instance.get_federal_judges(federal_judge_ids)
        print("The response of JudgesApi->get_federal_judges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_federal_judges: %s\n" % e)
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

# **get_magistrate**
> MagistrateJudgeData get_magistrate(magistrate_judge_id)

Get Magistrate

Gets data for a single federal magistrate judge.

- **magistrate_judge_id**: the Lex Machina magistrateJudgeId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.magistrate_judge_data import MagistrateJudgeData
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
    api_instance = lexmachina.JudgesApi(api_client)
    magistrate_judge_id = 56 # int | 

    try:
        # Get Magistrate
        api_response = api_instance.get_magistrate(magistrate_judge_id)
        print("The response of JudgesApi->get_magistrate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_magistrate: %s\n" % e)
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

# **get_magistrates**
> List[MagistrateJudgeData] get_magistrates(magistrate_judge_ids)

Get Magistrates

Gets data for a one or more federal magistrate judges.

- **magistrateJudgeIds**: the Lex Machina magistrateJudgeIds

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.magistrate_judge_data import MagistrateJudgeData
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
    api_instance = lexmachina.JudgesApi(api_client)
    magistrate_judge_ids = [56] # List[int] | 

    try:
        # Get Magistrates
        api_response = api_instance.get_magistrates(magistrate_judge_ids)
        print("The response of JudgesApi->get_magistrates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_magistrates: %s\n" % e)
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

# **get_state_judge**
> StateJudgeData get_state_judge(state_judge_id)

Get State Judge

Gets data on a single state judge.

- **state_judge_id**: the Lex Machina stateJudgeId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.state_judge_data import StateJudgeData
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
    api_instance = lexmachina.JudgesApi(api_client)
    state_judge_id = 56 # int | 

    try:
        # Get State Judge
        api_response = api_instance.get_state_judge(state_judge_id)
        print("The response of JudgesApi->get_state_judge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_state_judge: %s\n" % e)
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

# **get_state_judges**
> List[StateJudgeData] get_state_judges(state_judge_ids)

Get State Judges

Gets data on one or more single state judges.

- **stateJudgeIds**: the Lex Machina stateJudgeIds

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.state_judge_data import StateJudgeData
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
    api_instance = lexmachina.JudgesApi(api_client)
    state_judge_ids = [56] # List[int] | 

    try:
        # Get State Judges
        api_response = api_instance.get_state_judges(state_judge_ids)
        print("The response of JudgesApi->get_state_judges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->get_state_judges: %s\n" % e)
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

# **search_judges**
> JudgeSearchResult search_judges(q)

Search Judges

Searches for attorneys.

- **q**: the query string

This matches from the beginning of the last name. The search query "hof" will match the name "Hoffman" but will not match "Schofield".

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.judge_search_result import JudgeSearchResult
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
    api_instance = lexmachina.JudgesApi(api_client)
    q = 'q_example' # str | 

    try:
        # Search Judges
        api_response = api_instance.search_judges(q)
        print("The response of JudgesApi->search_judges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JudgesApi->search_judges: %s\n" % e)
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


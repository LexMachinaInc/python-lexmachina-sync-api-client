# openapi_client.EntitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attorney_attorneys_attorney_id_get**](EntitiesApi.md#get_attorney_attorneys_attorney_id_get) | **GET** /attorneys/{attorney_id} | Get Attorney
[**get_attorneys_attorneys_get**](EntitiesApi.md#get_attorneys_attorneys_get) | **GET** /attorneys | Get Attorneys
[**get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get**](EntitiesApi.md#get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get) | **GET** /bankruptcy-judges/{bankruptcy_judge_id} | Get Bankruptcy Judge
[**get_bankruptcy_judges_bankruptcy_judges_get**](EntitiesApi.md#get_bankruptcy_judges_bankruptcy_judges_get) | **GET** /bankruptcy-judges | Get Bankruptcy Judges
[**get_federal_judge_federal_judges_federal_judge_id_get**](EntitiesApi.md#get_federal_judge_federal_judges_federal_judge_id_get) | **GET** /federal-judges/{federal_judge_id} | Get Federal Judge
[**get_federal_judges_federal_judges_get**](EntitiesApi.md#get_federal_judges_federal_judges_get) | **GET** /federal-judges | Get Federal Judges
[**get_law_firm_law_firms_law_firm_id_get**](EntitiesApi.md#get_law_firm_law_firms_law_firm_id_get) | **GET** /law-firms/{law_firm_id} | Get Law Firm
[**get_law_firms_law_firms_get**](EntitiesApi.md#get_law_firms_law_firms_get) | **GET** /law-firms | Get Law Firms
[**get_magistrate_magistrate_judges_magistrate_judge_id_get**](EntitiesApi.md#get_magistrate_magistrate_judges_magistrate_judge_id_get) | **GET** /magistrate-judges/{magistrate_judge_id} | Get Magistrate
[**get_magistrates_magistrate_judges_get**](EntitiesApi.md#get_magistrates_magistrate_judges_get) | **GET** /magistrate-judges | Get Magistrates
[**get_parties_parties_get**](EntitiesApi.md#get_parties_parties_get) | **GET** /parties | Get Parties
[**get_party_parties_party_id_get**](EntitiesApi.md#get_party_parties_party_id_get) | **GET** /parties/{party_id} | Get Party
[**get_state_judge_state_judges_state_judge_id_get**](EntitiesApi.md#get_state_judge_state_judges_state_judge_id_get) | **GET** /state-judges/{state_judge_id} | Get State Judge
[**get_state_judges_state_judges_get**](EntitiesApi.md#get_state_judges_state_judges_get) | **GET** /state-judges | Get State Judges


# **get_attorney_attorneys_attorney_id_get**
> ResponseGetAttorneyAttorneysAttorneyIdGet get_attorney_attorneys_attorney_id_get(attorney_id)

Get Attorney

Gets data for a single attorney.  - **attorney_id**: the Lex Machina attorneyId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.response_get_attorney_attorneys_attorney_id_get import ResponseGetAttorneyAttorneysAttorneyIdGet
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
    api_instance = openapi_client.EntitiesApi(api_client)
    attorney_id = 56 # int | 

    try:
        # Get Attorney
        api_response = api_instance.get_attorney_attorneys_attorney_id_get(attorney_id)
        print("The response of EntitiesApi->get_attorney_attorneys_attorney_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_attorney_attorneys_attorney_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_id** | **int**|  | 

### Return type

[**ResponseGetAttorneyAttorneysAttorneyIdGet**](ResponseGetAttorneyAttorneysAttorneyIdGet.md)

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

# **get_attorneys_attorneys_get**
> List[GetAttorneysAttorneysGet200ResponseInner] get_attorneys_attorneys_get(attorney_ids)

Get Attorneys

Gets data for one or more attorneys.  - **attorneyIds**: the Lex Machina attorneyIds  If any of the the attorneyIds given are not the current lexmachina attorneyId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.get_attorneys_attorneys_get200_response_inner import GetAttorneysAttorneysGet200ResponseInner
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
    api_instance = openapi_client.EntitiesApi(api_client)
    attorney_ids = [56] # List[int] | 

    try:
        # Get Attorneys
        api_response = api_instance.get_attorneys_attorneys_get(attorney_ids)
        print("The response of EntitiesApi->get_attorneys_attorneys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_attorneys_attorneys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetAttorneysAttorneysGet200ResponseInner]**](GetAttorneysAttorneysGet200ResponseInner.md)

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
    api_instance = openapi_client.EntitiesApi(api_client)
    bankruptcy_judge_id = 56 # int | 

    try:
        # Get Bankruptcy Judge
        api_response = api_instance.get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get(bankruptcy_judge_id)
        print("The response of EntitiesApi->get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_bankruptcy_judge_bankruptcy_judges_bankruptcy_judge_id_get: %s\n" % e)
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
    api_instance = openapi_client.EntitiesApi(api_client)
    bankruptcy_judge_ids = [56] # List[int] | 

    try:
        # Get Bankruptcy Judges
        api_response = api_instance.get_bankruptcy_judges_bankruptcy_judges_get(bankruptcy_judge_ids)
        print("The response of EntitiesApi->get_bankruptcy_judges_bankruptcy_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_bankruptcy_judges_bankruptcy_judges_get: %s\n" % e)
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
    api_instance = openapi_client.EntitiesApi(api_client)
    federal_judge_id = 56 # int | 

    try:
        # Get Federal Judge
        api_response = api_instance.get_federal_judge_federal_judges_federal_judge_id_get(federal_judge_id)
        print("The response of EntitiesApi->get_federal_judge_federal_judges_federal_judge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_federal_judge_federal_judges_federal_judge_id_get: %s\n" % e)
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
    api_instance = openapi_client.EntitiesApi(api_client)
    federal_judge_ids = [56] # List[int] | 

    try:
        # Get Federal Judges
        api_response = api_instance.get_federal_judges_federal_judges_get(federal_judge_ids)
        print("The response of EntitiesApi->get_federal_judges_federal_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_federal_judges_federal_judges_get: %s\n" % e)
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

# **get_law_firm_law_firms_law_firm_id_get**
> ResponseGetLawFirmLawFirmsLawFirmIdGet get_law_firm_law_firms_law_firm_id_get(law_firm_id)

Get Law Firm

Gets data for a single law firm.  - **law_firm_id**: the Lex Machina lawFirmID

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.response_get_law_firm_law_firms_law_firm_id_get import ResponseGetLawFirmLawFirmsLawFirmIdGet
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
    api_instance = openapi_client.EntitiesApi(api_client)
    law_firm_id = 56 # int | 

    try:
        # Get Law Firm
        api_response = api_instance.get_law_firm_law_firms_law_firm_id_get(law_firm_id)
        print("The response of EntitiesApi->get_law_firm_law_firms_law_firm_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_law_firm_law_firms_law_firm_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **law_firm_id** | **int**|  | 

### Return type

[**ResponseGetLawFirmLawFirmsLawFirmIdGet**](ResponseGetLawFirmLawFirmsLawFirmIdGet.md)

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

# **get_law_firms_law_firms_get**
> List[GetLawFirmsLawFirmsGet200ResponseInner] get_law_firms_law_firms_get(law_firm_ids)

Get Law Firms

Gets data for one or more law firms.  - **lawFirmIds**: the Lex Machina lawFirmIds  If any of the the lawFirmIds given are not the current lexmachina lawFirmId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.get_law_firms_law_firms_get200_response_inner import GetLawFirmsLawFirmsGet200ResponseInner
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
    api_instance = openapi_client.EntitiesApi(api_client)
    law_firm_ids = [56] # List[int] | 

    try:
        # Get Law Firms
        api_response = api_instance.get_law_firms_law_firms_get(law_firm_ids)
        print("The response of EntitiesApi->get_law_firms_law_firms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_law_firms_law_firms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **law_firm_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetLawFirmsLawFirmsGet200ResponseInner]**](GetLawFirmsLawFirmsGet200ResponseInner.md)

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
    api_instance = openapi_client.EntitiesApi(api_client)
    magistrate_judge_id = 56 # int | 

    try:
        # Get Magistrate
        api_response = api_instance.get_magistrate_magistrate_judges_magistrate_judge_id_get(magistrate_judge_id)
        print("The response of EntitiesApi->get_magistrate_magistrate_judges_magistrate_judge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_magistrate_magistrate_judges_magistrate_judge_id_get: %s\n" % e)
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
    api_instance = openapi_client.EntitiesApi(api_client)
    magistrate_judge_ids = [56] # List[int] | 

    try:
        # Get Magistrates
        api_response = api_instance.get_magistrates_magistrate_judges_get(magistrate_judge_ids)
        print("The response of EntitiesApi->get_magistrates_magistrate_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_magistrates_magistrate_judges_get: %s\n" % e)
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

# **get_parties_parties_get**
> List[GetPartiesPartiesGet200ResponseInner] get_parties_parties_get(party_ids)

Get Parties

Gets data for one or more parties.  - **partyIds**: the Lex Machina partyIds  If any of the the partyIds given are not the current lexmachina partyId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.get_parties_parties_get200_response_inner import GetPartiesPartiesGet200ResponseInner
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
    api_instance = openapi_client.EntitiesApi(api_client)
    party_ids = [56] # List[int] | 

    try:
        # Get Parties
        api_response = api_instance.get_parties_parties_get(party_ids)
        print("The response of EntitiesApi->get_parties_parties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_parties_parties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetPartiesPartiesGet200ResponseInner]**](GetPartiesPartiesGet200ResponseInner.md)

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

# **get_party_parties_party_id_get**
> ResponseGetPartyPartiesPartyIdGet get_party_parties_party_id_get(party_id)

Get Party

Gets data for a single party.  - **party_id**: the Lex Machina partyId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import openapi_client
from openapi_client.models.response_get_party_parties_party_id_get import ResponseGetPartyPartiesPartyIdGet
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
    api_instance = openapi_client.EntitiesApi(api_client)
    party_id = 56 # int | 

    try:
        # Get Party
        api_response = api_instance.get_party_parties_party_id_get(party_id)
        print("The response of EntitiesApi->get_party_parties_party_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_party_parties_party_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_id** | **int**|  | 

### Return type

[**ResponseGetPartyPartiesPartyIdGet**](ResponseGetPartyPartiesPartyIdGet.md)

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
    api_instance = openapi_client.EntitiesApi(api_client)
    state_judge_id = 56 # int | 

    try:
        # Get State Judge
        api_response = api_instance.get_state_judge_state_judges_state_judge_id_get(state_judge_id)
        print("The response of EntitiesApi->get_state_judge_state_judges_state_judge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_state_judge_state_judges_state_judge_id_get: %s\n" % e)
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
    api_instance = openapi_client.EntitiesApi(api_client)
    state_judge_ids = [56] # List[int] | 

    try:
        # Get State Judges
        api_response = api_instance.get_state_judges_state_judges_get(state_judge_ids)
        print("The response of EntitiesApi->get_state_judges_state_judges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_state_judges_state_judges_get: %s\n" % e)
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


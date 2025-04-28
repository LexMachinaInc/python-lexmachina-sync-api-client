# lexmachina.EntitiesApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attorney**](EntitiesApi.md#get_attorney) | **GET** /attorneys/{attorney_id} | Get Attorney
[**get_attorneys**](EntitiesApi.md#get_attorneys) | **GET** /attorneys | Get Attorneys
[**get_bankruptcy_judge**](EntitiesApi.md#get_bankruptcy_judge) | **GET** /bankruptcy-judges/{bankruptcy_judge_id} | Get Bankruptcy Judge
[**get_bankruptcy_judges**](EntitiesApi.md#get_bankruptcy_judges) | **GET** /bankruptcy-judges | Get Bankruptcy Judges
[**get_federal_judge**](EntitiesApi.md#get_federal_judge) | **GET** /federal-judges/{federal_judge_id} | Get Federal Judge
[**get_federal_judges**](EntitiesApi.md#get_federal_judges) | **GET** /federal-judges | Get Federal Judges
[**get_law_firm**](EntitiesApi.md#get_law_firm) | **GET** /law-firms/{law_firm_id} | Get Law Firm
[**get_law_firms**](EntitiesApi.md#get_law_firms) | **GET** /law-firms | Get Law Firms
[**get_magistrate**](EntitiesApi.md#get_magistrate) | **GET** /magistrate-judges/{magistrate_judge_id} | Get Magistrate
[**get_magistrates**](EntitiesApi.md#get_magistrates) | **GET** /magistrate-judges | Get Magistrates
[**get_parties**](EntitiesApi.md#get_parties) | **GET** /parties | Get Parties
[**get_party**](EntitiesApi.md#get_party) | **GET** /parties/{party_id} | Get Party
[**get_state_judge**](EntitiesApi.md#get_state_judge) | **GET** /state-judges/{state_judge_id} | Get State Judge
[**get_state_judges**](EntitiesApi.md#get_state_judges) | **GET** /state-judges | Get State Judges


# **get_attorney**
> ResponseGetAttorneyAttorneysAttorneyIdGet get_attorney(attorney_id)

Get Attorney

Gets data for a single attorney.

- **attorney_id**: the Lex Machina attorneyId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.response_get_attorney_attorneys_attorney_id_get import ResponseGetAttorneyAttorneysAttorneyIdGet
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
    api_instance = lexmachina.EntitiesApi(api_client)
    attorney_id = 56 # int | 

    try:
        # Get Attorney
        api_response = api_instance.get_attorney(attorney_id)
        print("The response of EntitiesApi->get_attorney:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_attorney: %s\n" % e)
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

# **get_attorneys**
> List[GetAttorneys200ResponseInner] get_attorneys(attorney_ids)

Get Attorneys

Gets data for one or more attorneys.

- **attorneyIds**: the Lex Machina attorneyIds

If any of the the attorneyIds given are not the current lexmachina attorneyId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.get_attorneys200_response_inner import GetAttorneys200ResponseInner
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
    api_instance = lexmachina.EntitiesApi(api_client)
    attorney_ids = [56] # List[int] | 

    try:
        # Get Attorneys
        api_response = api_instance.get_attorneys(attorney_ids)
        print("The response of EntitiesApi->get_attorneys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_attorneys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attorney_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetAttorneys200ResponseInner]**](GetAttorneys200ResponseInner.md)

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
    api_instance = lexmachina.EntitiesApi(api_client)
    bankruptcy_judge_id = 56 # int | 

    try:
        # Get Bankruptcy Judge
        api_response = api_instance.get_bankruptcy_judge(bankruptcy_judge_id)
        print("The response of EntitiesApi->get_bankruptcy_judge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_bankruptcy_judge: %s\n" % e)
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
    api_instance = lexmachina.EntitiesApi(api_client)
    bankruptcy_judge_ids = [56] # List[int] | 

    try:
        # Get Bankruptcy Judges
        api_response = api_instance.get_bankruptcy_judges(bankruptcy_judge_ids)
        print("The response of EntitiesApi->get_bankruptcy_judges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_bankruptcy_judges: %s\n" % e)
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
    api_instance = lexmachina.EntitiesApi(api_client)
    federal_judge_id = 56 # int | 

    try:
        # Get Federal Judge
        api_response = api_instance.get_federal_judge(federal_judge_id)
        print("The response of EntitiesApi->get_federal_judge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_federal_judge: %s\n" % e)
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
    api_instance = lexmachina.EntitiesApi(api_client)
    federal_judge_ids = [56] # List[int] | 

    try:
        # Get Federal Judges
        api_response = api_instance.get_federal_judges(federal_judge_ids)
        print("The response of EntitiesApi->get_federal_judges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_federal_judges: %s\n" % e)
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

# **get_law_firm**
> ResponseGetLawFirmLawFirmsLawFirmIdGet get_law_firm(law_firm_id)

Get Law Firm

Gets data for a single law firm.

- **law_firm_id**: the Lex Machina lawFirmID

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.response_get_law_firm_law_firms_law_firm_id_get import ResponseGetLawFirmLawFirmsLawFirmIdGet
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
    api_instance = lexmachina.EntitiesApi(api_client)
    law_firm_id = 56 # int | 

    try:
        # Get Law Firm
        api_response = api_instance.get_law_firm(law_firm_id)
        print("The response of EntitiesApi->get_law_firm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_law_firm: %s\n" % e)
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

# **get_law_firms**
> List[GetLawFirms200ResponseInner] get_law_firms(law_firm_ids)

Get Law Firms

Gets data for one or more law firms.

- **lawFirmIds**: the Lex Machina lawFirmIds

If any of the the lawFirmIds given are not the current lexmachina lawFirmId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.get_law_firms200_response_inner import GetLawFirms200ResponseInner
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
    api_instance = lexmachina.EntitiesApi(api_client)
    law_firm_ids = [56] # List[int] | 

    try:
        # Get Law Firms
        api_response = api_instance.get_law_firms(law_firm_ids)
        print("The response of EntitiesApi->get_law_firms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_law_firms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **law_firm_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetLawFirms200ResponseInner]**](GetLawFirms200ResponseInner.md)

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
    api_instance = lexmachina.EntitiesApi(api_client)
    magistrate_judge_id = 56 # int | 

    try:
        # Get Magistrate
        api_response = api_instance.get_magistrate(magistrate_judge_id)
        print("The response of EntitiesApi->get_magistrate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_magistrate: %s\n" % e)
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
    api_instance = lexmachina.EntitiesApi(api_client)
    magistrate_judge_ids = [56] # List[int] | 

    try:
        # Get Magistrates
        api_response = api_instance.get_magistrates(magistrate_judge_ids)
        print("The response of EntitiesApi->get_magistrates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_magistrates: %s\n" % e)
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

# **get_parties**
> List[GetParties200ResponseInner] get_parties(party_ids)

Get Parties

Gets data for one or more parties.

- **partyIds**: the Lex Machina partyIds

If any of the the partyIds given are not the current lexmachina partyId, the results will include inputId for disambugation

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.get_parties200_response_inner import GetParties200ResponseInner
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
    api_instance = lexmachina.EntitiesApi(api_client)
    party_ids = [56] # List[int] | 

    try:
        # Get Parties
        api_response = api_instance.get_parties(party_ids)
        print("The response of EntitiesApi->get_parties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_parties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_ids** | [**List[int]**](int.md)|  | 

### Return type

[**List[GetParties200ResponseInner]**](GetParties200ResponseInner.md)

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

# **get_party**
> ResponseGetPartyPartiesPartyIdGet get_party(party_id)

Get Party

Gets data for a single party.

- **party_id**: the Lex Machina partyId

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.response_get_party_parties_party_id_get import ResponseGetPartyPartiesPartyIdGet
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
    api_instance = lexmachina.EntitiesApi(api_client)
    party_id = 56 # int | 

    try:
        # Get Party
        api_response = api_instance.get_party(party_id)
        print("The response of EntitiesApi->get_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_party: %s\n" % e)
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
    api_instance = lexmachina.EntitiesApi(api_client)
    state_judge_id = 56 # int | 

    try:
        # Get State Judge
        api_response = api_instance.get_state_judge(state_judge_id)
        print("The response of EntitiesApi->get_state_judge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_state_judge: %s\n" % e)
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
    api_instance = lexmachina.EntitiesApi(api_client)
    state_judge_ids = [56] # List[int] | 

    try:
        # Get State Judges
        api_response = api_instance.get_state_judges(state_judge_ids)
        print("The response of EntitiesApi->get_state_judges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_state_judges: %s\n" % e)
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


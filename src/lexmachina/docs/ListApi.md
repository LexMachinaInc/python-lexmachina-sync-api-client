# lexmachina.ListApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_appealability_rulings**](ListApi.md#list_appealability_rulings) | **GET** /list-appealability-rulings | List Appealability Rulings
[**list_appellate_decisions**](ListApi.md#list_appellate_decisions) | **GET** /list-appellate-decisions/FederalDistrict | List Appellate Decisions
[**list_case_resolutions**](ListApi.md#list_case_resolutions) | **GET** /list-case-resolutions/{court_type} | List Case Resolutions
[**list_case_tags**](ListApi.md#list_case_tags) | **GET** /list-case-tags/{court_type} | List Case Tags
[**list_case_types**](ListApi.md#list_case_types) | **GET** /list-case-types/{court_type} | List Case Types
[**list_courts**](ListApi.md#list_courts) | **GET** /list-courts/{court_type} | List Courts
[**list_events**](ListApi.md#list_events) | **GET** /list-events/{court_type} | List Events
[**list_federal_district_damages**](ListApi.md#list_federal_district_damages) | **GET** /list-damages/FederalDistrict | List Federal District Damages
[**list_federal_district_findings**](ListApi.md#list_federal_district_findings) | **GET** /list-findings/FederalDistrict | List Federal District Findings
[**list_judgment_events**](ListApi.md#list_judgment_events) | **GET** /list-judgment-events/State | List Judgment Events
[**list_judgment_sources**](ListApi.md#list_judgment_sources) | **GET** /list-judgment-sources/FederalDistrict | List Judgment Sources
[**list_originating_venues**](ListApi.md#list_originating_venues) | **GET** /list-originating-venues/FederalAppeals | List Originating Venues
[**list_state_damages**](ListApi.md#list_state_damages) | **GET** /list-damages/State | List State Damages
[**list_supreme_court_decisions**](ListApi.md#list_supreme_court_decisions) | **GET** /list-supreme-court-decisions/FederalAppeals | List Supreme Court Decisions


# **list_appealability_rulings**
> object list_appealability_rulings()

List Appealability Rulings

Lists appealability rulings for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List Appealability Rulings
        api_response = api_instance.list_appealability_rulings()
        print("The response of ListApi->list_appealability_rulings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_appealability_rulings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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

# **list_appellate_decisions**
> List[Optional[str]] list_appellate_decisions()

List Appellate Decisions

Lists appellate decisions for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List Appellate Decisions
        api_response = api_instance.list_appellate_decisions()
        print("The response of ListApi->list_appellate_decisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_appellate_decisions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Optional[str]]**

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

# **list_case_resolutions**
> CaseResolutionsList list_case_resolutions(court_type)

List Case Resolutions

Lists case resolutions given court type for use with querying.

- **court_type**: the relevant court type

Each resoltuon has both a summary and specific field which are valid in combinations listed.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.case_resolutions_list import CaseResolutionsList
from lexmachina.models.court_type import CourtType
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
    api_instance = lexmachina.ListApi(api_client)
    court_type = lexmachina.CourtType() # CourtType | 

    try:
        # List Case Resolutions
        api_response = api_instance.list_case_resolutions(court_type)
        print("The response of ListApi->list_case_resolutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_case_resolutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_type** | [**CourtType**](.md)|  | 

### Return type

[**CaseResolutionsList**](CaseResolutionsList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_case_tags**
> List[CaseTagsList] list_case_tags(court_type)

List Case Tags

Lists case tags for a given court type for use with querying.

- **court_type**: the relevant court type

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.case_tags_list import CaseTagsList
from lexmachina.models.court_type import CourtType
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
    api_instance = lexmachina.ListApi(api_client)
    court_type = lexmachina.CourtType() # CourtType | 

    try:
        # List Case Tags
        api_response = api_instance.list_case_tags(court_type)
        print("The response of ListApi->list_case_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_case_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_type** | [**CourtType**](.md)|  | 

### Return type

[**List[CaseTagsList]**](CaseTagsList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_case_types**
> List[CaseTypesList] list_case_types(court_type)

List Case Types

Lists case tags for a given court type for use with querying.

- **court_type**: the relevant court type

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.case_types_list import CaseTypesList
from lexmachina.models.court_type import CourtType
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
    api_instance = lexmachina.ListApi(api_client)
    court_type = lexmachina.CourtType() # CourtType | 

    try:
        # List Case Types
        api_response = api_instance.list_case_types(court_type)
        print("The response of ListApi->list_case_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_case_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_type** | [**CourtType**](.md)|  | 

### Return type

[**List[CaseTypesList]**](CaseTypesList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_courts**
> ResponseListCourtsListCourtsCourtTypeGet list_courts(court_type)

List Courts

Lists courts for a given court type. For use with querying or determining which courts data is avilable for.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.court_type import CourtType
from lexmachina.models.response_list_courts_list_courts_court_type_get import ResponseListCourtsListCourtsCourtTypeGet
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
    api_instance = lexmachina.ListApi(api_client)
    court_type = lexmachina.CourtType() # CourtType | 

    try:
        # List Courts
        api_response = api_instance.list_courts(court_type)
        print("The response of ListApi->list_courts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_courts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_type** | [**CourtType**](.md)|  | 

### Return type

[**ResponseListCourtsListCourtsCourtTypeGet**](ResponseListCourtsListCourtsCourtTypeGet.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events**
> EventsList list_events(court_type)

List Events

Lists events for a given for a given court type for use with querying.

- **court_type**: the relevant court type

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.court_type import CourtType
from lexmachina.models.events_list import EventsList
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
    api_instance = lexmachina.ListApi(api_client)
    court_type = lexmachina.CourtType() # CourtType | 

    try:
        # List Events
        api_response = api_instance.list_events(court_type)
        print("The response of ListApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **court_type** | [**CourtType**](.md)|  | 

### Return type

[**EventsList**](EventsList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_federal_district_damages**
> FederalDistrictDamagesList list_federal_district_damages()

List Federal District Damages

Lists of damages for Federal District courts organized by practice area for use with querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.federal_district_damages_list import FederalDistrictDamagesList
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List Federal District Damages
        api_response = api_instance.list_federal_district_damages()
        print("The response of ListApi->list_federal_district_damages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_federal_district_damages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FederalDistrictDamagesList**](FederalDistrictDamagesList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_federal_district_findings**
> FederalDistrictFindingsList list_federal_district_findings()

List Federal District Findings

Lists findings for Federal District courts organized by practice area for use with querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.federal_district_findings_list import FederalDistrictFindingsList
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List Federal District Findings
        api_response = api_instance.list_federal_district_findings()
        print("The response of ListApi->list_federal_district_findings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_federal_district_findings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FederalDistrictFindingsList**](FederalDistrictFindingsList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_judgment_events**
> JudgmentEventsList list_judgment_events()

List Judgment Events

Lists judgment events for State courts organized for use with querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.judgment_events_list import JudgmentEventsList
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List Judgment Events
        api_response = api_instance.list_judgment_events()
        print("The response of ListApi->list_judgment_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_judgment_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JudgmentEventsList**](JudgmentEventsList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_judgment_sources**
> JudgmentSourcesList list_judgment_sources()

List Judgment Sources

Lists judgment sources for Federal District courts for use with querying.

The sources are specific to damages, remedies and findings as presented in the list.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.judgment_sources_list import JudgmentSourcesList
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List Judgment Sources
        api_response = api_instance.list_judgment_sources()
        print("The response of ListApi->list_judgment_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_judgment_sources: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JudgmentSourcesList**](JudgmentSourcesList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_originating_venues**
> OriginatingVenuesList list_originating_venues()

List Originating Venues

Lists originating venues for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.originating_venues_list import OriginatingVenuesList
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List Originating Venues
        api_response = api_instance.list_originating_venues()
        print("The response of ListApi->list_originating_venues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_originating_venues: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OriginatingVenuesList**](OriginatingVenuesList.md)

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

# **list_state_damages**
> StateDamagesList list_state_damages()

List State Damages

Lists of damages for State courts organized by practice area for use with querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.state_damages_list import StateDamagesList
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List State Damages
        api_response = api_instance.list_state_damages()
        print("The response of ListApi->list_state_damages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_state_damages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StateDamagesList**](StateDamagesList.md)

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
**404** | Not Found |  -  |
**422** | Invalid Input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supreme_court_decisions**
> List[Optional[str]] list_supreme_court_decisions()

List Supreme Court Decisions

Lists decisions from the Supreme Court for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
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
    api_instance = lexmachina.ListApi(api_client)

    try:
        # List Supreme Court Decisions
        api_response = api_instance.list_supreme_court_decisions()
        print("The response of ListApi->list_supreme_court_decisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_supreme_court_decisions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Optional[str]]**

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


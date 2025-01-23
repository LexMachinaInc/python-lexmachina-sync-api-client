# lawmachine.ListApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_appealability_rulings_list_appealability_rulings_get**](ListApi.md#list_appealability_rulings_list_appealability_rulings_get) | **GET** /list-appealability-rulings | List Appealability Rulings
[**list_appellate_decisions_list_appellate_decisions_federal_district_get**](ListApi.md#list_appellate_decisions_list_appellate_decisions_federal_district_get) | **GET** /list-appellate-decisions/FederalDistrict | List Appellate Decisions
[**list_case_resolutions_list_case_resolutions_court_type_get**](ListApi.md#list_case_resolutions_list_case_resolutions_court_type_get) | **GET** /list-case-resolutions/{court_type} | List Case Resolutions
[**list_case_tags_list_case_tags_court_type_get**](ListApi.md#list_case_tags_list_case_tags_court_type_get) | **GET** /list-case-tags/{court_type} | List Case Tags
[**list_case_types_list_case_types_court_type_get**](ListApi.md#list_case_types_list_case_types_court_type_get) | **GET** /list-case-types/{court_type} | List Case Types
[**list_courts_list_courts_court_type_get**](ListApi.md#list_courts_list_courts_court_type_get) | **GET** /list-courts/{court_type} | List Courts
[**list_events_list_events_court_type_get**](ListApi.md#list_events_list_events_court_type_get) | **GET** /list-events/{court_type} | List Events
[**list_federal_district_damages_list_damages_federal_district_get**](ListApi.md#list_federal_district_damages_list_damages_federal_district_get) | **GET** /list-damages/FederalDistrict | List Federal District Damages
[**list_federal_district_findings_list_findings_federal_district_get**](ListApi.md#list_federal_district_findings_list_findings_federal_district_get) | **GET** /list-findings/FederalDistrict | List Federal District Findings
[**list_judgment_events_list_judgment_events_state_get**](ListApi.md#list_judgment_events_list_judgment_events_state_get) | **GET** /list-judgment-events/State | List Judgment Events
[**list_judgment_sources_list_judgment_sources_federal_district_get**](ListApi.md#list_judgment_sources_list_judgment_sources_federal_district_get) | **GET** /list-judgment-sources/FederalDistrict | List Judgment Sources
[**list_originating_venues_list_originating_venues_federal_appeals_get**](ListApi.md#list_originating_venues_list_originating_venues_federal_appeals_get) | **GET** /list-originating-venues/FederalAppeals | List Originating Venues
[**list_state_damages_list_damages_state_get**](ListApi.md#list_state_damages_list_damages_state_get) | **GET** /list-damages/State | List State Damages
[**list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get**](ListApi.md#list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get) | **GET** /list-supreme-court-decisions/FederalAppeals | List Supreme Court Decisions


# **list_appealability_rulings_list_appealability_rulings_get**
> object list_appealability_rulings_list_appealability_rulings_get()

List Appealability Rulings

Lists appealability rulings for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List Appealability Rulings
        api_response = api_instance.list_appealability_rulings_list_appealability_rulings_get()
        print("The response of ListApi->list_appealability_rulings_list_appealability_rulings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_appealability_rulings_list_appealability_rulings_get: %s\n" % e)
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

# **list_appellate_decisions_list_appellate_decisions_federal_district_get**
> List[Optional[str]] list_appellate_decisions_list_appellate_decisions_federal_district_get()

List Appellate Decisions

Lists appellate decisions for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List Appellate Decisions
        api_response = api_instance.list_appellate_decisions_list_appellate_decisions_federal_district_get()
        print("The response of ListApi->list_appellate_decisions_list_appellate_decisions_federal_district_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_appellate_decisions_list_appellate_decisions_federal_district_get: %s\n" % e)
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

# **list_case_resolutions_list_case_resolutions_court_type_get**
> CaseResolutionsList list_case_resolutions_list_case_resolutions_court_type_get(court_type)

List Case Resolutions

Lists case resolutions given court type for use with querying.  - **court_type**: the relevant court type  Each resoltuon has both a summary and specific field which are valid in combinations listed.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.case_resolutions_list import CaseResolutionsList
from lawmachine.models.court_type import CourtType
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
    api_instance = lawmachine.ListApi(api_client)
    court_type = lawmachine.CourtType() # CourtType | 

    try:
        # List Case Resolutions
        api_response = api_instance.list_case_resolutions_list_case_resolutions_court_type_get(court_type)
        print("The response of ListApi->list_case_resolutions_list_case_resolutions_court_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_case_resolutions_list_case_resolutions_court_type_get: %s\n" % e)
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

# **list_case_tags_list_case_tags_court_type_get**
> List[CaseTagsList] list_case_tags_list_case_tags_court_type_get(court_type)

List Case Tags

Lists case tags for a given court type for use with querying.  - **court_type**: the relevant court type

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.case_tags_list import CaseTagsList
from lawmachine.models.court_type import CourtType
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
    api_instance = lawmachine.ListApi(api_client)
    court_type = lawmachine.CourtType() # CourtType | 

    try:
        # List Case Tags
        api_response = api_instance.list_case_tags_list_case_tags_court_type_get(court_type)
        print("The response of ListApi->list_case_tags_list_case_tags_court_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_case_tags_list_case_tags_court_type_get: %s\n" % e)
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

# **list_case_types_list_case_types_court_type_get**
> List[CaseTypesList] list_case_types_list_case_types_court_type_get(court_type)

List Case Types

Lists case tags for a given court type for use with querying.  - **court_type**: the relevant court type

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.case_types_list import CaseTypesList
from lawmachine.models.court_type import CourtType
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
    api_instance = lawmachine.ListApi(api_client)
    court_type = lawmachine.CourtType() # CourtType | 

    try:
        # List Case Types
        api_response = api_instance.list_case_types_list_case_types_court_type_get(court_type)
        print("The response of ListApi->list_case_types_list_case_types_court_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_case_types_list_case_types_court_type_get: %s\n" % e)
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

# **list_courts_list_courts_court_type_get**
> ResponseListCourtsListCourtsCourtTypeGet list_courts_list_courts_court_type_get(court_type)

List Courts

Lists courts for a given court type. For use with querying or determining which courts data is avilable for.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.court_type import CourtType
from lawmachine.models.response_list_courts_list_courts_court_type_get import ResponseListCourtsListCourtsCourtTypeGet
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
    api_instance = lawmachine.ListApi(api_client)
    court_type = lawmachine.CourtType() # CourtType | 

    try:
        # List Courts
        api_response = api_instance.list_courts_list_courts_court_type_get(court_type)
        print("The response of ListApi->list_courts_list_courts_court_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_courts_list_courts_court_type_get: %s\n" % e)
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

# **list_events_list_events_court_type_get**
> EventsList list_events_list_events_court_type_get(court_type)

List Events

Lists events for a given for a given court type for use with querying.  - **court_type**: the relevant court type

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.court_type import CourtType
from lawmachine.models.events_list import EventsList
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
    api_instance = lawmachine.ListApi(api_client)
    court_type = lawmachine.CourtType() # CourtType | 

    try:
        # List Events
        api_response = api_instance.list_events_list_events_court_type_get(court_type)
        print("The response of ListApi->list_events_list_events_court_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_events_list_events_court_type_get: %s\n" % e)
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

# **list_federal_district_damages_list_damages_federal_district_get**
> FederalDistrictDamagesList list_federal_district_damages_list_damages_federal_district_get()

List Federal District Damages

Lists of damages for Federal District courts organized by practice area for use with querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.federal_district_damages_list import FederalDistrictDamagesList
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List Federal District Damages
        api_response = api_instance.list_federal_district_damages_list_damages_federal_district_get()
        print("The response of ListApi->list_federal_district_damages_list_damages_federal_district_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_federal_district_damages_list_damages_federal_district_get: %s\n" % e)
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

# **list_federal_district_findings_list_findings_federal_district_get**
> FederalDistrictFindingsList list_federal_district_findings_list_findings_federal_district_get()

List Federal District Findings

Lists findings for Federal District courts organized by practice area for use with querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.federal_district_findings_list import FederalDistrictFindingsList
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List Federal District Findings
        api_response = api_instance.list_federal_district_findings_list_findings_federal_district_get()
        print("The response of ListApi->list_federal_district_findings_list_findings_federal_district_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_federal_district_findings_list_findings_federal_district_get: %s\n" % e)
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

# **list_judgment_events_list_judgment_events_state_get**
> JudgmentEventsList list_judgment_events_list_judgment_events_state_get()

List Judgment Events

Lists judgment events for State courts organized for use with querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.judgment_events_list import JudgmentEventsList
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List Judgment Events
        api_response = api_instance.list_judgment_events_list_judgment_events_state_get()
        print("The response of ListApi->list_judgment_events_list_judgment_events_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_judgment_events_list_judgment_events_state_get: %s\n" % e)
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

# **list_judgment_sources_list_judgment_sources_federal_district_get**
> JudgmentSourcesList list_judgment_sources_list_judgment_sources_federal_district_get()

List Judgment Sources

Lists judgment sources for Federal District courts for use with querying.  The sources are specific to damages, remedies and findings as presented in the list.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.judgment_sources_list import JudgmentSourcesList
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List Judgment Sources
        api_response = api_instance.list_judgment_sources_list_judgment_sources_federal_district_get()
        print("The response of ListApi->list_judgment_sources_list_judgment_sources_federal_district_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_judgment_sources_list_judgment_sources_federal_district_get: %s\n" % e)
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

# **list_originating_venues_list_originating_venues_federal_appeals_get**
> OriginatingVenuesList list_originating_venues_list_originating_venues_federal_appeals_get()

List Originating Venues

Lists originating venues for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.originating_venues_list import OriginatingVenuesList
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List Originating Venues
        api_response = api_instance.list_originating_venues_list_originating_venues_federal_appeals_get()
        print("The response of ListApi->list_originating_venues_list_originating_venues_federal_appeals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_originating_venues_list_originating_venues_federal_appeals_get: %s\n" % e)
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

# **list_state_damages_list_damages_state_get**
> StateDamagesList list_state_damages_list_damages_state_get()

List State Damages

Lists of damages for State courts organized by practice area for use with querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
from lawmachine.models.state_damages_list import StateDamagesList
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List State Damages
        api_response = api_instance.list_state_damages_list_damages_state_get()
        print("The response of ListApi->list_state_damages_list_damages_state_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_state_damages_list_damages_state_get: %s\n" % e)
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

# **list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get**
> List[Optional[str]] list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get()

List Supreme Court Decisions

Lists decisions from the Supreme Court for use with appeals case querying.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lawmachine
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
    api_instance = lawmachine.ListApi(api_client)

    try:
        # List Supreme Court Decisions
        api_response = api_instance.list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get()
        print("The response of ListApi->list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->list_supreme_court_decisions_list_supreme_court_decisions_federal_appeals_get: %s\n" % e)
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


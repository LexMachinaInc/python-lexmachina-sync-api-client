# lexmachina.FederalDistrictCasesApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_district_case_by_number**](FederalDistrictCasesApi.md#find_district_case_by_number) | **GET** /find-district-cases | Find District Case By Number
[**get_district_case**](FederalDistrictCasesApi.md#get_district_case) | **GET** /district-cases/{district_case_id} | Get District Case
[**query_district_cases**](FederalDistrictCasesApi.md#query_district_cases) | **POST** /query-district-cases | Query District Cases


# **find_district_case_by_number**
> List[DistrictCaseNumberSearchResult] find_district_case_by_number(case_numbers, court=court)

Find District Case By Number

Finds Lex Machina case ids for specified case numbers.

- **case_numbers**: case number search strings
- **court**: optional court to limit results

Matches results for each individual case number is cut off at 1000 match results.

Because case number formats vary, and because the case number for the same case can change over time, the search tries to err on the side of being more inclusive.
So, this may return more results than you expect.
For example, the search ignores judge initials at the end of case numbers.
So, for case number "1:19-cv-00077-NLH-KMW", the trailing initials "NLH" and "KMW" will be ignored.

The court param is optional and can be any of the name versions given by the /list-courts endpoint (must match capitalization).
Providing a value for the court param will filter all case number searches in the request for cases within that court.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.district_case_number_search_result import DistrictCaseNumberSearchResult
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
    api_instance = lexmachina.FederalDistrictCasesApi(api_client)
    case_numbers = ['case_numbers_example'] # List[str] | 
    court = 'court_example' # str |  (optional)

    try:
        # Find District Case By Number
        api_response = api_instance.find_district_case_by_number(case_numbers, court=court)
        print("The response of FederalDistrictCasesApi->find_district_case_by_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalDistrictCasesApi->find_district_case_by_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_numbers** | [**List[str]**](str.md)|  | 
 **court** | **str**|  | [optional] 

### Return type

[**List[DistrictCaseNumberSearchResult]**](DistrictCaseNumberSearchResult.md)

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

# **get_district_case**
> DistrictCaseData get_district_case(district_case_id, docket_retrieval=docket_retrieval)

Get District Case

Gets data for a single federal district case.

- **district_case_id**: the Lex Machina districtCaseId
- **docket_retrieval**: docket retreival mode

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.district_case_data import DistrictCaseData
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
    api_instance = lexmachina.FederalDistrictCasesApi(api_client)
    district_case_id = 56 # int | 
    docket_retrieval = 'docket_retrieval_example' # str | 'all' to retrieve docket entries for the case, if not provided no docket entries will be retrieved. (optional)

    try:
        # Get District Case
        api_response = api_instance.get_district_case(district_case_id, docket_retrieval=docket_retrieval)
        print("The response of FederalDistrictCasesApi->get_district_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalDistrictCasesApi->get_district_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_case_id** | **int**|  | 
 **docket_retrieval** | **str**| &#39;all&#39; to retrieve docket entries for the case, if not provided no docket entries will be retrieved. | [optional] 

### Return type

[**DistrictCaseData**](DistrictCaseData.md)

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

# **query_district_cases**
> DistrictCaseQueryResult query_district_cases(district_case_query)

Query District Cases

Queries federal district court cases.

- **data**: the district case query

See [https://developer.lexmachina.com/posts/query/query_usage_portal_post/](https://developer.lexmachina.com/posts/query/query_usage_portal_post/] for query formation.

The results will contain a list of cases, each with a specificed url and Lex Machina districtCaseId.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.district_case_query import DistrictCaseQuery
from lexmachina.models.district_case_query_result import DistrictCaseQueryResult
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
    api_instance = lexmachina.FederalDistrictCasesApi(api_client)
    district_case_query = {"courts": {"include": ["njd"]}, "caseTypes": {"include": ["Contracts"]}, "dates": {"filed": {"onOrAfter": "2019-01-01", "onOrBefore": "2019-12-31"}, "terminated": {"onOrAfter": "2021-01-01", "onOrBefore": "2021-12-31"}}, "page": 1, "pageSize": 3} # DistrictCaseQuery | 

    try:
        # Query District Cases
        api_response = api_instance.query_district_cases(district_case_query)
        print("The response of FederalDistrictCasesApi->query_district_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FederalDistrictCasesApi->query_district_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_case_query** | [**DistrictCaseQuery**](DistrictCaseQuery.md)|  | 

### Return type

[**DistrictCaseQueryResult**](DistrictCaseQueryResult.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not found |  -  |
**422** | Error - 422 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


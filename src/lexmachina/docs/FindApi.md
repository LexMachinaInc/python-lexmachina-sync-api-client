# lexmachina.FindApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_district_case_by_number**](FindApi.md#find_district_case_by_number) | **GET** /find-district-cases | Find District Case By Number


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
    api_instance = lexmachina.FindApi(api_client)
    case_numbers = ['case_numbers_example'] # List[str] | 
    court = 'court_example' # str |  (optional)

    try:
        # Find District Case By Number
        api_response = api_instance.find_district_case_by_number(case_numbers, court=court)
        print("The response of FindApi->find_district_case_by_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindApi->find_district_case_by_number: %s\n" % e)
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


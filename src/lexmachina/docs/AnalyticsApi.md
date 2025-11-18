# lexmachina.AnalyticsApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_district_cases_from_alert**](AnalyticsApi.md#analyze_district_cases_from_alert) | **GET** /analyze-district-cases/from-alert/{alert_id} | Analyze District Cases From Alert
[**analyze_district_cases_from_query**](AnalyticsApi.md#analyze_district_cases_from_query) | **POST** /analyze-district-cases/from-query | Analyze District Cases From Query


# **analyze_district_cases_from_alert**
> CaseAnalyticResult analyze_district_cases_from_alert(alert_id, analytic_type, on_or_after=on_or_after, on_or_before=on_or_before)

Analyze District Cases From Alert

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.analytic_types import AnalyticTypes
from lexmachina.models.case_analytic_result import CaseAnalyticResult
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
    api_instance = lexmachina.AnalyticsApi(api_client)
    alert_id = 56 # int | 
    analytic_type = lexmachina.AnalyticTypes() # AnalyticTypes | 
    on_or_after = '2013-10-20' # date | alert start date (optional)
    on_or_before = '2013-10-20' # date | alert end date (optional)

    try:
        # Analyze District Cases From Alert
        api_response = api_instance.analyze_district_cases_from_alert(alert_id, analytic_type, on_or_after=on_or_after, on_or_before=on_or_before)
        print("The response of AnalyticsApi->analyze_district_cases_from_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analyze_district_cases_from_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**|  | 
 **analytic_type** | [**AnalyticTypes**](.md)|  | 
 **on_or_after** | **date**| alert start date | [optional] 
 **on_or_before** | **date**| alert end date | [optional] 

### Return type

[**CaseAnalyticResult**](CaseAnalyticResult.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analyze_district_cases_from_query**
> CaseAnalyticResult analyze_district_cases_from_query(district_case_analytic_from_query)

Analyze District Cases From Query

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.case_analytic_result import CaseAnalyticResult
from lexmachina.models.district_case_analytic_from_query import DistrictCaseAnalyticFromQuery
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
    api_instance = lexmachina.AnalyticsApi(api_client)
    district_case_analytic_from_query = lexmachina.DistrictCaseAnalyticFromQuery() # DistrictCaseAnalyticFromQuery | 

    try:
        # Analyze District Cases From Query
        api_response = api_instance.analyze_district_cases_from_query(district_case_analytic_from_query)
        print("The response of AnalyticsApi->analyze_district_cases_from_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->analyze_district_cases_from_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **district_case_analytic_from_query** | [**DistrictCaseAnalyticFromQuery**](DistrictCaseAnalyticFromQuery.md)|  | 

### Return type

[**CaseAnalyticResult**](CaseAnalyticResult.md)

### Authorization

[JwtAccessBearer](../README.md#JwtAccessBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


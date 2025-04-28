# lexmachina.AlertsApi

All URIs are relative to *https://api.lexmachina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_run_results**](AlertsApi.md#get_alert_run_results) | **GET** /alerts/runs/{alert_id}/{date} | Get Alert Run Results
[**get_alert_runs**](AlertsApi.md#get_alert_runs) | **GET** /alerts/runs/{alert_id} | Get Alert Runs
[**get_alerts**](AlertsApi.md#get_alerts) | **GET** /alerts | Get Alerts


# **get_alert_run_results**
> AlertRunResult get_alert_run_results(alert_id, var_date)

Get Alert Run Results

Gets a list of all new items for a given alert run.

- **alert_id**: the id of the alert
- **date**: the date of the run

Data returned for an alert run will vary in format based on context, only the ids and urls for the relevant data will included.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.alert_run_result import AlertRunResult
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
    api_instance = lexmachina.AlertsApi(api_client)
    alert_id = 56 # int | 
    var_date = '2013-10-20' # date | 

    try:
        # Get Alert Run Results
        api_response = api_instance.get_alert_run_results(alert_id, var_date)
        print("The response of AlertsApi->get_alert_run_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_run_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**|  | 
 **var_date** | **date**|  | 

### Return type

[**AlertRunResult**](AlertRunResult.md)

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

# **get_alert_runs**
> AlertRunData get_alert_runs(alert_id)

Get Alert Runs

Gets a list of all runs an alert has new data for.

- **alert_id**: the id of the alert

Each run represents a new set of relevant items that have been found by the alert on a given day.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.alert_run_data import AlertRunData
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
    api_instance = lexmachina.AlertsApi(api_client)
    alert_id = 56 # int | 

    try:
        # Get Alert Runs
        api_response = api_instance.get_alert_runs(alert_id)
        print("The response of AlertsApi->get_alert_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**|  | 

### Return type

[**AlertRunData**](AlertRunData.md)

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

# **get_alerts**
> List[Alert] get_alerts()

Get Alerts

Gets a list of all alerts the application has access too.

### Example

* Bearer Authentication (JwtAccessBearer):

```python
import lexmachina
from lexmachina.models.alert import Alert
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
    api_instance = lexmachina.AlertsApi(api_client)

    try:
        # Get Alerts
        api_response = api_instance.get_alerts()
        print("The response of AlertsApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Alert]**](Alert.md)

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


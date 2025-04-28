# AlertRunResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **int** |  | 
**type** | **str** |  | 
**count** | **int** |  | 
**run** | **date** |  | 
**items** | [**List[AlertItem]**](AlertItem.md) |  | 

## Example

```python
from lexmachina.models.alert_run_result import AlertRunResult

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRunResult from a JSON string
alert_run_result_instance = AlertRunResult.from_json(json)
# print the JSON string representation of the object
print(AlertRunResult.to_json())

# convert the object into a dict
alert_run_result_dict = alert_run_result_instance.to_dict()
# create an instance of AlertRunResult from a dict
alert_run_result_from_dict = AlertRunResult.from_dict(alert_run_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



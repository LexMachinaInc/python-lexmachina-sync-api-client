# AlertRunData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **int** |  | 
**type** | **str** |  | 
**runs** | **Dict[str, str]** |  | 

## Example

```python
from lexmachina.models.alert_run_data import AlertRunData

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRunData from a JSON string
alert_run_data_instance = AlertRunData.from_json(json)
# print the JSON string representation of the object
print(AlertRunData.to_json())

# convert the object into a dict
alert_run_data_dict = alert_run_data_instance.to_dict()
# create an instance of AlertRunData from a dict
alert_run_data_from_dict = AlertRunData.from_dict(alert_run_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



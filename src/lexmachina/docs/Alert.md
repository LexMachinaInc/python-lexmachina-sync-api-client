# Alert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **int** |  | 
**type** | **str** |  | 
**custom_name** | **str** |  | 
**frequency** | [**Frequency**](Frequency.md) |  | 
**last_run** | **date** |  | 
**alert_url** | **str** |  | 
**law_url** | **str** |  | 

## Example

```python
from lexmachina.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



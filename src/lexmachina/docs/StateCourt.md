# StateCourt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**CourtType**](CourtType.md) |  | 
**state** | **str** |  | 

## Example

```python
from lexmachina.models.state_court import StateCourt

# TODO update the JSON string below
json = "{}"
# create an instance of StateCourt from a JSON string
state_court_instance = StateCourt.from_json(json)
# print the JSON string representation of the object
print(StateCourt.to_json())

# convert the object into a dict
state_court_dict = state_court_instance.to_dict()
# create an instance of StateCourt from a dict
state_court_from_dict = StateCourt.from_dict(state_court_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



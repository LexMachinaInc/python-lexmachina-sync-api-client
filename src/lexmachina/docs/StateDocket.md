# StateDocket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[StateDocketEntry]**](StateDocketEntry.md) |  | 
**retrieved** | [**DocketEntriesIncludedInOutput**](DocketEntriesIncludedInOutput.md) |  | 
**count** | **int** |  | 

## Example

```python
from lexmachina.models.state_docket import StateDocket

# TODO update the JSON string below
json = "{}"
# create an instance of StateDocket from a JSON string
state_docket_instance = StateDocket.from_json(json)
# print the JSON string representation of the object
print(StateDocket.to_json())

# convert the object into a dict
state_docket_dict = state_docket_instance.to_dict()
# create an instance of StateDocket from a dict
state_docket_from_dict = StateDocket.from_dict(state_docket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



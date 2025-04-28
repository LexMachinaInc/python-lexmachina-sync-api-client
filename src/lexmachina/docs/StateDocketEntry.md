# StateDocketEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed_on** | **date** |  | 
**tags** | **List[str]** |  | 
**text** | **str** |  | 
**state_docket_entry_id** | **int** |  | 

## Example

```python
from lexmachina.models.state_docket_entry import StateDocketEntry

# TODO update the JSON string below
json = "{}"
# create an instance of StateDocketEntry from a JSON string
state_docket_entry_instance = StateDocketEntry.from_json(json)
# print the JSON string representation of the object
print(StateDocketEntry.to_json())

# convert the object into a dict
state_docket_entry_dict = state_docket_entry_instance.to_dict()
# create an instance of StateDocketEntry from a dict
state_docket_entry_from_dict = StateDocketEntry.from_dict(state_docket_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



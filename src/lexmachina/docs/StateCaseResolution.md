# StateCaseResolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** |  | 
**specific** | **str** |  | 
**docket_entry_filed** | **date** |  | 
**state_docket_entry_id** | **int** |  | 

## Example

```python
from lexmachina.models.state_case_resolution import StateCaseResolution

# TODO update the JSON string below
json = "{}"
# create an instance of StateCaseResolution from a JSON string
state_case_resolution_instance = StateCaseResolution.from_json(json)
# print the JSON string representation of the object
print(StateCaseResolution.to_json())

# convert the object into a dict
state_case_resolution_dict = state_case_resolution_instance.to_dict()
# create an instance of StateCaseResolution from a dict
state_case_resolution_from_dict = StateCaseResolution.from_dict(state_case_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



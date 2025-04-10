# StateCourtFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.state_court_filter import StateCourtFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StateCourtFilter from a JSON string
state_court_filter_instance = StateCourtFilter.from_json(json)
# print the JSON string representation of the object
print(StateCourtFilter.to_json())

# convert the object into a dict
state_court_filter_dict = state_court_filter_instance.to_dict()
# create an instance of StateCourtFilter from a dict
state_court_filter_from_dict = StateCourtFilter.from_dict(state_court_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



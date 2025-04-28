# StateDocketEntryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed_on** | **date** |  | 
**tags** | **List[str]** |  | 
**text** | **str** |  | 
**state_docket_entry_id** | **int** |  | 
**court_type** | [**CourtType**](CourtType.md) |  | 
**state_case_id** | **int** |  | 
**state_case_url** | **str** |  | 
**court** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from lexmachina.models.state_docket_entry_result import StateDocketEntryResult

# TODO update the JSON string below
json = "{}"
# create an instance of StateDocketEntryResult from a JSON string
state_docket_entry_result_instance = StateDocketEntryResult.from_json(json)
# print the JSON string representation of the object
print(StateDocketEntryResult.to_json())

# convert the object into a dict
state_docket_entry_result_dict = state_docket_entry_result_instance.to_dict()
# create an instance of StateDocketEntryResult from a dict
state_docket_entry_result_from_dict = StateDocketEntryResult.from_dict(state_docket_entry_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



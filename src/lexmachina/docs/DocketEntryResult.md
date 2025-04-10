# DocketEntryResult

The caseId and caseUrl fields will only be populated for the case type of the docket entry.  For example only a district case docket entry will have a districtCaseId and districtCaseURL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed_on** | **date** |  | 
**tags** | **List[str]** |  | 
**text** | **str** |  | 
**number** | **int** |  | 
**docket_entry_id** | **int** |  | 
**court_type** | [**CourtType**](CourtType.md) |  | 
**bankruptcy_case_id** | **int** |  | [optional] 
**appeals_case_id** | **int** |  | [optional] 
**district_case_id** | **int** |  | [optional] 
**district_case_url** | **str** |  | [optional] 
**appeals_case_url** | **str** |  | [optional] 
**bankruptcy_case_url** | **str** |  | [optional] 

## Example

```python
from lexmachina.models.docket_entry_result import DocketEntryResult

# TODO update the JSON string below
json = "{}"
# create an instance of DocketEntryResult from a JSON string
docket_entry_result_instance = DocketEntryResult.from_json(json)
# print the JSON string representation of the object
print(DocketEntryResult.to_json())

# convert the object into a dict
docket_entry_result_dict = docket_entry_result_instance.to_dict()
# create an instance of DocketEntryResult from a dict
docket_entry_result_from_dict = DocketEntryResult.from_dict(docket_entry_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



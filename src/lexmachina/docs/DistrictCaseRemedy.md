# DistrictCaseRemedy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**judgment_source** | **str** |  | 
**awarded_to_party_ids** | **List[int]** |  | 
**against_party_ids** | **List[int]** |  | 
**docket_entry_filed** | **date** |  | 
**negated** | **date** |  | [optional] 
**reinstated** | **date** |  | [optional] 
**docket_entry_id** | **int** |  | 
**negated_docket_entry_id** | **int** |  | [optional] 
**reinstated_docket_entry_id** | **int** |  | [optional] 

## Example

```python
from lexmachina.models.district_case_remedy import DistrictCaseRemedy

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseRemedy from a JSON string
district_case_remedy_instance = DistrictCaseRemedy.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseRemedy.to_json())

# convert the object into a dict
district_case_remedy_dict = district_case_remedy_instance.to_dict()
# create an instance of DistrictCaseRemedy from a dict
district_case_remedy_from_dict = DistrictCaseRemedy.from_dict(district_case_remedy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



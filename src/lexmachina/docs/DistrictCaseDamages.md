# DistrictCaseDamages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**judgment_source** | **str** |  | 
**awarded_to_party_ids** | **List[int]** |  | 
**awarded_against_party_ids** | **List[int]** |  | 
**amount** | [**Amount**](Amount.md) |  | 
**awarded** | **date** |  | 
**negated** | **date** |  | [optional] 
**reinstated** | **date** |  | [optional] 
**docket_entry_id** | **int** |  | 
**negated_docket_entry_id** | **int** |  | [optional] 
**reinstated_docket_entry_id** | **int** |  | [optional] 

## Example

```python
from lexmachina.models.district_case_damages import DistrictCaseDamages

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseDamages from a JSON string
district_case_damages_instance = DistrictCaseDamages.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseDamages.to_json())

# convert the object into a dict
district_case_damages_dict = district_case_damages_instance.to_dict()
# create an instance of DistrictCaseDamages from a dict
district_case_damages_from_dict = DistrictCaseDamages.from_dict(district_case_damages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



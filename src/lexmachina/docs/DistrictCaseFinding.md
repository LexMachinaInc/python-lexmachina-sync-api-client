# DistrictCaseFinding

The following schema field is deprecated: - **patentInvalidityReasons**: this field replaced by the new **specificReasons** field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**judgment_source** | **str** |  | 
**in_favor_of_party_ids** | **List[int]** |  | 
**patent_invalidity_reasons** | **List[str]** | Use &#39;specificReasons&#39; instead | 
**against_party_ids** | **List[int]** |  | 
**docket_entry_filed** | **date** |  | 
**specific_reasons** | **List[str]** |  | [optional] [default to []]
**negated** | **date** |  | [optional] 
**reinstated** | **date** |  | [optional] 
**docket_entry_id** | **int** |  | 
**negated_docket_entry_id** | **int** |  | [optional] 
**reinstated_docket_entry_id** | **int** |  | [optional] 

## Example

```python
from lexmachina.models.district_case_finding import DistrictCaseFinding

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseFinding from a JSON string
district_case_finding_instance = DistrictCaseFinding.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseFinding.to_json())

# convert the object into a dict
district_case_finding_dict = district_case_finding_instance.to_dict()
# create an instance of DistrictCaseFinding from a dict
district_case_finding_from_dict = DistrictCaseFinding.from_dict(district_case_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



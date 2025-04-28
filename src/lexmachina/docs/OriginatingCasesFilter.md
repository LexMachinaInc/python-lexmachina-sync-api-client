# OriginatingCasesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_district_case_ids** | **List[int]** |  | [optional] 
**exclude_district_case_ids** | **List[int]** |  | [optional] 
**include_originating_judges** | [**OriginatingJudgeFilter**](OriginatingJudgeFilter.md) |  | [optional] 
**originating_district_case_criteria** | [**OriginatingDistrictCaseFilter**](OriginatingDistrictCaseFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.originating_cases_filter import OriginatingCasesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatingCasesFilter from a JSON string
originating_cases_filter_instance = OriginatingCasesFilter.from_json(json)
# print the JSON string representation of the object
print(OriginatingCasesFilter.to_json())

# convert the object into a dict
originating_cases_filter_dict = originating_cases_filter_instance.to_dict()
# create an instance of OriginatingCasesFilter from a dict
originating_cases_filter_from_dict = OriginatingCasesFilter.from_dict(originating_cases_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



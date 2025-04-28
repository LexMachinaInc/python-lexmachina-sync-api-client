# OriginatingDistrictCourtCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**district_case_id** | **int** |  | 
**district_case_url** | **str** |  | 
**judges** | [**List[OriginatingDistrictCourtCaseJudgesInner]**](OriginatingDistrictCourtCaseJudgesInner.md) |  | 
**case_types** | **List[str]** |  | 

## Example

```python
from lexmachina.models.originating_district_court_case import OriginatingDistrictCourtCase

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatingDistrictCourtCase from a JSON string
originating_district_court_case_instance = OriginatingDistrictCourtCase.from_json(json)
# print the JSON string representation of the object
print(OriginatingDistrictCourtCase.to_json())

# convert the object into a dict
originating_district_court_case_dict = originating_district_court_case_instance.to_dict()
# create an instance of OriginatingDistrictCourtCase from a dict
originating_district_court_case_from_dict = OriginatingDistrictCourtCase.from_dict(originating_district_court_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



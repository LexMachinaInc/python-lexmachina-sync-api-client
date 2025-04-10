# OriginatingDistrictCaseFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courts** | [**CourtFilter**](CourtFilter.md) |  | [optional] 
**case_types** | [**OriginatingCaseTypesFilter**](OriginatingCaseTypesFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.originating_district_case_filter import OriginatingDistrictCaseFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatingDistrictCaseFilter from a JSON string
originating_district_case_filter_instance = OriginatingDistrictCaseFilter.from_json(json)
# print the JSON string representation of the object
print(OriginatingDistrictCaseFilter.to_json())

# convert the object into a dict
originating_district_case_filter_dict = originating_district_case_filter_instance.to_dict()
# create an instance of OriginatingDistrictCaseFilter from a dict
originating_district_case_filter_from_dict = OriginatingDistrictCaseFilter.from_dict(originating_district_case_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



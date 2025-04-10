# DistrictCaseNumberSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**input_case_number** | **str** |  | 
**input_court** | **str** |  | [optional] 
**matches** | [**List[DistrictCaseNumberReference]**](DistrictCaseNumberReference.md) |  | 

## Example

```python
from lexmachina.models.district_case_number_search_result import DistrictCaseNumberSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseNumberSearchResult from a JSON string
district_case_number_search_result_instance = DistrictCaseNumberSearchResult.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseNumberSearchResult.to_json())

# convert the object into a dict
district_case_number_search_result_dict = district_case_number_search_result_instance.to_dict()
# create an instance of DistrictCaseNumberSearchResult from a dict
district_case_number_search_result_from_dict = DistrictCaseNumberSearchResult.from_dict(district_case_number_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DistrictCaseNumberReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**district_case_id** | **int** |  | 
**case_number** | **str** |  | 
**court** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from lexmachina.models.district_case_number_reference import DistrictCaseNumberReference

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseNumberReference from a JSON string
district_case_number_reference_instance = DistrictCaseNumberReference.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseNumberReference.to_json())

# convert the object into a dict
district_case_number_reference_dict = district_case_number_reference_instance.to_dict()
# create an instance of DistrictCaseNumberReference from a dict
district_case_number_reference_from_dict = DistrictCaseNumberReference.from_dict(district_case_number_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



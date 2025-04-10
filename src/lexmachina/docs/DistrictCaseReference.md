# DistrictCaseReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**district_case_id** | **int** |  | 

## Example

```python
from lexmachina.models.district_case_reference import DistrictCaseReference

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseReference from a JSON string
district_case_reference_instance = DistrictCaseReference.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseReference.to_json())

# convert the object into a dict
district_case_reference_dict = district_case_reference_instance.to_dict()
# create an instance of DistrictCaseReference from a dict
district_case_reference_from_dict = DistrictCaseReference.from_dict(district_case_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



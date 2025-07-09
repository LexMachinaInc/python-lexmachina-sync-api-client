# DistrictCaseResolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** |  | 
**specific** | **str** |  | 
**docket_entry_filed** | **date** |  | 
**docket_entry_id** | **int** |  | 

## Example

```python
from lexmachina.models.district_case_resolution import DistrictCaseResolution

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseResolution from a JSON string
district_case_resolution_instance = DistrictCaseResolution.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseResolution.to_json())

# convert the object into a dict
district_case_resolution_dict = district_case_resolution_instance.to_dict()
# create an instance of DistrictCaseResolution from a dict
district_case_resolution_from_dict = DistrictCaseResolution.from_dict(district_case_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AppealsCase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appeals_case_id** | **int** |  | 
**appeals_case_url** | **str** |  | 
**resolution** | [**DistrictCaseResolution**](DistrictCaseResolution.md) |  | [optional] 
**filed_on** | **date** |  | 
**terminated** | **date** |  | [optional] 

## Example

```python
from lexmachina.models.appeals_case import AppealsCase

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCase from a JSON string
appeals_case_instance = AppealsCase.from_json(json)
# print the JSON string representation of the object
print(AppealsCase.to_json())

# convert the object into a dict
appeals_case_dict = appeals_case_instance.to_dict()
# create an instance of AppealsCase from a dict
appeals_case_from_dict = AppealsCase.from_dict(appeals_case_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



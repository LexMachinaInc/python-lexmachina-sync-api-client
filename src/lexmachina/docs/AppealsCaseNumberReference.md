# AppealsCaseNumberReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**appeals_case_id** | **int** |  | 
**civil_action_number** | **str** |  | 
**court** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from lexmachina.models.appeals_case_number_reference import AppealsCaseNumberReference

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCaseNumberReference from a JSON string
appeals_case_number_reference_instance = AppealsCaseNumberReference.from_json(json)
# print the JSON string representation of the object
print(AppealsCaseNumberReference.to_json())

# convert the object into a dict
appeals_case_number_reference_dict = appeals_case_number_reference_instance.to_dict()
# create an instance of AppealsCaseNumberReference from a dict
appeals_case_number_reference_from_dict = AppealsCaseNumberReference.from_dict(appeals_case_number_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



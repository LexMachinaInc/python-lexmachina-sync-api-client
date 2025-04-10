# AppealsCaseReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**appeals_case_id** | **int** |  | 

## Example

```python
from lexmachina.models.appeals_case_reference import AppealsCaseReference

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCaseReference from a JSON string
appeals_case_reference_instance = AppealsCaseReference.from_json(json)
# print the JSON string representation of the object
print(AppealsCaseReference.to_json())

# convert the object into a dict
appeals_case_reference_dict = appeals_case_reference_instance.to_dict()
# create an instance of AppealsCaseReference from a dict
appeals_case_reference_from_dict = AppealsCaseReference.from_dict(appeals_case_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



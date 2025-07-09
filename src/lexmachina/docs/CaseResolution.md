# CaseResolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** |  | 
**specific** | **str** |  | 
**docket_entry_filed** | **date** |  | 

## Example

```python
from lexmachina.models.case_resolution import CaseResolution

# TODO update the JSON string below
json = "{}"
# create an instance of CaseResolution from a JSON string
case_resolution_instance = CaseResolution.from_json(json)
# print the JSON string representation of the object
print(CaseResolution.to_json())

# convert the object into a dict
case_resolution_dict = case_resolution_instance.to_dict()
# create an instance of CaseResolution from a dict
case_resolution_from_dict = CaseResolution.from_dict(case_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CaseResolutionsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court**](Court.md) |  | 
**case_resolutions** | [**List[PossibleCaseResolution]**](PossibleCaseResolution.md) |  | 

## Example

```python
from lexmachina.models.case_resolutions_list import CaseResolutionsList

# TODO update the JSON string below
json = "{}"
# create an instance of CaseResolutionsList from a JSON string
case_resolutions_list_instance = CaseResolutionsList.from_json(json)
# print the JSON string representation of the object
print(CaseResolutionsList.to_json())

# convert the object into a dict
case_resolutions_list_dict = case_resolutions_list_instance.to_dict()
# create an instance of CaseResolutionsList from a dict
case_resolutions_list_from_dict = CaseResolutionsList.from_dict(case_resolutions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



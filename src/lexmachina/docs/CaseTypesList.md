# CaseTypesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court1**](Court1.md) |  | 
**case_types** | **List[str]** |  | 

## Example

```python
from lexmachina.models.case_types_list import CaseTypesList

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTypesList from a JSON string
case_types_list_instance = CaseTypesList.from_json(json)
# print the JSON string representation of the object
print(CaseTypesList.to_json())

# convert the object into a dict
case_types_list_dict = case_types_list_instance.to_dict()
# create an instance of CaseTypesList from a dict
case_types_list_from_dict = CaseTypesList.from_dict(case_types_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



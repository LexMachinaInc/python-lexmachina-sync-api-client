# CaseTypesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.case_types_filter import CaseTypesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTypesFilter from a JSON string
case_types_filter_instance = CaseTypesFilter.from_json(json)
# print the JSON string representation of the object
print(CaseTypesFilter.to_json())

# convert the object into a dict
case_types_filter_dict = case_types_filter_instance.to_dict()
# create an instance of CaseTypesFilter from a dict
case_types_filter_from_dict = CaseTypesFilter.from_dict(case_types_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



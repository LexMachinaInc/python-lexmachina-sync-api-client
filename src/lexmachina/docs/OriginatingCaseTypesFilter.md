# OriginatingCaseTypesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.originating_case_types_filter import OriginatingCaseTypesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatingCaseTypesFilter from a JSON string
originating_case_types_filter_instance = OriginatingCaseTypesFilter.from_json(json)
# print the JSON string representation of the object
print(OriginatingCaseTypesFilter.to_json())

# convert the object into a dict
originating_case_types_filter_dict = originating_case_types_filter_instance.to_dict()
# create an instance of OriginatingCaseTypesFilter from a dict
originating_case_types_filter_from_dict = OriginatingCaseTypesFilter.from_dict(originating_case_types_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



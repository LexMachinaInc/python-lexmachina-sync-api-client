# CaseTagsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.case_tags_filter import CaseTagsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTagsFilter from a JSON string
case_tags_filter_instance = CaseTagsFilter.from_json(json)
# print the JSON string representation of the object
print(CaseTagsFilter.to_json())

# convert the object into a dict
case_tags_filter_dict = case_tags_filter_instance.to_dict()
# create an instance of CaseTagsFilter from a dict
case_tags_filter_from_dict = CaseTagsFilter.from_dict(case_tags_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



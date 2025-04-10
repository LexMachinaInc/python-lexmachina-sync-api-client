# CaseTagsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court1**](Court1.md) |  | 
**case_tags** | **List[str]** |  | 

## Example

```python
from lexmachina.models.case_tags_list import CaseTagsList

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTagsList from a JSON string
case_tags_list_instance = CaseTagsList.from_json(json)
# print the JSON string representation of the object
print(CaseTagsList.to_json())

# convert the object into a dict
case_tags_list_dict = case_tags_list_instance.to_dict()
# create an instance of CaseTagsList from a dict
case_tags_list_from_dict = CaseTagsList.from_dict(case_tags_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CaseCountByType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_type** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from lexmachina.models.case_count_by_type import CaseCountByType

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountByType from a JSON string
case_count_by_type_instance = CaseCountByType.from_json(json)
# print the JSON string representation of the object
print(CaseCountByType.to_json())

# convert the object into a dict
case_count_by_type_dict = case_count_by_type_instance.to_dict()
# create an instance of CaseCountByType from a dict
case_count_by_type_from_dict = CaseCountByType.from_dict(case_count_by_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



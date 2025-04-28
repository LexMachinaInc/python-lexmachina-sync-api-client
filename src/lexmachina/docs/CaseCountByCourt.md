# CaseCountByCourt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from lexmachina.models.case_count_by_court import CaseCountByCourt

# TODO update the JSON string below
json = "{}"
# create an instance of CaseCountByCourt from a JSON string
case_count_by_court_instance = CaseCountByCourt.from_json(json)
# print the JSON string representation of the object
print(CaseCountByCourt.to_json())

# convert the object into a dict
case_count_by_court_dict = case_count_by_court_instance.to_dict()
# create an instance of CaseCountByCourt from a dict
case_count_by_court_from_dict = CaseCountByCourt.from_dict(case_count_by_court_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



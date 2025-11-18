# CaseTypeAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CaseCountByType]**](CaseCountByType.md) |  | 

## Example

```python
from lexmachina.models.case_type_aggregation import CaseTypeAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of CaseTypeAggregation from a JSON string
case_type_aggregation_instance = CaseTypeAggregation.from_json(json)
# print the JSON string representation of the object
print(CaseTypeAggregation.to_json())

# convert the object into a dict
case_type_aggregation_dict = case_type_aggregation_instance.to_dict()
# create an instance of CaseTypeAggregation from a dict
case_type_aggregation_from_dict = CaseTypeAggregation.from_dict(case_type_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



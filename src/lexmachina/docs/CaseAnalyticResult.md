# CaseAnalyticResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cases** | **int** |  | 
**aggregation** | [**Aggregation**](Aggregation.md) |  | 

## Example

```python
from lexmachina.models.case_analytic_result import CaseAnalyticResult

# TODO update the JSON string below
json = "{}"
# create an instance of CaseAnalyticResult from a JSON string
case_analytic_result_instance = CaseAnalyticResult.from_json(json)
# print the JSON string representation of the object
print(CaseAnalyticResult.to_json())

# convert the object into a dict
case_analytic_result_dict = case_analytic_result_instance.to_dict()
# create an instance of CaseAnalyticResult from a dict
case_analytic_result_from_dict = CaseAnalyticResult.from_dict(case_analytic_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



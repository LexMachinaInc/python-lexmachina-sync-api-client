# FederalJudgeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**federal_judge_id** | **int** |  | 
**initials** | **str** |  | 
**case_count_by_court** | [**List[CaseCountByCourt]**](CaseCountByCourt.md) |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.federal_judge_result import FederalJudgeResult

# TODO update the JSON string below
json = "{}"
# create an instance of FederalJudgeResult from a JSON string
federal_judge_result_instance = FederalJudgeResult.from_json(json)
# print the JSON string representation of the object
print(FederalJudgeResult.to_json())

# convert the object into a dict
federal_judge_result_dict = federal_judge_result_instance.to_dict()
# create an instance of FederalJudgeResult from a dict
federal_judge_result_from_dict = FederalJudgeResult.from_dict(federal_judge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



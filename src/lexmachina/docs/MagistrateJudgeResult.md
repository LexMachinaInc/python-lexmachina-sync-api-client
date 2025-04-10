# MagistrateJudgeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**magistrate_judge_id** | **int** |  | 
**case_count_by_court** | [**List[CaseCountByCourt]**](CaseCountByCourt.md) |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.magistrate_judge_result import MagistrateJudgeResult

# TODO update the JSON string below
json = "{}"
# create an instance of MagistrateJudgeResult from a JSON string
magistrate_judge_result_instance = MagistrateJudgeResult.from_json(json)
# print the JSON string representation of the object
print(MagistrateJudgeResult.to_json())

# convert the object into a dict
magistrate_judge_result_dict = magistrate_judge_result_instance.to_dict()
# create an instance of MagistrateJudgeResult from a dict
magistrate_judge_result_from_dict = MagistrateJudgeResult.from_dict(magistrate_judge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



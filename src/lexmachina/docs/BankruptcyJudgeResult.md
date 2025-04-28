# BankruptcyJudgeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**bankruptcy_judge_id** | **int** |  | 
**case_count_by_court** | [**List[CaseCountByCourt]**](CaseCountByCourt.md) |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.bankruptcy_judge_result import BankruptcyJudgeResult

# TODO update the JSON string below
json = "{}"
# create an instance of BankruptcyJudgeResult from a JSON string
bankruptcy_judge_result_instance = BankruptcyJudgeResult.from_json(json)
# print the JSON string representation of the object
print(BankruptcyJudgeResult.to_json())

# convert the object into a dict
bankruptcy_judge_result_dict = bankruptcy_judge_result_instance.to_dict()
# create an instance of BankruptcyJudgeResult from a dict
bankruptcy_judge_result_from_dict = BankruptcyJudgeResult.from_dict(bankruptcy_judge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# JudgeSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**federal_judges** | [**List[FederalJudgeResult]**](FederalJudgeResult.md) |  | 
**magistrate_judges** | [**List[MagistrateJudgeResult]**](MagistrateJudgeResult.md) |  | 
**state_judges** | [**List[StateJudgeResult]**](StateJudgeResult.md) |  | 
**bankruptcy_judges** | [**List[BankruptcyJudgeResult]**](BankruptcyJudgeResult.md) |  | 

## Example

```python
from lexmachina.models.judge_search_result import JudgeSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of JudgeSearchResult from a JSON string
judge_search_result_instance = JudgeSearchResult.from_json(json)
# print the JSON string representation of the object
print(JudgeSearchResult.to_json())

# convert the object into a dict
judge_search_result_dict = judge_search_result_instance.to_dict()
# create an instance of JudgeSearchResult from a dict
judge_search_result_from_dict = JudgeSearchResult.from_dict(judge_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



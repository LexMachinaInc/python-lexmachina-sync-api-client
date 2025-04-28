# StateJudgeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**state_judge_id** | **int** |  | 
**court_posting** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.state_judge_result import StateJudgeResult

# TODO update the JSON string below
json = "{}"
# create an instance of StateJudgeResult from a JSON string
state_judge_result_instance = StateJudgeResult.from_json(json)
# print the JSON string representation of the object
print(StateJudgeResult.to_json())

# convert the object into a dict
state_judge_result_dict = state_judge_result_instance.to_dict()
# create an instance of StateJudgeResult from a dict
state_judge_result_from_dict = StateJudgeResult.from_dict(state_judge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



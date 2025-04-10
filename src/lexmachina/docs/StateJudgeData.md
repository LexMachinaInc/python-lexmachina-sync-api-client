# StateJudgeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**state_judge_id** | **int** |  | 
**court_posting** | **str** |  | 

## Example

```python
from lexmachina.models.state_judge_data import StateJudgeData

# TODO update the JSON string below
json = "{}"
# create an instance of StateJudgeData from a JSON string
state_judge_data_instance = StateJudgeData.from_json(json)
# print the JSON string representation of the object
print(StateJudgeData.to_json())

# convert the object into a dict
state_judge_data_dict = state_judge_data_instance.to_dict()
# create an instance of StateJudgeData from a dict
state_judge_data_from_dict = StateJudgeData.from_dict(state_judge_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



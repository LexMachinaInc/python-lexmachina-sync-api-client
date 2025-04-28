# MagistrateJudgeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**magistrate_judge_id** | **int** |  | 
**initials** | **str** |  | 
**case_count_by_court** | [**List[CaseCountByCourt]**](CaseCountByCourt.md) |  | 

## Example

```python
from lexmachina.models.magistrate_judge_data import MagistrateJudgeData

# TODO update the JSON string below
json = "{}"
# create an instance of MagistrateJudgeData from a JSON string
magistrate_judge_data_instance = MagistrateJudgeData.from_json(json)
# print the JSON string representation of the object
print(MagistrateJudgeData.to_json())

# convert the object into a dict
magistrate_judge_data_dict = magistrate_judge_data_instance.to_dict()
# create an instance of MagistrateJudgeData from a dict
magistrate_judge_data_from_dict = MagistrateJudgeData.from_dict(magistrate_judge_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



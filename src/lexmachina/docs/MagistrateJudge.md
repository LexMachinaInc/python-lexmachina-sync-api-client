# MagistrateJudge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**magistrate_judge_id** | **int** |  | 

## Example

```python
from lexmachina.models.magistrate_judge import MagistrateJudge

# TODO update the JSON string below
json = "{}"
# create an instance of MagistrateJudge from a JSON string
magistrate_judge_instance = MagistrateJudge.from_json(json)
# print the JSON string representation of the object
print(MagistrateJudge.to_json())

# convert the object into a dict
magistrate_judge_dict = magistrate_judge_instance.to_dict()
# create an instance of MagistrateJudge from a dict
magistrate_judge_from_dict = MagistrateJudge.from_dict(magistrate_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FederalJudge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**federal_judge_id** | **int** |  | 

## Example

```python
from lexmachina.models.federal_judge import FederalJudge

# TODO update the JSON string below
json = "{}"
# create an instance of FederalJudge from a JSON string
federal_judge_instance = FederalJudge.from_json(json)
# print the JSON string representation of the object
print(FederalJudge.to_json())

# convert the object into a dict
federal_judge_dict = federal_judge_instance.to_dict()
# create an instance of FederalJudge from a dict
federal_judge_from_dict = FederalJudge.from_dict(federal_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



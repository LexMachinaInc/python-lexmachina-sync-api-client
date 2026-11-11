# JudgesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**federal_judge_id** | **int** |  | 
**magistrate_judge_id** | **int** |  | 

## Example

```python
from lexmachina.models.judges_inner import JudgesInner

# TODO update the JSON string below
json = "{}"
# create an instance of JudgesInner from a JSON string
judges_inner_instance = JudgesInner.from_json(json)
# print the JSON string representation of the object
print(JudgesInner.to_json())

# convert the object into a dict
judges_inner_dict = judges_inner_instance.to_dict()
# create an instance of JudgesInner from a dict
judges_inner_from_dict = JudgesInner.from_dict(judges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# JudgeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[int]** |  | [optional] 
**exclude** | **List[int]** |  | [optional] 

## Example

```python
from lexmachina.models.judge_filter import JudgeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of JudgeFilter from a JSON string
judge_filter_instance = JudgeFilter.from_json(json)
# print the JSON string representation of the object
print(JudgeFilter.to_json())

# convert the object into a dict
judge_filter_dict = judge_filter_instance.to_dict()
# create an instance of JudgeFilter from a dict
judge_filter_from_dict = JudgeFilter.from_dict(judge_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



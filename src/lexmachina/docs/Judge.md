# Judge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**federal_judge_id** | **int** |  | 
**magistrate_judge_id** | **int** |  | 

## Example

```python
from lexmachina.models.judge import Judge

# TODO update the JSON string below
json = "{}"
# create an instance of Judge from a JSON string
judge_instance = Judge.from_json(json)
# print the JSON string representation of the object
print(Judge.to_json())

# convert the object into a dict
judge_dict = judge_instance.to_dict()
# create an instance of Judge from a dict
judge_from_dict = Judge.from_dict(judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



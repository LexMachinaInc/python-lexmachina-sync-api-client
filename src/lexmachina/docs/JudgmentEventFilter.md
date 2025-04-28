# JudgmentEventFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.judgment_event_filter import JudgmentEventFilter

# TODO update the JSON string below
json = "{}"
# create an instance of JudgmentEventFilter from a JSON string
judgment_event_filter_instance = JudgmentEventFilter.from_json(json)
# print the JSON string representation of the object
print(JudgmentEventFilter.to_json())

# convert the object into a dict
judgment_event_filter_dict = judgment_event_filter_instance.to_dict()
# create an instance of JudgmentEventFilter from a dict
judgment_event_filter_from_dict = JudgmentEventFilter.from_dict(judgment_event_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



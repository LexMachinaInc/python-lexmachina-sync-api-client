# JudgmentEventsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judgment_events** | **List[str]** |  | 
**court** | [**Court**](Court.md) |  | [optional] 

## Example

```python
from lexmachina.models.judgment_events_list import JudgmentEventsList

# TODO update the JSON string below
json = "{}"
# create an instance of JudgmentEventsList from a JSON string
judgment_events_list_instance = JudgmentEventsList.from_json(json)
# print the JSON string representation of the object
print(JudgmentEventsList.to_json())

# convert the object into a dict
judgment_events_list_dict = judgment_events_list_instance.to_dict()
# create an instance of JudgmentEventsList from a dict
judgment_events_list_from_dict = JudgmentEventsList.from_dict(judgment_events_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



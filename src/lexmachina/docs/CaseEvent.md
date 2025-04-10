# CaseEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**occurred** | **date** |  | 

## Example

```python
from lexmachina.models.case_event import CaseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CaseEvent from a JSON string
case_event_instance = CaseEvent.from_json(json)
# print the JSON string representation of the object
print(CaseEvent.to_json())

# convert the object into a dict
case_event_dict = case_event_instance.to_dict()
# create an instance of CaseEvent from a dict
case_event_from_dict = CaseEvent.from_dict(case_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



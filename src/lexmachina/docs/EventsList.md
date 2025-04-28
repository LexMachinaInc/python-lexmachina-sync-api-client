# EventsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court**](Court.md) |  | 
**events** | **List[str]** |  | 

## Example

```python
from lexmachina.models.events_list import EventsList

# TODO update the JSON string below
json = "{}"
# create an instance of EventsList from a JSON string
events_list_instance = EventsList.from_json(json)
# print the JSON string representation of the object
print(EventsList.to_json())

# convert the object into a dict
events_list_dict = events_list_instance.to_dict()
# create an instance of EventsList from a dict
events_list_from_dict = EventsList.from_dict(events_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



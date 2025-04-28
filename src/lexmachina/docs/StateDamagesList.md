# StateDamagesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court**](Court.md) |  | [optional] 
**damages** | **List[str]** |  | 

## Example

```python
from lexmachina.models.state_damages_list import StateDamagesList

# TODO update the JSON string below
json = "{}"
# create an instance of StateDamagesList from a JSON string
state_damages_list_instance = StateDamagesList.from_json(json)
# print the JSON string representation of the object
print(StateDamagesList.to_json())

# convert the object into a dict
state_damages_list_dict = state_damages_list_instance.to_dict()
# create an instance of StateDamagesList from a dict
state_damages_list_from_dict = StateDamagesList.from_dict(state_damages_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# StateCaseDamages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**awarded_to_party_id** | **List[int]** |  | 
**awarded_against_party_ids** | **List[int]** |  | 
**amount** | **str** |  | 
**awarded** | **date** |  | 

## Example

```python
from lexmachina.models.state_case_damages import StateCaseDamages

# TODO update the JSON string below
json = "{}"
# create an instance of StateCaseDamages from a JSON string
state_case_damages_instance = StateCaseDamages.from_json(json)
# print the JSON string representation of the object
print(StateCaseDamages.to_json())

# convert the object into a dict
state_case_damages_dict = state_case_damages_instance.to_dict()
# create an instance of StateCaseDamages from a dict
state_case_damages_from_dict = StateCaseDamages.from_dict(state_case_damages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



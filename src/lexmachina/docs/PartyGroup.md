# PartyGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party_group_name** | **str** |  | 
**parties** | **List[int]** |  | 
**party_group_id** | **int** |  | 
**law_url** | **str** |  | 

## Example

```python
from lexmachina.models.party_group import PartyGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PartyGroup from a JSON string
party_group_instance = PartyGroup.from_json(json)
# print the JSON string representation of the object
print(PartyGroup.to_json())

# convert the object into a dict
party_group_dict = party_group_instance.to_dict()
# create an instance of PartyGroup from a dict
party_group_from_dict = PartyGroup.from_dict(party_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



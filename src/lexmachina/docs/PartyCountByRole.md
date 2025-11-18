# PartyCountByRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**party_id** | **int** |  | 
**party_name** | **str** |  | 
**roles_and_counts** | [**List[CountsPerRole]**](CountsPerRole.md) |  | 

## Example

```python
from lexmachina.models.party_count_by_role import PartyCountByRole

# TODO update the JSON string below
json = "{}"
# create an instance of PartyCountByRole from a JSON string
party_count_by_role_instance = PartyCountByRole.from_json(json)
# print the JSON string representation of the object
print(PartyCountByRole.to_json())

# convert the object into a dict
party_count_by_role_dict = party_count_by_role_instance.to_dict()
# create an instance of PartyCountByRole from a dict
party_count_by_role_from_dict = PartyCountByRole.from_dict(party_count_by_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



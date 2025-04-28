# PartyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**party_id** | **int** |  | 

## Example

```python
from lexmachina.models.party_data import PartyData

# TODO update the JSON string below
json = "{}"
# create an instance of PartyData from a JSON string
party_data_instance = PartyData.from_json(json)
# print the JSON string representation of the object
print(PartyData.to_json())

# convert the object into a dict
party_data_dict = party_data_instance.to_dict()
# create an instance of PartyData from a dict
party_data_from_dict = PartyData.from_dict(party_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



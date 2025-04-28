# PartyReference

Indicates that the Lex Machina party id input was has changed, the inputId is the ID given that should map to the returned partyId.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**party_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.party_reference import PartyReference

# TODO update the JSON string below
json = "{}"
# create an instance of PartyReference from a JSON string
party_reference_instance = PartyReference.from_json(json)
# print the JSON string representation of the object
print(PartyReference.to_json())

# convert the object into a dict
party_reference_dict = party_reference_instance.to_dict()
# create an instance of PartyReference from a dict
party_reference_from_dict = PartyReference.from_dict(party_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



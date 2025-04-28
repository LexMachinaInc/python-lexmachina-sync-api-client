# ITCParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from lexmachina.models.itc_party import ITCParty

# TODO update the JSON string below
json = "{}"
# create an instance of ITCParty from a JSON string
itc_party_instance = ITCParty.from_json(json)
# print the JSON string representation of the object
print(ITCParty.to_json())

# convert the object into a dict
itc_party_dict = itc_party_instance.to_dict()
# create an instance of ITCParty from a dict
itc_party_from_dict = ITCParty.from_dict(itc_party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



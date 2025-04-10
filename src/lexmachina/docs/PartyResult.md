# PartyResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**party_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.party_result import PartyResult

# TODO update the JSON string below
json = "{}"
# create an instance of PartyResult from a JSON string
party_result_instance = PartyResult.from_json(json)
# print the JSON string representation of the object
print(PartyResult.to_json())

# convert the object into a dict
party_result_dict = party_result_instance.to_dict()
# create an instance of PartyResult from a dict
party_result_from_dict = PartyResult.from_dict(party_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PartyFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[int]** |  | [optional] 
**exclude** | **List[int]** |  | [optional] 
**include_plaintiff** | **List[int]** |  | [optional] 
**exclude_plaintiff** | **List[int]** |  | [optional] 
**include_defendant** | **List[int]** |  | [optional] 
**exclude_defendant** | **List[int]** |  | [optional] 
**include_third_party** | **List[int]** |  | [optional] 
**exclude_third_party** | **List[int]** |  | [optional] 

## Example

```python
from lexmachina.models.party_filter import PartyFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PartyFilter from a JSON string
party_filter_instance = PartyFilter.from_json(json)
# print the JSON string representation of the object
print(PartyFilter.to_json())

# convert the object into a dict
party_filter_dict = party_filter_instance.to_dict()
# create an instance of PartyFilter from a dict
party_filter_from_dict = PartyFilter.from_dict(party_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



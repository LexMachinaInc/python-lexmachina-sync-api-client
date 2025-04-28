# Rulings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judgment_event** | **str** |  | 
**awarded_to_party_ids** | **List[int]** |  | 
**awarded_against_party_ids** | **List[int]** |  | 
**awarded** | **date** |  | 

## Example

```python
from lexmachina.models.rulings import Rulings

# TODO update the JSON string below
json = "{}"
# create an instance of Rulings from a JSON string
rulings_instance = Rulings.from_json(json)
# print the JSON string representation of the object
print(Rulings.to_json())

# convert the object into a dict
rulings_dict = rulings_instance.to_dict()
# create an instance of Rulings from a dict
rulings_from_dict = Rulings.from_dict(rulings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Attorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attorney_id** | **int** |  | 
**law_firm_ids** | **List[int]** |  | 
**clients_party_ids** | **List[int]** |  | 

## Example

```python
from lexmachina.models.attorney import Attorney

# TODO update the JSON string below
json = "{}"
# create an instance of Attorney from a JSON string
attorney_instance = Attorney.from_json(json)
# print the JSON string representation of the object
print(Attorney.to_json())

# convert the object into a dict
attorney_dict = attorney_instance.to_dict()
# create an instance of Attorney from a dict
attorney_from_dict = Attorney.from_dict(attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



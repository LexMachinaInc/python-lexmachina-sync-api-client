# ResponseGetParty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**party_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.response_get_party import ResponseGetParty

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetParty from a JSON string
response_get_party_instance = ResponseGetParty.from_json(json)
# print the JSON string representation of the object
print(ResponseGetParty.to_json())

# convert the object into a dict
response_get_party_dict = response_get_party_instance.to_dict()
# create an instance of ResponseGetParty from a dict
response_get_party_from_dict = ResponseGetParty.from_dict(response_get_party_dict)
```
[[Back to Model list]](../../../README.md#documentation-for-models) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)



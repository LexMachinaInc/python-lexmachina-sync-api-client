# ResponseGetPartyPartiesPartyIdGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**party_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.response_get_party_parties_party_id_get import ResponseGetPartyPartiesPartyIdGet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetPartyPartiesPartyIdGet from a JSON string
response_get_party_parties_party_id_get_instance = ResponseGetPartyPartiesPartyIdGet.from_json(json)
# print the JSON string representation of the object
print(ResponseGetPartyPartiesPartyIdGet.to_json())

# convert the object into a dict
response_get_party_parties_party_id_get_dict = response_get_party_parties_party_id_get_instance.to_dict()
# create an instance of ResponseGetPartyPartiesPartyIdGet from a dict
response_get_party_parties_party_id_get_from_dict = ResponseGetPartyPartiesPartyIdGet.from_dict(response_get_party_parties_party_id_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetPartiesPartiesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**party_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from openapi_client.models.get_parties_parties_get200_response_inner import GetPartiesPartiesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPartiesPartiesGet200ResponseInner from a JSON string
get_parties_parties_get200_response_inner_instance = GetPartiesPartiesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetPartiesPartiesGet200ResponseInner.to_json())

# convert the object into a dict
get_parties_parties_get200_response_inner_dict = get_parties_parties_get200_response_inner_instance.to_dict()
# create an instance of GetPartiesPartiesGet200ResponseInner from a dict
get_parties_parties_get200_response_inner_from_dict = GetPartiesPartiesGet200ResponseInner.from_dict(get_parties_parties_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



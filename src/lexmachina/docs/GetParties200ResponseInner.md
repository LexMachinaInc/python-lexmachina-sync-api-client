# GetParties200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**party_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.get_parties200_response_inner import GetParties200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetParties200ResponseInner from a JSON string
get_parties200_response_inner_instance = GetParties200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetParties200ResponseInner.to_json())

# convert the object into a dict
get_parties200_response_inner_dict = get_parties200_response_inner_instance.to_dict()
# create an instance of GetParties200ResponseInner from a dict
get_parties200_response_inner_from_dict = GetParties200ResponseInner.from_dict(get_parties200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



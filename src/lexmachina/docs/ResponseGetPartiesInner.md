# ResponseGetPartiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**party_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.response_get_parties_inner import ResponseGetPartiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetPartiesInner from a JSON string
response_get_parties_inner_instance = ResponseGetPartiesInner.from_json(json)
# print the JSON string representation of the object
print(ResponseGetPartiesInner.to_json())

# convert the object into a dict
response_get_parties_inner_dict = response_get_parties_inner_instance.to_dict()
# create an instance of ResponseGetPartiesInner from a dict
response_get_parties_inner_from_dict = ResponseGetPartiesInner.from_dict(response_get_parties_inner_dict)
```
[[Back to Model list]](../../../README.md#documentation-for-models) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)



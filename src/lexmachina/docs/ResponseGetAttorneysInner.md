# ResponseGetAttorneysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attorney_id** | **int** |  | 
**url** | **str** |  | 
**input_id** | **int** |  | 

## Example

```python
from lexmachina.models.response_get_attorneys_inner import ResponseGetAttorneysInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetAttorneysInner from a JSON string
response_get_attorneys_inner_instance = ResponseGetAttorneysInner.from_json(json)
# print the JSON string representation of the object
print(ResponseGetAttorneysInner.to_json())

# convert the object into a dict
response_get_attorneys_inner_dict = response_get_attorneys_inner_instance.to_dict()
# create an instance of ResponseGetAttorneysInner from a dict
response_get_attorneys_inner_from_dict = ResponseGetAttorneysInner.from_dict(response_get_attorneys_inner_dict)
```
[[Back to Model list]](../../../README.md#documentation-for-models) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)



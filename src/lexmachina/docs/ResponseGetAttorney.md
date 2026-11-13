# ResponseGetAttorney


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attorney_id** | **int** |  | 
**url** | **str** |  | 
**input_id** | **int** |  | 

## Example

```python
from lexmachina.models.response_get_attorney import ResponseGetAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetAttorney from a JSON string
response_get_attorney_instance = ResponseGetAttorney.from_json(json)
# print the JSON string representation of the object
print(ResponseGetAttorney.to_json())

# convert the object into a dict
response_get_attorney_dict = response_get_attorney_instance.to_dict()
# create an instance of ResponseGetAttorney from a dict
response_get_attorney_from_dict = ResponseGetAttorney.from_dict(response_get_attorney_dict)
```
[[Back to Model list]](../../../README.md#documentation-for-models) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)



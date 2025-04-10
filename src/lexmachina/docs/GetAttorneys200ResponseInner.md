# GetAttorneys200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attorney_id** | **int** |  | 
**url** | **str** |  | 
**input_id** | **int** |  | 

## Example

```python
from lexmachina.models.get_attorneys200_response_inner import GetAttorneys200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAttorneys200ResponseInner from a JSON string
get_attorneys200_response_inner_instance = GetAttorneys200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAttorneys200ResponseInner.to_json())

# convert the object into a dict
get_attorneys200_response_inner_dict = get_attorneys200_response_inner_instance.to_dict()
# create an instance of GetAttorneys200ResponseInner from a dict
get_attorneys200_response_inner_from_dict = GetAttorneys200ResponseInner.from_dict(get_attorneys200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



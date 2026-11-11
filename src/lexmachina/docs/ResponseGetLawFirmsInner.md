# ResponseGetLawFirmsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**law_firm_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.response_get_law_firms_inner import ResponseGetLawFirmsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetLawFirmsInner from a JSON string
response_get_law_firms_inner_instance = ResponseGetLawFirmsInner.from_json(json)
# print the JSON string representation of the object
print(ResponseGetLawFirmsInner.to_json())

# convert the object into a dict
response_get_law_firms_inner_dict = response_get_law_firms_inner_instance.to_dict()
# create an instance of ResponseGetLawFirmsInner from a dict
response_get_law_firms_inner_from_dict = ResponseGetLawFirmsInner.from_dict(response_get_law_firms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



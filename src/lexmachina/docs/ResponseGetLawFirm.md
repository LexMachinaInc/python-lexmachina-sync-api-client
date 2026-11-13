# ResponseGetLawFirm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**law_firm_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.response_get_law_firm import ResponseGetLawFirm

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetLawFirm from a JSON string
response_get_law_firm_instance = ResponseGetLawFirm.from_json(json)
# print the JSON string representation of the object
print(ResponseGetLawFirm.to_json())

# convert the object into a dict
response_get_law_firm_dict = response_get_law_firm_instance.to_dict()
# create an instance of ResponseGetLawFirm from a dict
response_get_law_firm_from_dict = ResponseGetLawFirm.from_dict(response_get_law_firm_dict)
```
[[Back to Model list]](../../../README.md#documentation-for-models) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)



# GetLawFirms200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**law_firm_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.get_law_firms200_response_inner import GetLawFirms200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLawFirms200ResponseInner from a JSON string
get_law_firms200_response_inner_instance = GetLawFirms200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetLawFirms200ResponseInner.to_json())

# convert the object into a dict
get_law_firms200_response_inner_dict = get_law_firms200_response_inner_instance.to_dict()
# create an instance of GetLawFirms200ResponseInner from a dict
get_law_firms200_response_inner_from_dict = GetLawFirms200ResponseInner.from_dict(get_law_firms200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



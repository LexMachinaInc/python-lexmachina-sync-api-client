# LawFirmFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[int]** |  | [optional] 
**exclude** | **List[int]** |  | [optional] 
**include_plaintiff** | **List[int]** |  | [optional] 
**exclude_plaintiff** | **List[int]** |  | [optional] 
**include_defendant** | **List[int]** |  | [optional] 
**exclude_defendant** | **List[int]** |  | [optional] 
**include_third_party** | **List[int]** |  | [optional] 
**exclude_third_party** | **List[int]** |  | [optional] 

## Example

```python
from lexmachina.models.law_firm_filter import LawFirmFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirmFilter from a JSON string
law_firm_filter_instance = LawFirmFilter.from_json(json)
# print the JSON string representation of the object
print(LawFirmFilter.to_json())

# convert the object into a dict
law_firm_filter_dict = law_firm_filter_instance.to_dict()
# create an instance of LawFirmFilter from a dict
law_firm_filter_from_dict = LawFirmFilter.from_dict(law_firm_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



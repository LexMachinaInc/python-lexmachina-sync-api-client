# LawFirmReference

Indicates that the Lex Machina law firm id input was has changed, the inputId is the ID given that should map to the returned lawFirmId.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**law_firm_id** | **int** |  | 
**input_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.law_firm_reference import LawFirmReference

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirmReference from a JSON string
law_firm_reference_instance = LawFirmReference.from_json(json)
# print the JSON string representation of the object
print(LawFirmReference.to_json())

# convert the object into a dict
law_firm_reference_dict = law_firm_reference_instance.to_dict()
# create an instance of LawFirmReference from a dict
law_firm_reference_from_dict = LawFirmReference.from_dict(law_firm_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



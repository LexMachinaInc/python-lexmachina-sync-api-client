# LawFirmResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**law_firm_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.law_firm_result import LawFirmResult

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirmResult from a JSON string
law_firm_result_instance = LawFirmResult.from_json(json)
# print the JSON string representation of the object
print(LawFirmResult.to_json())

# convert the object into a dict
law_firm_result_dict = law_firm_result_instance.to_dict()
# create an instance of LawFirmResult from a dict
law_firm_result_from_dict = LawFirmResult.from_dict(law_firm_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LawFirmData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**law_firm_id** | **int** |  | 

## Example

```python
from lexmachina.models.law_firm_data import LawFirmData

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirmData from a JSON string
law_firm_data_instance = LawFirmData.from_json(json)
# print the JSON string representation of the object
print(LawFirmData.to_json())

# convert the object into a dict
law_firm_data_dict = law_firm_data_instance.to_dict()
# create an instance of LawFirmData from a dict
law_firm_data_from_dict = LawFirmData.from_dict(law_firm_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LawFirm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**law_firm_id** | **int** |  | 
**client_party_ids** | **List[int]** |  | 

## Example

```python
from lexmachina.models.law_firm import LawFirm

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirm from a JSON string
law_firm_instance = LawFirm.from_json(json)
# print the JSON string representation of the object
print(LawFirm.to_json())

# convert the object into a dict
law_firm_dict = law_firm_instance.to_dict()
# create an instance of LawFirm from a dict
law_firm_from_dict = LawFirm.from_dict(law_firm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



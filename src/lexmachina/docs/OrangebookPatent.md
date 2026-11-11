# OrangebookPatent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_number** | **str** |  | 
**product_number** | **str** |  | 
**trade_name** | **str** |  | [optional] 
**active_ingredient** | **str** |  | [optional] 
**applicant** | **str** |  | [optional] 
**strength** | **str** |  | [optional] 
**dosage_form_route** | **str** |  | [optional] 
**patent_expiration_date** | **date** |  | [optional] 
**pediatric_exclusivity_expiration_date** | **date** |  | [optional] 

## Example

```python
from lexmachina.models.orangebook_patent import OrangebookPatent

# TODO update the JSON string below
json = "{}"
# create an instance of OrangebookPatent from a JSON string
orangebook_patent_instance = OrangebookPatent.from_json(json)
# print the JSON string representation of the object
print(OrangebookPatent.to_json())

# convert the object into a dict
orangebook_patent_dict = orangebook_patent_instance.to_dict()
# create an instance of OrangebookPatent from a dict
orangebook_patent_from_dict = OrangebookPatent.from_dict(orangebook_patent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



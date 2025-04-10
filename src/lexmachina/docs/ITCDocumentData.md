# ITCDocumentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usitc_document_id** | **int** |  | 
**var_date** | **date** |  | 
**title** | **str** |  | 
**type** | **str** |  | 
**filed_by** | [**List[ITCDocumentEntityData]**](ITCDocumentEntityData.md) |  | 
**firm** | [**List[ITCDocumentEntityData]**](ITCDocumentEntityData.md) |  | 
**on_behalf_of** | [**List[ITCDocumentEntityData]**](ITCDocumentEntityData.md) |  | 
**investigation_number** | **str** |  | 

## Example

```python
from lexmachina.models.itc_document_data import ITCDocumentData

# TODO update the JSON string below
json = "{}"
# create an instance of ITCDocumentData from a JSON string
itc_document_data_instance = ITCDocumentData.from_json(json)
# print the JSON string representation of the object
print(ITCDocumentData.to_json())

# convert the object into a dict
itc_document_data_dict = itc_document_data_instance.to_dict()
# create an instance of ITCDocumentData from a dict
itc_document_data_from_dict = ITCDocumentData.from_dict(itc_document_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



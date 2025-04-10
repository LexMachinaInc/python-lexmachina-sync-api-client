# ITCDocument


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

## Example

```python
from lexmachina.models.itc_document import ITCDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ITCDocument from a JSON string
itc_document_instance = ITCDocument.from_json(json)
# print the JSON string representation of the object
print(ITCDocument.to_json())

# convert the object into a dict
itc_document_dict = itc_document_instance.to_dict()
# create an instance of ITCDocument from a dict
itc_document_from_dict = ITCDocument.from_dict(itc_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ITCDocumentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ITCDocument]**](ITCDocument.md) |  | 
**retrieved** | [**DocketEntriesIncludedInOutput**](DocketEntriesIncludedInOutput.md) |  | 
**count** | **int** |  | 

## Example

```python
from lexmachina.models.itc_document_list import ITCDocumentList

# TODO update the JSON string below
json = "{}"
# create an instance of ITCDocumentList from a JSON string
itc_document_list_instance = ITCDocumentList.from_json(json)
# print the JSON string representation of the object
print(ITCDocumentList.to_json())

# convert the object into a dict
itc_document_list_dict = itc_document_list_instance.to_dict()
# create an instance of ITCDocumentList from a dict
itc_document_list_from_dict = ITCDocumentList.from_dict(itc_document_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ITCInvestigationData

A single US ITC investigation and relevant metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itc_investigation_id** | **str** |  | 
**investigation_number** | **str** |  | 
**title** | **str** |  | 
**investigation_types** | [**List[ITCInvestigationType]**](ITCInvestigationType.md) |  | 
**status** | [**ITCInvestigationStatus**](ITCInvestigationStatus.md) |  | 
**dates** | [**ITCInvestigationDates**](ITCInvestigationDates.md) |  | 
**administrative_law_judges** | [**List[AdministrativeLawJudge]**](AdministrativeLawJudge.md) |  | 
**dispositions** | **List[str]** |  | 
**parties** | [**List[ITCParty]**](ITCParty.md) |  | 
**patents** | [**List[Patent]**](Patent.md) |  | 
**itc_document_list** | [**ITCDocumentList**](ITCDocumentList.md) |  | 

## Example

```python
from lexmachina.models.itc_investigation_data import ITCInvestigationData

# TODO update the JSON string below
json = "{}"
# create an instance of ITCInvestigationData from a JSON string
itc_investigation_data_instance = ITCInvestigationData.from_json(json)
# print the JSON string representation of the object
print(ITCInvestigationData.to_json())

# convert the object into a dict
itc_investigation_data_dict = itc_investigation_data_instance.to_dict()
# create an instance of ITCInvestigationData from a dict
itc_investigation_data_from_dict = ITCInvestigationData.from_dict(itc_investigation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



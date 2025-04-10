# AppealsCaseData

A single case from a federal district appeals court case and relevant metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appeals_case_id** | **int** |  | 
**title** | **str** |  | 
**court** | **str** |  | 
**civil_action_number** | **str** |  | 
**status** | [**CaseStatus**](CaseStatus.md) |  | 
**case_tags** | **List[str]** |  | 
**dates** | [**AppealsCaseDates**](AppealsCaseDates.md) |  | 
**judges** | [**List[FederalJudge]**](FederalJudge.md) |  | 
**law_firms** | [**List[LawFirm]**](LawFirm.md) |  | 
**attorneys** | [**List[Attorney]**](Attorney.md) |  | 
**parties** | [**List[Party]**](Party.md) |  | 
**originating_venues** | **List[str]** |  | 
**originating_cases** | [**List[OriginatingDistrictCourtCase]**](OriginatingDistrictCourtCase.md) |  | 
**appealability_rulings** | **List[str]** |  | 
**case_resolution** | [**CaseResolution**](CaseResolution.md) |  | [optional] 
**supreme_court_and_rehearing_decisions** | [**List[SupremeCourtOrRehearingDecision]**](SupremeCourtOrRehearingDecision.md) |  | 

## Example

```python
from lexmachina.models.appeals_case_data import AppealsCaseData

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCaseData from a JSON string
appeals_case_data_instance = AppealsCaseData.from_json(json)
# print the JSON string representation of the object
print(AppealsCaseData.to_json())

# convert the object into a dict
appeals_case_data_dict = appeals_case_data_instance.to_dict()
# create an instance of AppealsCaseData from a dict
appeals_case_data_from_dict = AppealsCaseData.from_dict(appeals_case_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



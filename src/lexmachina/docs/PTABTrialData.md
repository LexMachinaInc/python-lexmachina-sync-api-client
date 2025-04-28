# PTABTrialData

A single PTAB trial and relevant metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ptab_trial_id** | **int** |  | 
**ptab_trial_number** | **str** |  | 
**status** | [**CaseStatus**](CaseStatus.md) |  | 
**dates** | [**PTABTrialDates**](PTABTrialDates.md) |  | 
**uspto_patent_technology_center** | [**USPTOPatentTechnologyCenter**](USPTOPatentTechnologyCenter.md) |  | 
**administrative_patent_judges** | [**List[AdministrativePatentJudge]**](AdministrativePatentJudge.md) |  | 
**law_firms** | [**List[LawFirm]**](LawFirm.md) |  | 
**attorneys** | [**List[Attorney]**](Attorney.md) |  | 
**parties** | [**List[Party]**](Party.md) |  | 
**trial_type** | **str** |  | 
**trial_tags** | **List[str]** |  | 
**trial_resolution** | **str** |  | 
**patent** | [**PTABPatent**](PTABPatent.md) |  | 
**claim_findings** | [**List[PTABClaimFindings]**](PTABClaimFindings.md) |  | 
**petition_stage_grounds** | [**PTABPetitionStageGround**](PTABPetitionStageGround.md) |  | 
**institution_decision_grounds** | [**List[PTABDecisionGround]**](PTABDecisionGround.md) |  | 
**final_decision_grounds** | [**List[PTABDecisionGround]**](PTABDecisionGround.md) |  | 

## Example

```python
from lexmachina.models.ptab_trial_data import PTABTrialData

# TODO update the JSON string below
json = "{}"
# create an instance of PTABTrialData from a JSON string
ptab_trial_data_instance = PTABTrialData.from_json(json)
# print the JSON string representation of the object
print(PTABTrialData.to_json())

# convert the object into a dict
ptab_trial_data_dict = ptab_trial_data_instance.to_dict()
# create an instance of PTABTrialData from a dict
ptab_trial_data_from_dict = PTABTrialData.from_dict(ptab_trial_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



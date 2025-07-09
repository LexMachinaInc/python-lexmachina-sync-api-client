# DistrictCaseData

A single case from a federal district court case and relevant metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**district_case_id** | **int** |  | 
**title** | **str** |  | 
**court** | **str** |  | 
**case_no** | **str** |  | 
**status** | [**CaseStatus**](CaseStatus.md) |  | 
**case_type** | **List[str]** |  | 
**case_tags** | **List[str]** |  | 
**dates** | [**DistrictCaseDates**](DistrictCaseDates.md) |  | 
**resolution** | [**DistrictCaseResolution**](DistrictCaseResolution.md) |  | [optional] 
**events** | [**List[CaseEvent]**](CaseEvent.md) |  | 
**judges** | [**List[FederalJudge]**](FederalJudge.md) |  | 
**magistrate_judges** | [**List[MagistrateJudge]**](MagistrateJudge.md) |  | 
**remedies** | [**DistrictCaseRemediesByStatus**](DistrictCaseRemediesByStatus.md) |  | 
**findings** | [**DistrictCaseFindingsByStatus**](DistrictCaseFindingsByStatus.md) |  | 
**law_firms** | [**List[LawFirm]**](LawFirm.md) |  | 
**attorneys** | [**List[Attorney]**](Attorney.md) |  | 
**parties** | [**List[Party]**](Party.md) |  | 
**damages** | [**DistrictCaseDamagesByStatus**](DistrictCaseDamagesByStatus.md) |  | 
**patents** | [**List[Patent]**](Patent.md) |  | 
**orders** | [**Orders**](Orders.md) |  | 
**mdl** | [**MultiDistrictLitigation**](MultiDistrictLitigation.md) |  | 
**appeals_cases** | [**List[AppealsCase]**](AppealsCase.md) |  | 
**docket** | [**Docket**](Docket.md) |  | 
**complaint_summary** | [**ComplaintSummary**](ComplaintSummary.md) |  | 

## Example

```python
from lexmachina.models.district_case_data import DistrictCaseData

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseData from a JSON string
district_case_data_instance = DistrictCaseData.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseData.to_json())

# convert the object into a dict
district_case_data_dict = district_case_data_instance.to_dict()
# create an instance of DistrictCaseData from a dict
district_case_data_from_dict = DistrictCaseData.from_dict(district_case_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



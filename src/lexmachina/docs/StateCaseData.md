# StateCaseData

A single case from an enahnced state court and relevant metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_case_id** | **int** |  | 
**title** | **str** |  | 
**state** | **str** |  | 
**court** | **str** |  | 
**case_no** | **str** |  | 
**status** | [**CaseStatus**](CaseStatus.md) |  | 
**case_type** | **List[str]** |  | 
**case_tags** | **List[str]** |  | 
**dates** | [**StateCaseDates**](StateCaseDates.md) |  | 
**resolution** | [**StateCaseResolution**](StateCaseResolution.md) |  | [optional] 
**events** | [**List[CaseEvent]**](CaseEvent.md) |  | 
**judges** | [**List[StateJudge]**](StateJudge.md) |  | 
**rulings** | [**StateCaseRulingsByStatus**](StateCaseRulingsByStatus.md) |  | 
**law_firms** | [**List[LawFirm]**](LawFirm.md) |  | 
**attorneys** | [**List[Attorney]**](Attorney.md) |  | 
**parties** | [**List[Party]**](Party.md) |  | 
**damages** | [**StateCaseDamagesByStatus**](StateCaseDamagesByStatus.md) |  | 
**docket** | [**StateDocket**](StateDocket.md) |  | 

## Example

```python
from lexmachina.models.state_case_data import StateCaseData

# TODO update the JSON string below
json = "{}"
# create an instance of StateCaseData from a JSON string
state_case_data_instance = StateCaseData.from_json(json)
# print the JSON string representation of the object
print(StateCaseData.to_json())

# convert the object into a dict
state_case_data_dict = state_case_data_instance.to_dict()
# create an instance of StateCaseData from a dict
state_case_data_from_dict = StateCaseData.from_dict(state_case_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



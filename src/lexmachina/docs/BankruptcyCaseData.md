# BankruptcyCaseData

A single case from a federal bankruptcy court case and relevant metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankruptcy_case_id** | **int** |  | 
**title** | **str** |  | 
**court** | **str** |  | 
**civil_action_number** | **str** |  | 
**status** | [**CaseStatus**](CaseStatus.md) |  | 
**case_tags** | **List[str]** |  | 
**dates** | [**BankruptcyCaseDates**](BankruptcyCaseDates.md) |  | 
**judges** | [**List[BankruptcyJudge]**](BankruptcyJudge.md) |  | 
**law_firms** | [**List[LawFirm]**](LawFirm.md) |  | 
**attorneys** | [**List[Attorney]**](Attorney.md) |  | 
**parties** | [**List[Party]**](Party.md) |  | 
**assets** | **str** |  | [optional] 
**liabilities** | **str** |  | [optional] 

## Example

```python
from lexmachina.models.bankruptcy_case_data import BankruptcyCaseData

# TODO update the JSON string below
json = "{}"
# create an instance of BankruptcyCaseData from a JSON string
bankruptcy_case_data_instance = BankruptcyCaseData.from_json(json)
# print the JSON string representation of the object
print(BankruptcyCaseData.to_json())

# convert the object into a dict
bankruptcy_case_data_dict = bankruptcy_case_data_instance.to_dict()
# create an instance of BankruptcyCaseData from a dict
bankruptcy_case_data_from_dict = BankruptcyCaseData.from_dict(bankruptcy_case_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



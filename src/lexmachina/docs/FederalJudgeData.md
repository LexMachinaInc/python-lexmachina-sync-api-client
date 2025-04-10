# FederalJudgeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**federal_judge_id** | **int** |  | 
**initials** | **str** |  | 
**date_of_birth** | **date** |  | 
**case_count_by_court** | [**List[CaseCountByCourt]**](CaseCountByCourt.md) |  | 
**nominating_president** | **str** |  | 

## Example

```python
from lexmachina.models.federal_judge_data import FederalJudgeData

# TODO update the JSON string below
json = "{}"
# create an instance of FederalJudgeData from a JSON string
federal_judge_data_instance = FederalJudgeData.from_json(json)
# print the JSON string representation of the object
print(FederalJudgeData.to_json())

# convert the object into a dict
federal_judge_data_dict = federal_judge_data_instance.to_dict()
# create an instance of FederalJudgeData from a dict
federal_judge_data_from_dict = FederalJudgeData.from_dict(federal_judge_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



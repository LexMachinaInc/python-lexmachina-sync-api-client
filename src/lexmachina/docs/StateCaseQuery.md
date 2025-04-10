# StateCaseQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courts** | [**StateCourtFilter**](StateCourtFilter.md) |  | 
**case_status** | [**CaseStatus**](CaseStatus.md) |  | [optional] 
**case_types** | [**CaseTypesFilter**](CaseTypesFilter.md) |  | [optional] 
**case_tags** | [**CaseTagsFilter**](CaseTagsFilter.md) |  | [optional] 
**dates** | [**CaseDatesFilter**](CaseDatesFilter.md) |  | [optional] 
**judges** | [**JudgeFilter**](JudgeFilter.md) |  | [optional] 
**events** | [**EventFilter**](EventFilter.md) |  | [optional] 
**law_firms** | [**LawFirmFilter**](LawFirmFilter.md) |  | [optional] 
**attorneys** | [**AttorneyFilter**](AttorneyFilter.md) |  | [optional] 
**parties** | [**PartyFilter**](PartyFilter.md) |  | [optional] 
**resolutions** | [**ResolutionsFilter**](ResolutionsFilter.md) |  | [optional] 
**damages** | [**List[IndividualStateDamagesFilter]**](IndividualStateDamagesFilter.md) |  | [optional] 
**rulings** | [**List[IndividualRulingsFilter]**](IndividualRulingsFilter.md) |  | [optional] 
**ordering** | [**Ordering**](Ordering.md) |  | [optional] 
**page** | **int** |  | [optional] [default to 1]
**page_size** | **int** |  | [optional] [default to 5]

## Example

```python
from lexmachina.models.state_case_query import StateCaseQuery

# TODO update the JSON string below
json = "{}"
# create an instance of StateCaseQuery from a JSON string
state_case_query_instance = StateCaseQuery.from_json(json)
# print the JSON string representation of the object
print(StateCaseQuery.to_json())

# convert the object into a dict
state_case_query_dict = state_case_query_instance.to_dict()
# create an instance of StateCaseQuery from a dict
state_case_query_from_dict = StateCaseQuery.from_dict(state_case_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



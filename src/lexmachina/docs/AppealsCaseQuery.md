# AppealsCaseQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courts** | [**CourtFilter**](CourtFilter.md) |  | [optional] 
**case_status** | [**CaseStatus**](CaseStatus.md) |  | [optional] 
**case_tags** | [**CaseTagsFilter**](CaseTagsFilter.md) |  | [optional] 
**dates** | [**AppealsCaseDatesFilter**](AppealsCaseDatesFilter.md) |  | [optional] 
**judges** | [**JudgeFilter**](JudgeFilter.md) |  | [optional] 
**law_firms** | [**AppealsLawFirmFilter**](AppealsLawFirmFilter.md) |  | [optional] 
**attorneys** | [**AppealsAttorneyFilter**](AppealsAttorneyFilter.md) |  | [optional] 
**parties** | [**AppealsPartyFilter**](AppealsPartyFilter.md) |  | [optional] 
**originating_venues** | [**OriginatingVenuesFilter**](OriginatingVenuesFilter.md) |  | [optional] 
**originating_cases** | [**OriginatingCasesFilter**](OriginatingCasesFilter.md) |  | [optional] 
**resolutions** | [**ResolutionsFilter**](ResolutionsFilter.md) |  | [optional] 
**supreme_court_decisions** | [**SupremeCourtDecisionsFilter**](SupremeCourtDecisionsFilter.md) |  | [optional] 
**ordering** | [**Ordering**](Ordering.md) |  | [optional] 
**page** | **int** |  | [optional] [default to 1]
**page_size** | **int** |  | [optional] [default to 5]

## Example

```python
from lexmachina.models.appeals_case_query import AppealsCaseQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCaseQuery from a JSON string
appeals_case_query_instance = AppealsCaseQuery.from_json(json)
# print the JSON string representation of the object
print(AppealsCaseQuery.to_json())

# convert the object into a dict
appeals_case_query_dict = appeals_case_query_instance.to_dict()
# create an instance of AppealsCaseQuery from a dict
appeals_case_query_from_dict = AppealsCaseQuery.from_dict(appeals_case_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



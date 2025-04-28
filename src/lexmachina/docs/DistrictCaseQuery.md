# DistrictCaseQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_status** | [**CaseStatus**](CaseStatus.md) |  | [optional] 
**case_types** | [**CaseTypesFilter**](CaseTypesFilter.md) |  | [optional] 
**case_tags** | [**CaseTagsFilter**](CaseTagsFilter.md) |  | [optional] 
**dates** | [**CaseDatesFilter**](CaseDatesFilter.md) |  | [optional] 
**judges** | [**JudgeFilter**](JudgeFilter.md) |  | [optional] 
**magistrates** | [**MagistrateFilter**](MagistrateFilter.md) |  | [optional] 
**events** | [**EventFilter**](EventFilter.md) |  | [optional] 
**law_firms** | [**LawFirmFilter**](LawFirmFilter.md) |  | [optional] 
**attorneys** | [**AttorneyFilter**](AttorneyFilter.md) |  | [optional] 
**parties** | [**PartyFilter**](PartyFilter.md) |  | [optional] 
**courts** | [**CourtFilter**](CourtFilter.md) |  | [optional] 
**resolutions** | [**ResolutionsFilter**](ResolutionsFilter.md) |  | [optional] 
**findings** | [**List[IndividualFindingsFilter]**](IndividualFindingsFilter.md) |  | [optional] 
**remedies** | [**List[IndividualRemediesFilter]**](IndividualRemediesFilter.md) |  | [optional] 
**damages** | [**List[IndividualDamagesFilter]**](IndividualDamagesFilter.md) |  | [optional] 
**patents** | [**PatentFilter**](PatentFilter.md) |  | [optional] 
**mdl** | [**MultidistrictLitigationFilter**](MultidistrictLitigationFilter.md) |  | [optional] 
**appellate_decisions** | [**AppellateDecisionFilter**](AppellateDecisionFilter.md) |  | [optional] 
**ordering** | [**Ordering**](Ordering.md) |  | [optional] 
**page** | **int** |  | [optional] [default to 1]
**page_size** | **int** |  | [optional] [default to 5]

## Example

```python
from lexmachina.models.district_case_query import DistrictCaseQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseQuery from a JSON string
district_case_query_instance = DistrictCaseQuery.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseQuery.to_json())

# convert the object into a dict
district_case_query_dict = district_case_query_instance.to_dict()
# create an instance of DistrictCaseQuery from a dict
district_case_query_from_dict = DistrictCaseQuery.from_dict(district_case_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



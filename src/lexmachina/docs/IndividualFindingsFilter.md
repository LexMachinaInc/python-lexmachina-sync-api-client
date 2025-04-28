# IndividualFindingsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judgment_source** | [**JudgmentSourceFilter**](JudgmentSourceFilter.md) |  | [optional] 
**name_type** | [**NameTypeFilter**](NameTypeFilter.md) |  | [optional] 
**var_date** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**awarded_to_parties** | **List[int]** |  | [optional] 
**awarded_against_parties** | **List[int]** |  | [optional] 
**patent_invalidity_reasons** | [**PatentInvalidityReasonsFilter**](PatentInvalidityReasonsFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.individual_findings_filter import IndividualFindingsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualFindingsFilter from a JSON string
individual_findings_filter_instance = IndividualFindingsFilter.from_json(json)
# print the JSON string representation of the object
print(IndividualFindingsFilter.to_json())

# convert the object into a dict
individual_findings_filter_dict = individual_findings_filter_instance.to_dict()
# create an instance of IndividualFindingsFilter from a dict
individual_findings_filter_from_dict = IndividualFindingsFilter.from_dict(individual_findings_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IndividualRemediesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judgment_source** | [**JudgmentSourceFilter**](JudgmentSourceFilter.md) |  | [optional] 
**name_type** | [**NameTypeFilter**](NameTypeFilter.md) |  | [optional] 
**var_date** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**awarded_to_parties** | **List[int]** |  | [optional] 
**awarded_against_parties** | **List[int]** |  | [optional] 

## Example

```python
from lexmachina.models.individual_remedies_filter import IndividualRemediesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualRemediesFilter from a JSON string
individual_remedies_filter_instance = IndividualRemediesFilter.from_json(json)
# print the JSON string representation of the object
print(IndividualRemediesFilter.to_json())

# convert the object into a dict
individual_remedies_filter_dict = individual_remedies_filter_instance.to_dict()
# create an instance of IndividualRemediesFilter from a dict
individual_remedies_filter_from_dict = IndividualRemediesFilter.from_dict(individual_remedies_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



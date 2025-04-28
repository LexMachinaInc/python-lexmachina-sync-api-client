# IndividualDamagesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judgment_source** | [**JudgmentSourceFilter**](JudgmentSourceFilter.md) |  | [optional] 
**name_type** | [**NameTypeFilter**](NameTypeFilter.md) |  | [optional] 
**var_date** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**awarded_to_parties** | **List[int]** |  | [optional] 
**awarded_against_parties** | **List[int]** |  | [optional] 
**minimum_amount** | [**Minimumamount**](Minimumamount.md) |  | [optional] 

## Example

```python
from lexmachina.models.individual_damages_filter import IndividualDamagesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualDamagesFilter from a JSON string
individual_damages_filter_instance = IndividualDamagesFilter.from_json(json)
# print the JSON string representation of the object
print(IndividualDamagesFilter.to_json())

# convert the object into a dict
individual_damages_filter_dict = individual_damages_filter_instance.to_dict()
# create an instance of IndividualDamagesFilter from a dict
individual_damages_filter_from_dict = IndividualDamagesFilter.from_dict(individual_damages_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



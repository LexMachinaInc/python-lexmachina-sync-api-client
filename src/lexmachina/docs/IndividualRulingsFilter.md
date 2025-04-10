# IndividualRulingsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**judgment_event** | [**JudgmentEventFilter**](JudgmentEventFilter.md) |  | [optional] 
**awarded_to_parties** | **List[int]** |  | [optional] 
**awarded_against_parties** | **List[int]** |  | [optional] 
**var_date** | [**TimingFilter**](TimingFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.individual_rulings_filter import IndividualRulingsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualRulingsFilter from a JSON string
individual_rulings_filter_instance = IndividualRulingsFilter.from_json(json)
# print the JSON string representation of the object
print(IndividualRulingsFilter.to_json())

# convert the object into a dict
individual_rulings_filter_dict = individual_rulings_filter_instance.to_dict()
# create an instance of IndividualRulingsFilter from a dict
individual_rulings_filter_from_dict = IndividualRulingsFilter.from_dict(individual_rulings_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# IndividualStateDamagesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**NameFilter**](NameFilter.md) |  | [optional] 
**var_date** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**awarded_to_parties** | **List[int]** |  | [optional] 
**awarded_against_parties** | **List[int]** |  | [optional] 
**minimum_amount** | [**Minimumamount**](Minimumamount.md) |  | [optional] 

## Example

```python
from lexmachina.models.individual_state_damages_filter import IndividualStateDamagesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualStateDamagesFilter from a JSON string
individual_state_damages_filter_instance = IndividualStateDamagesFilter.from_json(json)
# print the JSON string representation of the object
print(IndividualStateDamagesFilter.to_json())

# convert the object into a dict
individual_state_damages_filter_dict = individual_state_damages_filter_instance.to_dict()
# create an instance of IndividualStateDamagesFilter from a dict
individual_state_damages_filter_from_dict = IndividualStateDamagesFilter.from_dict(individual_state_damages_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



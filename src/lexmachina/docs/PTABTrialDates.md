# PTABTrialDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed** | **date** |  | 
**terminated** | **date** |  | [optional] 
**institution_decision** | **date** |  | 
**final_decision** | **date** |  | 

## Example

```python
from lexmachina.models.ptab_trial_dates import PTABTrialDates

# TODO update the JSON string below
json = "{}"
# create an instance of PTABTrialDates from a JSON string
ptab_trial_dates_instance = PTABTrialDates.from_json(json)
# print the JSON string representation of the object
print(PTABTrialDates.to_json())

# convert the object into a dict
ptab_trial_dates_dict = ptab_trial_dates_instance.to_dict()
# create an instance of PTABTrialDates from a dict
ptab_trial_dates_from_dict = PTABTrialDates.from_dict(ptab_trial_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



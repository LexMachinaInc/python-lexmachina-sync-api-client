# StateCaseDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed** | **date** |  | 
**terminated** | **date** |  | [optional] 
**trial** | **date** |  | 

## Example

```python
from lexmachina.models.state_case_dates import StateCaseDates

# TODO update the JSON string below
json = "{}"
# create an instance of StateCaseDates from a JSON string
state_case_dates_instance = StateCaseDates.from_json(json)
# print the JSON string representation of the object
print(StateCaseDates.to_json())

# convert the object into a dict
state_case_dates_dict = state_case_dates_instance.to_dict()
# create an instance of StateCaseDates from a dict
state_case_dates_from_dict = StateCaseDates.from_dict(state_case_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



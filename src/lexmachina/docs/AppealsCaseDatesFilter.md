# AppealsCaseDatesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**terminated** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**last_docket** | [**TimingFilter**](TimingFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.appeals_case_dates_filter import AppealsCaseDatesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCaseDatesFilter from a JSON string
appeals_case_dates_filter_instance = AppealsCaseDatesFilter.from_json(json)
# print the JSON string representation of the object
print(AppealsCaseDatesFilter.to_json())

# convert the object into a dict
appeals_case_dates_filter_dict = appeals_case_dates_filter_instance.to_dict()
# create an instance of AppealsCaseDatesFilter from a dict
appeals_case_dates_filter_from_dict = AppealsCaseDatesFilter.from_dict(appeals_case_dates_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



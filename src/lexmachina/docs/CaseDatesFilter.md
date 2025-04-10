# CaseDatesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**terminated** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**trial** | [**TimingFilter**](TimingFilter.md) |  | [optional] 
**last_docket** | [**TimingFilter**](TimingFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.case_dates_filter import CaseDatesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CaseDatesFilter from a JSON string
case_dates_filter_instance = CaseDatesFilter.from_json(json)
# print the JSON string representation of the object
print(CaseDatesFilter.to_json())

# convert the object into a dict
case_dates_filter_dict = case_dates_filter_instance.to_dict()
# create an instance of CaseDatesFilter from a dict
case_dates_filter_from_dict = CaseDatesFilter.from_dict(case_dates_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



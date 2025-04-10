# AppealsCaseDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed** | **date** |  | 
**terminated** | **date** |  | [optional] 
**last_docket** | **date** |  | 

## Example

```python
from lexmachina.models.appeals_case_dates import AppealsCaseDates

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCaseDates from a JSON string
appeals_case_dates_instance = AppealsCaseDates.from_json(json)
# print the JSON string representation of the object
print(AppealsCaseDates.to_json())

# convert the object into a dict
appeals_case_dates_dict = appeals_case_dates_instance.to_dict()
# create an instance of AppealsCaseDates from a dict
appeals_case_dates_from_dict = AppealsCaseDates.from_dict(appeals_case_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



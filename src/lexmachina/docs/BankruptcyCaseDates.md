# BankruptcyCaseDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed** | **date** |  | 
**terminated** | **date** |  | [optional] 
**last_docket** | **date** |  | 

## Example

```python
from lexmachina.models.bankruptcy_case_dates import BankruptcyCaseDates

# TODO update the JSON string below
json = "{}"
# create an instance of BankruptcyCaseDates from a JSON string
bankruptcy_case_dates_instance = BankruptcyCaseDates.from_json(json)
# print the JSON string representation of the object
print(BankruptcyCaseDates.to_json())

# convert the object into a dict
bankruptcy_case_dates_dict = bankruptcy_case_dates_instance.to_dict()
# create an instance of BankruptcyCaseDates from a dict
bankruptcy_case_dates_from_dict = BankruptcyCaseDates.from_dict(bankruptcy_case_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



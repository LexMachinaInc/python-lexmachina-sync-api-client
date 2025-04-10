# DistrictCaseDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed** | **date** |  | 
**terminated** | **date** |  | [optional] 
**trial** | **date** |  | 
**last_docket** | **date** |  | 

## Example

```python
from lexmachina.models.district_case_dates import DistrictCaseDates

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseDates from a JSON string
district_case_dates_instance = DistrictCaseDates.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseDates.to_json())

# convert the object into a dict
district_case_dates_dict = district_case_dates_instance.to_dict()
# create an instance of DistrictCaseDates from a dict
district_case_dates_from_dict = DistrictCaseDates.from_dict(district_case_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



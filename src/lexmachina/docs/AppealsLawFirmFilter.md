# AppealsLawFirmFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[int]** |  | [optional] 
**exclude** | **List[int]** |  | [optional] 
**include_appellant** | **List[int]** |  | [optional] 
**exclude_appellant** | **List[int]** |  | [optional] 
**include_appellee** | **List[int]** |  | [optional] 
**exclude_appellee** | **List[int]** |  | [optional] 
**include_respondent** | **List[int]** |  | [optional] 
**exclude_respondent** | **List[int]** |  | [optional] 
**include_third_party** | **List[int]** |  | [optional] 
**exclude_third_party** | **List[int]** |  | [optional] 
**include_petitioner_movant** | **List[int]** |  | [optional] 
**exclude_petitioner_movant** | **List[int]** |  | [optional] 

## Example

```python
from lexmachina.models.appeals_law_firm_filter import AppealsLawFirmFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsLawFirmFilter from a JSON string
appeals_law_firm_filter_instance = AppealsLawFirmFilter.from_json(json)
# print the JSON string representation of the object
print(AppealsLawFirmFilter.to_json())

# convert the object into a dict
appeals_law_firm_filter_dict = appeals_law_firm_filter_instance.to_dict()
# create an instance of AppealsLawFirmFilter from a dict
appeals_law_firm_filter_from_dict = AppealsLawFirmFilter.from_dict(appeals_law_firm_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



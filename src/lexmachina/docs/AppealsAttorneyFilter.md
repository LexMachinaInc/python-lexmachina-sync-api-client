# AppealsAttorneyFilter


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
from lexmachina.models.appeals_attorney_filter import AppealsAttorneyFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsAttorneyFilter from a JSON string
appeals_attorney_filter_instance = AppealsAttorneyFilter.from_json(json)
# print the JSON string representation of the object
print(AppealsAttorneyFilter.to_json())

# convert the object into a dict
appeals_attorney_filter_dict = appeals_attorney_filter_instance.to_dict()
# create an instance of AppealsAttorneyFilter from a dict
appeals_attorney_filter_from_dict = AppealsAttorneyFilter.from_dict(appeals_attorney_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



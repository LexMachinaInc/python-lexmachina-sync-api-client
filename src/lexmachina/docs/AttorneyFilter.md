# AttorneyFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[int]** |  | [optional] 
**exclude** | **List[int]** |  | [optional] 
**include_plaintiff** | **List[int]** |  | [optional] 
**exclude_plaintiff** | **List[int]** |  | [optional] 
**include_defendant** | **List[int]** |  | [optional] 
**exclude_defendant** | **List[int]** |  | [optional] 
**include_third_party** | **List[int]** |  | [optional] 
**exclude_third_party** | **List[int]** |  | [optional] 

## Example

```python
from lexmachina.models.attorney_filter import AttorneyFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyFilter from a JSON string
attorney_filter_instance = AttorneyFilter.from_json(json)
# print the JSON string representation of the object
print(AttorneyFilter.to_json())

# convert the object into a dict
attorney_filter_dict = attorney_filter_instance.to_dict()
# create an instance of AttorneyFilter from a dict
attorney_filter_from_dict = AttorneyFilter.from_dict(attorney_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



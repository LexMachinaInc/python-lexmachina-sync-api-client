# NameFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.name_filter import NameFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NameFilter from a JSON string
name_filter_instance = NameFilter.from_json(json)
# print the JSON string representation of the object
print(NameFilter.to_json())

# convert the object into a dict
name_filter_dict = name_filter_instance.to_dict()
# create an instance of NameFilter from a dict
name_filter_from_dict = NameFilter.from_dict(name_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



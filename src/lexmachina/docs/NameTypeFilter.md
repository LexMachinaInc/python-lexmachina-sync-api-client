# NameTypeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | [**List[IndividualNameTypeFilter]**](IndividualNameTypeFilter.md) |  | [optional] 
**exclude** | [**List[IndividualNameTypeFilter]**](IndividualNameTypeFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.name_type_filter import NameTypeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NameTypeFilter from a JSON string
name_type_filter_instance = NameTypeFilter.from_json(json)
# print the JSON string representation of the object
print(NameTypeFilter.to_json())

# convert the object into a dict
name_type_filter_dict = name_type_filter_instance.to_dict()
# create an instance of NameTypeFilter from a dict
name_type_filter_from_dict = NameTypeFilter.from_dict(name_type_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



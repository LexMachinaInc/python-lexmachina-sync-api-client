# IndividualNameTypeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from lexmachina.models.individual_name_type_filter import IndividualNameTypeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IndividualNameTypeFilter from a JSON string
individual_name_type_filter_instance = IndividualNameTypeFilter.from_json(json)
# print the JSON string representation of the object
print(IndividualNameTypeFilter.to_json())

# convert the object into a dict
individual_name_type_filter_dict = individual_name_type_filter_instance.to_dict()
# create an instance of IndividualNameTypeFilter from a dict
individual_name_type_filter_from_dict = IndividualNameTypeFilter.from_dict(individual_name_type_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



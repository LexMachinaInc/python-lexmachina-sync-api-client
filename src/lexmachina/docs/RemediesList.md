# RemediesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court**](Court.md) |  | [optional] 
**remedies_by_remedy_type** | **Dict[str, List[str]]** |  | 

## Example

```python
from lexmachina.models.remedies_list import RemediesList

# TODO update the JSON string below
json = "{}"
# create an instance of RemediesList from a JSON string
remedies_list_instance = RemediesList.from_json(json)
# print the JSON string representation of the object
print(RemediesList.to_json())

# convert the object into a dict
remedies_list_dict = remedies_list_instance.to_dict()
# create an instance of RemediesList from a dict
remedies_list_from_dict = RemediesList.from_dict(remedies_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



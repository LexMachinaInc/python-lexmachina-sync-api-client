# MagistrateFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[int]** |  | [optional] 
**exclude** | **List[int]** |  | [optional] 

## Example

```python
from lexmachina.models.magistrate_filter import MagistrateFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MagistrateFilter from a JSON string
magistrate_filter_instance = MagistrateFilter.from_json(json)
# print the JSON string representation of the object
print(MagistrateFilter.to_json())

# convert the object into a dict
magistrate_filter_dict = magistrate_filter_instance.to_dict()
# create an instance of MagistrateFilter from a dict
magistrate_filter_from_dict = MagistrateFilter.from_dict(magistrate_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



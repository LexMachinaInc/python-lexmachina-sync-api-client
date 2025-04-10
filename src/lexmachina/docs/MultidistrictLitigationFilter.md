# MultidistrictLitigationFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[int]** |  | [optional] 
**exclude** | **List[int]** |  | [optional] 

## Example

```python
from lexmachina.models.multidistrict_litigation_filter import MultidistrictLitigationFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MultidistrictLitigationFilter from a JSON string
multidistrict_litigation_filter_instance = MultidistrictLitigationFilter.from_json(json)
# print the JSON string representation of the object
print(MultidistrictLitigationFilter.to_json())

# convert the object into a dict
multidistrict_litigation_filter_dict = multidistrict_litigation_filter_instance.to_dict()
# create an instance of MultidistrictLitigationFilter from a dict
multidistrict_litigation_filter_from_dict = MultidistrictLitigationFilter.from_dict(multidistrict_litigation_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



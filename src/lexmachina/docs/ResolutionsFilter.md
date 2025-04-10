# ResolutionsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | [**List[IndividualResolutionsFilter]**](IndividualResolutionsFilter.md) |  | [optional] 
**exclude** | [**List[IndividualResolutionsFilter]**](IndividualResolutionsFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.resolutions_filter import ResolutionsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ResolutionsFilter from a JSON string
resolutions_filter_instance = ResolutionsFilter.from_json(json)
# print the JSON string representation of the object
print(ResolutionsFilter.to_json())

# convert the object into a dict
resolutions_filter_dict = resolutions_filter_instance.to_dict()
# create an instance of ResolutionsFilter from a dict
resolutions_filter_from_dict = ResolutionsFilter.from_dict(resolutions_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



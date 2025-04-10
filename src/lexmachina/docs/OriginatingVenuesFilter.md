# OriginatingVenuesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.originating_venues_filter import OriginatingVenuesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatingVenuesFilter from a JSON string
originating_venues_filter_instance = OriginatingVenuesFilter.from_json(json)
# print the JSON string representation of the object
print(OriginatingVenuesFilter.to_json())

# convert the object into a dict
originating_venues_filter_dict = originating_venues_filter_instance.to_dict()
# create an instance of OriginatingVenuesFilter from a dict
originating_venues_filter_from_dict = OriginatingVenuesFilter.from_dict(originating_venues_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OriginatingVenuesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originating_venues** | **List[str]** |  | 
**court** | [**Court**](Court.md) |  | [optional] 

## Example

```python
from lexmachina.models.originating_venues_list import OriginatingVenuesList

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatingVenuesList from a JSON string
originating_venues_list_instance = OriginatingVenuesList.from_json(json)
# print the JSON string representation of the object
print(OriginatingVenuesList.to_json())

# convert the object into a dict
originating_venues_list_dict = originating_venues_list_instance.to_dict()
# create an instance of OriginatingVenuesList from a dict
originating_venues_list_from_dict = OriginatingVenuesList.from_dict(originating_venues_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



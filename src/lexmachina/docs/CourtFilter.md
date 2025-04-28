# CourtFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.court_filter import CourtFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CourtFilter from a JSON string
court_filter_instance = CourtFilter.from_json(json)
# print the JSON string representation of the object
print(CourtFilter.to_json())

# convert the object into a dict
court_filter_dict = court_filter_instance.to_dict()
# create an instance of CourtFilter from a dict
court_filter_from_dict = CourtFilter.from_dict(court_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



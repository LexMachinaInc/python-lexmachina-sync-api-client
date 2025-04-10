# SupremeCourtDecisionsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.supreme_court_decisions_filter import SupremeCourtDecisionsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SupremeCourtDecisionsFilter from a JSON string
supreme_court_decisions_filter_instance = SupremeCourtDecisionsFilter.from_json(json)
# print the JSON string representation of the object
print(SupremeCourtDecisionsFilter.to_json())

# convert the object into a dict
supreme_court_decisions_filter_dict = supreme_court_decisions_filter_instance.to_dict()
# create an instance of SupremeCourtDecisionsFilter from a dict
supreme_court_decisions_filter_from_dict = SupremeCourtDecisionsFilter.from_dict(supreme_court_decisions_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



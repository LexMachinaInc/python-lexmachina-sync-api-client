# AppellateDecisionFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.appellate_decision_filter import AppellateDecisionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppellateDecisionFilter from a JSON string
appellate_decision_filter_instance = AppellateDecisionFilter.from_json(json)
# print the JSON string representation of the object
print(AppellateDecisionFilter.to_json())

# convert the object into a dict
appellate_decision_filter_dict = appellate_decision_filter_instance.to_dict()
# create an instance of AppellateDecisionFilter from a dict
appellate_decision_filter_from_dict = AppellateDecisionFilter.from_dict(appellate_decision_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



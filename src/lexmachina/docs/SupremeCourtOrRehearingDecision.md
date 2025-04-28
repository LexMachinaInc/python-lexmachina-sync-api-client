# SupremeCourtOrRehearingDecision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docket_entry_filed** | **date** |  | 
**decision** | **str** |  | 
**original_resolution_docket_entry_filed** | **date** |  | [optional] 
**original_resolution** | **str** |  | [optional] 

## Example

```python
from lexmachina.models.supreme_court_or_rehearing_decision import SupremeCourtOrRehearingDecision

# TODO update the JSON string below
json = "{}"
# create an instance of SupremeCourtOrRehearingDecision from a JSON string
supreme_court_or_rehearing_decision_instance = SupremeCourtOrRehearingDecision.from_json(json)
# print the JSON string representation of the object
print(SupremeCourtOrRehearingDecision.to_json())

# convert the object into a dict
supreme_court_or_rehearing_decision_dict = supreme_court_or_rehearing_decision_instance.to_dict()
# create an instance of SupremeCourtOrRehearingDecision from a dict
supreme_court_or_rehearing_decision_from_dict = SupremeCourtOrRehearingDecision.from_dict(supreme_court_or_rehearing_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



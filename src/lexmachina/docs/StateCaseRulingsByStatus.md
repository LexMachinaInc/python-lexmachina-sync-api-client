# StateCaseRulingsByStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[Rulings]**](Rulings.md) |  | 

## Example

```python
from lexmachina.models.state_case_rulings_by_status import StateCaseRulingsByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StateCaseRulingsByStatus from a JSON string
state_case_rulings_by_status_instance = StateCaseRulingsByStatus.from_json(json)
# print the JSON string representation of the object
print(StateCaseRulingsByStatus.to_json())

# convert the object into a dict
state_case_rulings_by_status_dict = state_case_rulings_by_status_instance.to_dict()
# create an instance of StateCaseRulingsByStatus from a dict
state_case_rulings_by_status_from_dict = StateCaseRulingsByStatus.from_dict(state_case_rulings_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ExpertWitnessesAdmissibilityOrderByStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[ExpertWitnessAdmissibilityOrder]**](ExpertWitnessAdmissibilityOrder.md) |  | 
**voided** | [**List[ExpertWitnessAdmissibilityOrder]**](ExpertWitnessAdmissibilityOrder.md) |  | 
**reversed** | [**List[ExpertWitnessAdmissibilityOrder]**](ExpertWitnessAdmissibilityOrder.md) |  | 

## Example

```python
from lexmachina.models.expert_witnesses_admissibility_order_by_status import ExpertWitnessesAdmissibilityOrderByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ExpertWitnessesAdmissibilityOrderByStatus from a JSON string
expert_witnesses_admissibility_order_by_status_instance = ExpertWitnessesAdmissibilityOrderByStatus.from_json(json)
# print the JSON string representation of the object
print(ExpertWitnessesAdmissibilityOrderByStatus.to_json())

# convert the object into a dict
expert_witnesses_admissibility_order_by_status_dict = expert_witnesses_admissibility_order_by_status_instance.to_dict()
# create an instance of ExpertWitnessesAdmissibilityOrderByStatus from a dict
expert_witnesses_admissibility_order_by_status_from_dict = ExpertWitnessesAdmissibilityOrderByStatus.from_dict(expert_witnesses_admissibility_order_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



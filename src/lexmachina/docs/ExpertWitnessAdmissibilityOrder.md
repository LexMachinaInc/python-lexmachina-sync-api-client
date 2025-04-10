# ExpertWitnessAdmissibilityOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expert_witness** | [**ExpertWitness**](ExpertWitness.md) |  | 
**retaining_party_ids** | **List[int]** |  | 
**opposing_party_ids** | **List[int]** |  | 
**judge** | [**Judge**](Judge.md) |  | [optional] 
**docket_entry_filed** | **date** |  | [optional] 
**outcome** | **str** |  | 
**occurred** | **date** |  | 
**negated** | **date** |  | [optional] 
**reinstated** | **date** |  | [optional] 

## Example

```python
from lexmachina.models.expert_witness_admissibility_order import ExpertWitnessAdmissibilityOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ExpertWitnessAdmissibilityOrder from a JSON string
expert_witness_admissibility_order_instance = ExpertWitnessAdmissibilityOrder.from_json(json)
# print the JSON string representation of the object
print(ExpertWitnessAdmissibilityOrder.to_json())

# convert the object into a dict
expert_witness_admissibility_order_dict = expert_witness_admissibility_order_instance.to_dict()
# create an instance of ExpertWitnessAdmissibilityOrder from a dict
expert_witness_admissibility_order_from_dict = ExpertWitnessAdmissibilityOrder.from_dict(expert_witness_admissibility_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



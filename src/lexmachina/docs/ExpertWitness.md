# ExpertWitness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**expert_witness_id** | **int** |  | 

## Example

```python
from lexmachina.models.expert_witness import ExpertWitness

# TODO update the JSON string below
json = "{}"
# create an instance of ExpertWitness from a JSON string
expert_witness_instance = ExpertWitness.from_json(json)
# print the JSON string representation of the object
print(ExpertWitness.to_json())

# convert the object into a dict
expert_witness_dict = expert_witness_instance.to_dict()
# create an instance of ExpertWitness from a dict
expert_witness_from_dict = ExpertWitness.from_dict(expert_witness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



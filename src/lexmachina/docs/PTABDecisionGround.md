# PTABDecisionGround


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | **str** |  | 
**statute** | **str** |  | 
**claims** | **List[int]** |  | 
**prior_art** | [**List[PriorArt]**](PriorArt.md) |  | 

## Example

```python
from lexmachina.models.ptab_decision_ground import PTABDecisionGround

# TODO update the JSON string below
json = "{}"
# create an instance of PTABDecisionGround from a JSON string
ptab_decision_ground_instance = PTABDecisionGround.from_json(json)
# print the JSON string representation of the object
print(PTABDecisionGround.to_json())

# convert the object into a dict
ptab_decision_ground_dict = ptab_decision_ground_instance.to_dict()
# create an instance of PTABDecisionGround from a dict
ptab_decision_ground_from_dict = PTABDecisionGround.from_dict(ptab_decision_ground_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



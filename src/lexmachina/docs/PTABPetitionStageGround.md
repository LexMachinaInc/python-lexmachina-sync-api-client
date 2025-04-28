# PTABPetitionStageGround


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statutes** | **List[str]** |  | 
**prior_art** | [**List[PriorArt]**](PriorArt.md) |  | 

## Example

```python
from lexmachina.models.ptab_petition_stage_ground import PTABPetitionStageGround

# TODO update the JSON string below
json = "{}"
# create an instance of PTABPetitionStageGround from a JSON string
ptab_petition_stage_ground_instance = PTABPetitionStageGround.from_json(json)
# print the JSON string representation of the object
print(PTABPetitionStageGround.to_json())

# convert the object into a dict
ptab_petition_stage_ground_dict = ptab_petition_stage_ground_instance.to_dict()
# create an instance of PTABPetitionStageGround from a dict
ptab_petition_stage_ground_from_dict = PTABPetitionStageGround.from_dict(ptab_petition_stage_ground_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



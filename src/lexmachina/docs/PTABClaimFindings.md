# PTABClaimFindings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numbers** | **List[int]** |  | 
**petition** | **str** |  | 
**institution_decision** | **str** |  | 
**final_written_decision** | **str** |  | 

## Example

```python
from lexmachina.models.ptab_claim_findings import PTABClaimFindings

# TODO update the JSON string below
json = "{}"
# create an instance of PTABClaimFindings from a JSON string
ptab_claim_findings_instance = PTABClaimFindings.from_json(json)
# print the JSON string representation of the object
print(PTABClaimFindings.to_json())

# convert the object into a dict
ptab_claim_findings_dict = ptab_claim_findings_instance.to_dict()
# create an instance of PTABClaimFindings from a dict
ptab_claim_findings_from_dict = PTABClaimFindings.from_dict(ptab_claim_findings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



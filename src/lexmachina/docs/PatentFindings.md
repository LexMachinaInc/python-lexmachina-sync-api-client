# PatentFindings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **List[int]** |  | 
**type** | **List[str]** |  | 
**winner** | **str** |  | 

## Example

```python
from lexmachina.models.patent_findings import PatentFindings

# TODO update the JSON string below
json = "{}"
# create an instance of PatentFindings from a JSON string
patent_findings_instance = PatentFindings.from_json(json)
# print the JSON string representation of the object
print(PatentFindings.to_json())

# convert the object into a dict
patent_findings_dict = patent_findings_instance.to_dict()
# create an instance of PatentFindings from a dict
patent_findings_from_dict = PatentFindings.from_dict(patent_findings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



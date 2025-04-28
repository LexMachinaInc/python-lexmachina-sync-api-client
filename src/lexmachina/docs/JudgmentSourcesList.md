# JudgmentSourcesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court**](Court.md) |  | [optional] 
**damages** | **List[str]** |  | 
**remedies** | **List[str]** |  | 
**findings** | **List[str]** |  | 

## Example

```python
from lexmachina.models.judgment_sources_list import JudgmentSourcesList

# TODO update the JSON string below
json = "{}"
# create an instance of JudgmentSourcesList from a JSON string
judgment_sources_list_instance = JudgmentSourcesList.from_json(json)
# print the JSON string representation of the object
print(JudgmentSourcesList.to_json())

# convert the object into a dict
judgment_sources_list_dict = judgment_sources_list_instance.to_dict()
# create an instance of JudgmentSourcesList from a dict
judgment_sources_list_from_dict = JudgmentSourcesList.from_dict(judgment_sources_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



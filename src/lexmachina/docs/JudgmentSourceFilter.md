# JudgmentSourceFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.judgment_source_filter import JudgmentSourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of JudgmentSourceFilter from a JSON string
judgment_source_filter_instance = JudgmentSourceFilter.from_json(json)
# print the JSON string representation of the object
print(JudgmentSourceFilter.to_json())

# convert the object into a dict
judgment_source_filter_dict = judgment_source_filter_instance.to_dict()
# create an instance of JudgmentSourceFilter from a dict
judgment_source_filter_from_dict = JudgmentSourceFilter.from_dict(judgment_source_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



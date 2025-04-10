# PatentInvalidityReasonsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.patent_invalidity_reasons_filter import PatentInvalidityReasonsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PatentInvalidityReasonsFilter from a JSON string
patent_invalidity_reasons_filter_instance = PatentInvalidityReasonsFilter.from_json(json)
# print the JSON string representation of the object
print(PatentInvalidityReasonsFilter.to_json())

# convert the object into a dict
patent_invalidity_reasons_filter_dict = patent_invalidity_reasons_filter_instance.to_dict()
# create an instance of PatentInvalidityReasonsFilter from a dict
patent_invalidity_reasons_filter_from_dict = PatentInvalidityReasonsFilter.from_dict(patent_invalidity_reasons_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



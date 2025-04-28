# PatentFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**exclude** | **List[str]** |  | [optional] 

## Example

```python
from lexmachina.models.patent_filter import PatentFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PatentFilter from a JSON string
patent_filter_instance = PatentFilter.from_json(json)
# print the JSON string representation of the object
print(PatentFilter.to_json())

# convert the object into a dict
patent_filter_dict = patent_filter_instance.to_dict()
# create an instance of PatentFilter from a dict
patent_filter_from_dict = PatentFilter.from_dict(patent_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



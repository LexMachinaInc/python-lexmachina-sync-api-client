# Patent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | 
**title** | **str** |  | [optional] 

## Example

```python
from lexmachina.models.patent import Patent

# TODO update the JSON string below
json = "{}"
# create an instance of Patent from a JSON string
patent_instance = Patent.from_json(json)
# print the JSON string representation of the object
print(Patent.to_json())

# convert the object into a dict
patent_dict = patent_instance.to_dict()
# create an instance of Patent from a dict
patent_from_dict = Patent.from_dict(patent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



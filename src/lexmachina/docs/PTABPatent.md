# PTABPatent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | 
**title** | **str** |  | [optional] 
**application_number** | **str** |  | 

## Example

```python
from lexmachina.models.ptab_patent import PTABPatent

# TODO update the JSON string below
json = "{}"
# create an instance of PTABPatent from a JSON string
ptab_patent_instance = PTABPatent.from_json(json)
# print the JSON string representation of the object
print(PTABPatent.to_json())

# convert the object into a dict
ptab_patent_dict = ptab_patent_instance.to_dict()
# create an instance of PTABPatent from a dict
ptab_patent_from_dict = PTABPatent.from_dict(ptab_patent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



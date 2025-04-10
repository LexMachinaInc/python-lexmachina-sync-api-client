# DocketEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filed_on** | **date** |  | 
**tags** | **List[str]** |  | 
**text** | **str** |  | 
**number** | **int** |  | 
**docket_entry_id** | **int** |  | 

## Example

```python
from lexmachina.models.docket_entry import DocketEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DocketEntry from a JSON string
docket_entry_instance = DocketEntry.from_json(json)
# print the JSON string representation of the object
print(DocketEntry.to_json())

# convert the object into a dict
docket_entry_dict = docket_entry_instance.to_dict()
# create an instance of DocketEntry from a dict
docket_entry_from_dict = DocketEntry.from_dict(docket_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



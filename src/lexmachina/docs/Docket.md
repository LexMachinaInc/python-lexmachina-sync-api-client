# Docket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[DocketEntry]**](DocketEntry.md) |  | 
**retrieved** | [**DocketEntriesIncludedInOutput**](DocketEntriesIncludedInOutput.md) |  | 
**count** | **int** |  | 

## Example

```python
from lexmachina.models.docket import Docket

# TODO update the JSON string below
json = "{}"
# create an instance of Docket from a JSON string
docket_instance = Docket.from_json(json)
# print the JSON string representation of the object
print(Docket.to_json())

# convert the object into a dict
docket_dict = docket_instance.to_dict()
# create an instance of Docket from a dict
docket_from_dict = Docket.from_dict(docket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



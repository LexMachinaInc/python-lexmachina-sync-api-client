# Court1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**CourtType**](CourtType.md) |  | 
**state** | **str** |  | 

## Example

```python
from lexmachina.models.court1 import Court1

# TODO update the JSON string below
json = "{}"
# create an instance of Court1 from a JSON string
court1_instance = Court1.from_json(json)
# print the JSON string representation of the object
print(Court1.to_json())

# convert the object into a dict
court1_dict = court1_instance.to_dict()
# create an instance of Court1 from a dict
court1_from_dict = Court1.from_dict(court1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



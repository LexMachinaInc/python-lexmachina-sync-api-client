# Court


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**CourtType**](CourtType.md) |  | 

## Example

```python
from lexmachina.models.court import Court

# TODO update the JSON string below
json = "{}"
# create an instance of Court from a JSON string
court_instance = Court.from_json(json)
# print the JSON string representation of the object
print(Court.to_json())

# convert the object into a dict
court_dict = court_instance.to_dict()
# create an instance of Court from a dict
court_from_dict = Court.from_dict(court_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



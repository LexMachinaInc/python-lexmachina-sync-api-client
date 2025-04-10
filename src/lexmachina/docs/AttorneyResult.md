# AttorneyResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attorney_id** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from lexmachina.models.attorney_result import AttorneyResult

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyResult from a JSON string
attorney_result_instance = AttorneyResult.from_json(json)
# print the JSON string representation of the object
print(AttorneyResult.to_json())

# convert the object into a dict
attorney_result_dict = attorney_result_instance.to_dict()
# create an instance of AttorneyResult from a dict
attorney_result_from_dict = AttorneyResult.from_dict(attorney_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



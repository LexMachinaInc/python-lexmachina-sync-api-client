# AttorneyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attorney_id** | **int** |  | 

## Example

```python
from lexmachina.models.attorney_data import AttorneyData

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyData from a JSON string
attorney_data_instance = AttorneyData.from_json(json)
# print the JSON string representation of the object
print(AttorneyData.to_json())

# convert the object into a dict
attorney_data_dict = attorney_data_instance.to_dict()
# create an instance of AttorneyData from a dict
attorney_data_from_dict = AttorneyData.from_dict(attorney_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



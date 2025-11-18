# CountsPerRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from lexmachina.models.counts_per_role import CountsPerRole

# TODO update the JSON string below
json = "{}"
# create an instance of CountsPerRole from a JSON string
counts_per_role_instance = CountsPerRole.from_json(json)
# print the JSON string representation of the object
print(CountsPerRole.to_json())

# convert the object into a dict
counts_per_role_dict = counts_per_role_instance.to_dict()
# create an instance of CountsPerRole from a dict
counts_per_role_from_dict = CountsPerRole.from_dict(counts_per_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



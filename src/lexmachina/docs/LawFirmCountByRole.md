# LawFirmCountByRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**law_firm_id** | **int** |  | 
**law_firm_name** | **str** |  | 
**roles_and_counts** | [**List[CountsPerRole]**](CountsPerRole.md) |  | 

## Example

```python
from lexmachina.models.law_firm_count_by_role import LawFirmCountByRole

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirmCountByRole from a JSON string
law_firm_count_by_role_instance = LawFirmCountByRole.from_json(json)
# print the JSON string representation of the object
print(LawFirmCountByRole.to_json())

# convert the object into a dict
law_firm_count_by_role_dict = law_firm_count_by_role_instance.to_dict()
# create an instance of LawFirmCountByRole from a dict
law_firm_count_by_role_from_dict = LawFirmCountByRole.from_dict(law_firm_count_by_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MultiDistrictLitigation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mdl_no** | **List[int]** |  | 
**master_case_ids** | **List[int]** |  | 
**truncated_data** | **bool** |  | 

## Example

```python
from lexmachina.models.multi_district_litigation import MultiDistrictLitigation

# TODO update the JSON string below
json = "{}"
# create an instance of MultiDistrictLitigation from a JSON string
multi_district_litigation_instance = MultiDistrictLitigation.from_json(json)
# print the JSON string representation of the object
print(MultiDistrictLitigation.to_json())

# convert the object into a dict
multi_district_litigation_dict = multi_district_litigation_instance.to_dict()
# create an instance of MultiDistrictLitigation from a dict
multi_district_litigation_from_dict = MultiDistrictLitigation.from_dict(multi_district_litigation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



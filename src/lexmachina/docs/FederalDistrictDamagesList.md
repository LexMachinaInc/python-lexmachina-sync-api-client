# FederalDistrictDamagesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court**](Court.md) |  | [optional] 
**damages_by_pratice_area** | **Dict[str, List[str]]** |  | 

## Example

```python
from lexmachina.models.federal_district_damages_list import FederalDistrictDamagesList

# TODO update the JSON string below
json = "{}"
# create an instance of FederalDistrictDamagesList from a JSON string
federal_district_damages_list_instance = FederalDistrictDamagesList.from_json(json)
# print the JSON string representation of the object
print(FederalDistrictDamagesList.to_json())

# convert the object into a dict
federal_district_damages_list_dict = federal_district_damages_list_instance.to_dict()
# create an instance of FederalDistrictDamagesList from a dict
federal_district_damages_list_from_dict = FederalDistrictDamagesList.from_dict(federal_district_damages_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



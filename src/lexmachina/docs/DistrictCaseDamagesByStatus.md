# DistrictCaseDamagesByStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[DistrictCaseDamages]**](DistrictCaseDamages.md) |  | 
**voided** | [**List[DistrictCaseDamages]**](DistrictCaseDamages.md) |  | 
**reversed** | [**List[DistrictCaseDamages]**](DistrictCaseDamages.md) |  | 

## Example

```python
from lexmachina.models.district_case_damages_by_status import DistrictCaseDamagesByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseDamagesByStatus from a JSON string
district_case_damages_by_status_instance = DistrictCaseDamagesByStatus.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseDamagesByStatus.to_json())

# convert the object into a dict
district_case_damages_by_status_dict = district_case_damages_by_status_instance.to_dict()
# create an instance of DistrictCaseDamagesByStatus from a dict
district_case_damages_by_status_from_dict = DistrictCaseDamagesByStatus.from_dict(district_case_damages_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



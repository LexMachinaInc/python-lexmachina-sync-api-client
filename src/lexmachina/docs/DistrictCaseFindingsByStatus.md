# DistrictCaseFindingsByStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[DistrictCaseFinding]**](DistrictCaseFinding.md) |  | 
**voided** | [**List[DistrictCaseFinding]**](DistrictCaseFinding.md) |  | 
**reversed** | [**List[DistrictCaseFinding]**](DistrictCaseFinding.md) |  | 

## Example

```python
from lexmachina.models.district_case_findings_by_status import DistrictCaseFindingsByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseFindingsByStatus from a JSON string
district_case_findings_by_status_instance = DistrictCaseFindingsByStatus.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseFindingsByStatus.to_json())

# convert the object into a dict
district_case_findings_by_status_dict = district_case_findings_by_status_instance.to_dict()
# create an instance of DistrictCaseFindingsByStatus from a dict
district_case_findings_by_status_from_dict = DistrictCaseFindingsByStatus.from_dict(district_case_findings_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



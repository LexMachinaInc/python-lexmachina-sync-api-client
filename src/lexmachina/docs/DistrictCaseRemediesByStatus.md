# DistrictCaseRemediesByStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[DistrictCaseRemedy]**](DistrictCaseRemedy.md) |  | 
**voided** | [**List[DistrictCaseRemedy]**](DistrictCaseRemedy.md) |  | 
**reversed** | [**List[DistrictCaseRemedy]**](DistrictCaseRemedy.md) |  | 

## Example

```python
from lexmachina.models.district_case_remedies_by_status import DistrictCaseRemediesByStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseRemediesByStatus from a JSON string
district_case_remedies_by_status_instance = DistrictCaseRemediesByStatus.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseRemediesByStatus.to_json())

# convert the object into a dict
district_case_remedies_by_status_dict = district_case_remedies_by_status_instance.to_dict()
# create an instance of DistrictCaseRemediesByStatus from a dict
district_case_remedies_by_status_from_dict = DistrictCaseRemediesByStatus.from_dict(district_case_remedies_by_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



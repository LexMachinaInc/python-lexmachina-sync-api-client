# FederalDistrictCourt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**CourtType**](CourtType.md) |  | 
**short_name** | **str** |  | 
**abbreviation** | **str** |  | 

## Example

```python
from lexmachina.models.federal_district_court import FederalDistrictCourt

# TODO update the JSON string below
json = "{}"
# create an instance of FederalDistrictCourt from a JSON string
federal_district_court_instance = FederalDistrictCourt.from_json(json)
# print the JSON string representation of the object
print(FederalDistrictCourt.to_json())

# convert the object into a dict
federal_district_court_dict = federal_district_court_instance.to_dict()
# create an instance of FederalDistrictCourt from a dict
federal_district_court_from_dict = FederalDistrictCourt.from_dict(federal_district_court_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



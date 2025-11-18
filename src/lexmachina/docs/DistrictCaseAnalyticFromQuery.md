# DistrictCaseAnalyticFromQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic_type** | [**AnalyticTypes**](AnalyticTypes.md) |  | 
**district_case_query** | [**DistrictCaseQuery**](DistrictCaseQuery.md) |  | 

## Example

```python
from lexmachina.models.district_case_analytic_from_query import DistrictCaseAnalyticFromQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseAnalyticFromQuery from a JSON string
district_case_analytic_from_query_instance = DistrictCaseAnalyticFromQuery.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseAnalyticFromQuery.to_json())

# convert the object into a dict
district_case_analytic_from_query_dict = district_case_analytic_from_query_instance.to_dict()
# create an instance of DistrictCaseAnalyticFromQuery from a dict
district_case_analytic_from_query_from_dict = DistrictCaseAnalyticFromQuery.from_dict(district_case_analytic_from_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



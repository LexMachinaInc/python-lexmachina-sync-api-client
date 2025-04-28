# DistrictCaseQueryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**List[DistrictCaseReference]**](DistrictCaseReference.md) |  | 

## Example

```python
from lexmachina.models.district_case_query_result import DistrictCaseQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of DistrictCaseQueryResult from a JSON string
district_case_query_result_instance = DistrictCaseQueryResult.from_json(json)
# print the JSON string representation of the object
print(DistrictCaseQueryResult.to_json())

# convert the object into a dict
district_case_query_result_dict = district_case_query_result_instance.to_dict()
# create an instance of DistrictCaseQueryResult from a dict
district_case_query_result_from_dict = DistrictCaseQueryResult.from_dict(district_case_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



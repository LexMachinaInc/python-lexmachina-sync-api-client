# AppealsCaseQueryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**List[AppealsCaseReference]**](AppealsCaseReference.md) |  | 

## Example

```python
from lexmachina.models.appeals_case_query_result import AppealsCaseQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCaseQueryResult from a JSON string
appeals_case_query_result_instance = AppealsCaseQueryResult.from_json(json)
# print the JSON string representation of the object
print(AppealsCaseQueryResult.to_json())

# convert the object into a dict
appeals_case_query_result_dict = appeals_case_query_result_instance.to_dict()
# create an instance of AppealsCaseQueryResult from a dict
appeals_case_query_result_from_dict = AppealsCaseQueryResult.from_dict(appeals_case_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



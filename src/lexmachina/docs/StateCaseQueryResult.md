# StateCaseQueryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cases** | [**List[StateCaseReference]**](StateCaseReference.md) |  | 

## Example

```python
from lexmachina.models.state_case_query_result import StateCaseQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of StateCaseQueryResult from a JSON string
state_case_query_result_instance = StateCaseQueryResult.from_json(json)
# print the JSON string representation of the object
print(StateCaseQueryResult.to_json())

# convert the object into a dict
state_case_query_result_dict = state_case_query_result_instance.to_dict()
# create an instance of StateCaseQueryResult from a dict
state_case_query_result_from_dict = StateCaseQueryResult.from_dict(state_case_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



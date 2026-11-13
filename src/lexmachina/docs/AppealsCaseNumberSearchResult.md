# AppealsCaseNumberSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**input_case_number** | **str** |  | 
**input_court** | **str** |  | [optional] 
**matches** | [**List[AppealsCaseNumberReference]**](AppealsCaseNumberReference.md) |  | 

## Example

```python
from lexmachina.models.appeals_case_number_search_result import AppealsCaseNumberSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsCaseNumberSearchResult from a JSON string
appeals_case_number_search_result_instance = AppealsCaseNumberSearchResult.from_json(json)
# print the JSON string representation of the object
print(AppealsCaseNumberSearchResult.to_json())

# convert the object into a dict
appeals_case_number_search_result_dict = appeals_case_number_search_result_instance.to_dict()
# create an instance of AppealsCaseNumberSearchResult from a dict
appeals_case_number_search_result_from_dict = AppealsCaseNumberSearchResult.from_dict(appeals_case_number_search_result_dict)
```
[[Back to Model list]](../../../README.md#documentation-for-models) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to README]](../../../README.md)



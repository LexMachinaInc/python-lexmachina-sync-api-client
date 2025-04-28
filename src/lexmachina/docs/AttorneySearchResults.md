# AttorneySearchResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**page** | **int** |  | 
**next_page** | **str** |  | [optional] 
**attorneys** | [**List[AttorneyResult]**](AttorneyResult.md) |  | 

## Example

```python
from lexmachina.models.attorney_search_results import AttorneySearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneySearchResults from a JSON string
attorney_search_results_instance = AttorneySearchResults.from_json(json)
# print the JSON string representation of the object
print(AttorneySearchResults.to_json())

# convert the object into a dict
attorney_search_results_dict = attorney_search_results_instance.to_dict()
# create an instance of AttorneySearchResults from a dict
attorney_search_results_from_dict = AttorneySearchResults.from_dict(attorney_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



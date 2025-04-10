# LawFirmSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**page** | **int** |  | 
**next_page** | **str** |  | [optional] 
**law_firms** | [**List[LawFirmResult]**](LawFirmResult.md) |  | 

## Example

```python
from lexmachina.models.law_firm_search_result import LawFirmSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirmSearchResult from a JSON string
law_firm_search_result_instance = LawFirmSearchResult.from_json(json)
# print the JSON string representation of the object
print(LawFirmSearchResult.to_json())

# convert the object into a dict
law_firm_search_result_dict = law_firm_search_result_instance.to_dict()
# create an instance of LawFirmSearchResult from a dict
law_firm_search_result_from_dict = LawFirmSearchResult.from_dict(law_firm_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



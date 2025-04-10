# PartySearchResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**page** | **int** |  | 
**next_page** | **str** |  | [optional] 
**parties** | [**List[PartyResult]**](PartyResult.md) |  | 

## Example

```python
from lexmachina.models.party_search_results import PartySearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of PartySearchResults from a JSON string
party_search_results_instance = PartySearchResults.from_json(json)
# print the JSON string representation of the object
print(PartySearchResults.to_json())

# convert the object into a dict
party_search_results_dict = party_search_results_instance.to_dict()
# create an instance of PartySearchResults from a dict
party_search_results_from_dict = PartySearchResults.from_dict(party_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



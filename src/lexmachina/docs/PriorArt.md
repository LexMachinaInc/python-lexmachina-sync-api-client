# PriorArt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prior_art_type** | **str** |  | 
**prior_art_references** | **List[str]** |  | 

## Example

```python
from lexmachina.models.prior_art import PriorArt

# TODO update the JSON string below
json = "{}"
# create an instance of PriorArt from a JSON string
prior_art_instance = PriorArt.from_json(json)
# print the JSON string representation of the object
print(PriorArt.to_json())

# convert the object into a dict
prior_art_dict = prior_art_instance.to_dict()
# create an instance of PriorArt from a dict
prior_art_from_dict = PriorArt.from_dict(prior_art_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



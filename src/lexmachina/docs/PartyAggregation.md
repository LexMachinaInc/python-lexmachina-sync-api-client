# PartyAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PartyCountByRole]**](PartyCountByRole.md) |  | 

## Example

```python
from lexmachina.models.party_aggregation import PartyAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of PartyAggregation from a JSON string
party_aggregation_instance = PartyAggregation.from_json(json)
# print the JSON string representation of the object
print(PartyAggregation.to_json())

# convert the object into a dict
party_aggregation_dict = party_aggregation_instance.to_dict()
# create an instance of PartyAggregation from a dict
party_aggregation_from_dict = PartyAggregation.from_dict(party_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



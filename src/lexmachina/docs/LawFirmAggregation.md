# LawFirmAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LawFirmCountByRole]**](LawFirmCountByRole.md) |  | 

## Example

```python
from lexmachina.models.law_firm_aggregation import LawFirmAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of LawFirmAggregation from a JSON string
law_firm_aggregation_instance = LawFirmAggregation.from_json(json)
# print the JSON string representation of the object
print(LawFirmAggregation.to_json())

# convert the object into a dict
law_firm_aggregation_dict = law_firm_aggregation_instance.to_dict()
# create an instance of LawFirmAggregation from a dict
law_firm_aggregation_from_dict = LawFirmAggregation.from_dict(law_firm_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



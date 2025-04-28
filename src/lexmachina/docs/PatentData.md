# PatentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | 
**title** | **str** |  | [optional] 
**abstract** | **str** |  | [optional] 
**inventors** | [**Inventors**](Inventors.md) |  | 
**district_court_cases** | [**PatentCaseInformation**](PatentCaseInformation.md) |  | 

## Example

```python
from lexmachina.models.patent_data import PatentData

# TODO update the JSON string below
json = "{}"
# create an instance of PatentData from a JSON string
patent_data_instance = PatentData.from_json(json)
# print the JSON string representation of the object
print(PatentData.to_json())

# convert the object into a dict
patent_data_dict = patent_data_instance.to_dict()
# create an instance of PatentData from a dict
patent_data_from_dict = PatentData.from_dict(patent_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



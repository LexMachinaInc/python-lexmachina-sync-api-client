# PatentCaseInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_cases** | **int** |  | 
**findings** | [**List[PatentFindings]**](PatentFindings.md) |  | 

## Example

```python
from lexmachina.models.patent_case_information import PatentCaseInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PatentCaseInformation from a JSON string
patent_case_information_instance = PatentCaseInformation.from_json(json)
# print the JSON string representation of the object
print(PatentCaseInformation.to_json())

# convert the object into a dict
patent_case_information_dict = patent_case_information_instance.to_dict()
# create an instance of PatentCaseInformation from a dict
patent_case_information_from_dict = PatentCaseInformation.from_dict(patent_case_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



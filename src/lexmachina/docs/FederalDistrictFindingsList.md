# FederalDistrictFindingsList

findingsByPracticeArea: a dictionary where the key is the name and the values are all the relevant types for supported findings.  patentInvalidityReasons: only applicable to findings when the finding has {\"name\":\"Patent\",\"type\":\"Invalidity\"}.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**court** | [**Court**](Court.md) |  | [optional] 
**findings_by_practice_area** | **Dict[str, List[str]]** |  | 
**patent_invalidity_reasons** | **List[str]** |  | 

## Example

```python
from lexmachina.models.federal_district_findings_list import FederalDistrictFindingsList

# TODO update the JSON string below
json = "{}"
# create an instance of FederalDistrictFindingsList from a JSON string
federal_district_findings_list_instance = FederalDistrictFindingsList.from_json(json)
# print the JSON string representation of the object
print(FederalDistrictFindingsList.to_json())

# convert the object into a dict
federal_district_findings_list_dict = federal_district_findings_list_instance.to_dict()
# create an instance of FederalDistrictFindingsList from a dict
federal_district_findings_list_from_dict = FederalDistrictFindingsList.from_dict(federal_district_findings_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



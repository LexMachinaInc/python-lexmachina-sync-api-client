# AdministrativePatentJudge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**administrative_patent_judge_id** | **int** |  | 
**details** | [**List[AdministrativePatentJudgeDetail]**](AdministrativePatentJudgeDetail.md) |  | 

## Example

```python
from lexmachina.models.administrative_patent_judge import AdministrativePatentJudge

# TODO update the JSON string below
json = "{}"
# create an instance of AdministrativePatentJudge from a JSON string
administrative_patent_judge_instance = AdministrativePatentJudge.from_json(json)
# print the JSON string representation of the object
print(AdministrativePatentJudge.to_json())

# convert the object into a dict
administrative_patent_judge_dict = administrative_patent_judge_instance.to_dict()
# create an instance of AdministrativePatentJudge from a dict
administrative_patent_judge_from_dict = AdministrativePatentJudge.from_dict(administrative_patent_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# OriginatingJudgeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**district_federal_judges** | [**JudgeFilter**](JudgeFilter.md) |  | [optional] 

## Example

```python
from lexmachina.models.originating_judge_filter import OriginatingJudgeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OriginatingJudgeFilter from a JSON string
originating_judge_filter_instance = OriginatingJudgeFilter.from_json(json)
# print the JSON string representation of the object
print(OriginatingJudgeFilter.to_json())

# convert the object into a dict
originating_judge_filter_dict = originating_judge_filter_instance.to_dict()
# create an instance of OriginatingJudgeFilter from a dict
originating_judge_filter_from_dict = OriginatingJudgeFilter.from_dict(originating_judge_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



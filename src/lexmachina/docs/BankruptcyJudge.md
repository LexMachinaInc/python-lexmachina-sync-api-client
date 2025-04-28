# BankruptcyJudge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**bankruptcy_judge_id** | **int** |  | 

## Example

```python
from lexmachina.models.bankruptcy_judge import BankruptcyJudge

# TODO update the JSON string below
json = "{}"
# create an instance of BankruptcyJudge from a JSON string
bankruptcy_judge_instance = BankruptcyJudge.from_json(json)
# print the JSON string representation of the object
print(BankruptcyJudge.to_json())

# convert the object into a dict
bankruptcy_judge_dict = bankruptcy_judge_instance.to_dict()
# create an instance of BankruptcyJudge from a dict
bankruptcy_judge_from_dict = BankruptcyJudge.from_dict(bankruptcy_judge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



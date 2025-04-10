# AttorneyReference

Indicates that the Lex Machina attorney id input was has changed, the inputId is the ID given that should map to the returned attorneyId.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attorney_id** | **int** |  | 
**url** | **str** |  | 
**input_id** | **int** |  | 

## Example

```python
from lexmachina.models.attorney_reference import AttorneyReference

# TODO update the JSON string below
json = "{}"
# create an instance of AttorneyReference from a JSON string
attorney_reference_instance = AttorneyReference.from_json(json)
# print the JSON string representation of the object
print(AttorneyReference.to_json())

# convert the object into a dict
attorney_reference_dict = attorney_reference_instance.to_dict()
# create an instance of AttorneyReference from a dict
attorney_reference_from_dict = AttorneyReference.from_dict(attorney_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



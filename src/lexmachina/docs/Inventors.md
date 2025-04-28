# Inventors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventors** | **List[str]** |  | 
**original_assignee** | **List[object]** |  | 
**filing_date** | **date** |  | 
**issue_date** | **date** |  | 

## Example

```python
from lexmachina.models.inventors import Inventors

# TODO update the JSON string below
json = "{}"
# create an instance of Inventors from a JSON string
inventors_instance = Inventors.from_json(json)
# print the JSON string representation of the object
print(Inventors.to_json())

# convert the object into a dict
inventors_dict = inventors_instance.to_dict()
# create an instance of Inventors from a dict
inventors_from_dict = Inventors.from_dict(inventors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



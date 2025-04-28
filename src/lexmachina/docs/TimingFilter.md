# TimingFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_or_after** | **date** |  | [optional] 
**on_or_before** | **date** |  | [optional] 

## Example

```python
from lexmachina.models.timing_filter import TimingFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TimingFilter from a JSON string
timing_filter_instance = TimingFilter.from_json(json)
# print the JSON string representation of the object
print(TimingFilter.to_json())

# convert the object into a dict
timing_filter_dict = timing_filter_instance.to_dict()
# create an instance of TimingFilter from a dict
timing_filter_from_dict = TimingFilter.from_dict(timing_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



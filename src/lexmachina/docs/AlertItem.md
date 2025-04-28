# AlertItem

A single item resulting from an alert run.  The various caseId and caseUrl fields will only appear when an alert item is a part of metadata about a specific case.  For example an alert on a district case docket entry will include the districtCaseId and districtCaseUrl here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**item_id** | [**Itemid**](Itemid.md) |  | [optional] 
**district_case_id** | **int** |  | [optional] 
**appeals_case_id** | **int** |  | [optional] 
**state_case_id** | **int** |  | [optional] 
**bankruptcy_case_id** | **int** |  | [optional] 
**itc_investigation_number** | **str** |  | [optional] 
**ptab_trial_id** | **int** |  | [optional] 
**district_case_url** | **str** |  | [optional] 
**appeals_case_url** | **str** |  | [optional] 
**state_case_url** | **str** |  | [optional] 
**bankruptcy_case_url** | **str** |  | [optional] 
**itc_investigation_url** | **str** |  | [optional] 
**ptab_trial_url** | **str** |  | [optional] 

## Example

```python
from lexmachina.models.alert_item import AlertItem

# TODO update the JSON string below
json = "{}"
# create an instance of AlertItem from a JSON string
alert_item_instance = AlertItem.from_json(json)
# print the JSON string representation of the object
print(AlertItem.to_json())

# convert the object into a dict
alert_item_dict = alert_item_instance.to_dict()
# create an instance of AlertItem from a dict
alert_item_from_dict = AlertItem.from_dict(alert_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ComplaintSummary

Complaint Summaries appear on District Court case pages and briefly describe the contents of case-originating complaints.  This allows users to quickly review cases for relevant fact patterns. Summaries include specific complaint points such as the nature of the case, plaintiff and defendant information, alleged harm, and requested remedies.  In collaboration with Lexis+ AI and CourtLink, Lex Machina utilizes a sophisticated AI large language model (LLM) to review complaints and draft the summaries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** |  | 
**document_law_url** | **str** |  | 
**summarized** | **date** |  | 

## Example

```python
from lexmachina.models.complaint_summary import ComplaintSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ComplaintSummary from a JSON string
complaint_summary_instance = ComplaintSummary.from_json(json)
# print the JSON string representation of the object
print(ComplaintSummary.to_json())

# convert the object into a dict
complaint_summary_dict = complaint_summary_instance.to_dict()
# create an instance of ComplaintSummary from a dict
complaint_summary_from_dict = ComplaintSummary.from_dict(complaint_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



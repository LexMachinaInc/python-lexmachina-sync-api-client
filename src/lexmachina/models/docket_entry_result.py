# coding: utf-8

"""
    Lex Machina API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 20250318
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lexmachina.models.court_type import CourtType
from typing import Optional, Set
from typing_extensions import Self

class DocketEntryResult(BaseModel):
    """
    The caseId and caseUrl fields will only be populated for the case type of the docket entry.  For example only a district case docket entry will have a districtCaseId and districtCaseURL.
    """ # noqa: E501
    filed_on: date = Field(alias="filedOn")
    tags: List[StrictStr]
    text: StrictStr
    number: Optional[StrictInt]
    docket_entry_id: StrictInt = Field(alias="docketEntryId")
    court_type: CourtType = Field(alias="courtType")
    bankruptcy_case_id: Optional[StrictInt] = Field(default=None, alias="bankruptcyCaseId")
    appeals_case_id: Optional[StrictInt] = Field(default=None, alias="appealsCaseId")
    district_case_id: Optional[StrictInt] = Field(default=None, alias="districtCaseId")
    district_case_url: Optional[StrictStr] = Field(default=None, alias="districtCaseUrl")
    appeals_case_url: Optional[StrictStr] = Field(default=None, alias="appealsCaseUrl")
    bankruptcy_case_url: Optional[StrictStr] = Field(default=None, alias="bankruptcyCaseUrl")
    __properties: ClassVar[List[str]] = ["filedOn", "tags", "text", "number", "docketEntryId", "courtType", "bankruptcyCaseId", "appealsCaseId", "districtCaseId", "districtCaseUrl", "appealsCaseUrl", "bankruptcyCaseUrl"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DocketEntryResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if number (nullable) is None
        # and model_fields_set contains the field
        if self.number is None and "number" in self.model_fields_set:
            _dict['number'] = None

        # set to None if bankruptcy_case_id (nullable) is None
        # and model_fields_set contains the field
        if self.bankruptcy_case_id is None and "bankruptcy_case_id" in self.model_fields_set:
            _dict['bankruptcyCaseId'] = None

        # set to None if appeals_case_id (nullable) is None
        # and model_fields_set contains the field
        if self.appeals_case_id is None and "appeals_case_id" in self.model_fields_set:
            _dict['appealsCaseId'] = None

        # set to None if district_case_id (nullable) is None
        # and model_fields_set contains the field
        if self.district_case_id is None and "district_case_id" in self.model_fields_set:
            _dict['districtCaseId'] = None

        # set to None if district_case_url (nullable) is None
        # and model_fields_set contains the field
        if self.district_case_url is None and "district_case_url" in self.model_fields_set:
            _dict['districtCaseUrl'] = None

        # set to None if appeals_case_url (nullable) is None
        # and model_fields_set contains the field
        if self.appeals_case_url is None and "appeals_case_url" in self.model_fields_set:
            _dict['appealsCaseUrl'] = None

        # set to None if bankruptcy_case_url (nullable) is None
        # and model_fields_set contains the field
        if self.bankruptcy_case_url is None and "bankruptcy_case_url" in self.model_fields_set:
            _dict['bankruptcyCaseUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocketEntryResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filedOn": obj.get("filedOn"),
            "tags": obj.get("tags"),
            "text": obj.get("text"),
            "number": obj.get("number"),
            "docketEntryId": obj.get("docketEntryId"),
            "courtType": obj.get("courtType"),
            "bankruptcyCaseId": obj.get("bankruptcyCaseId"),
            "appealsCaseId": obj.get("appealsCaseId"),
            "districtCaseId": obj.get("districtCaseId"),
            "districtCaseUrl": obj.get("districtCaseUrl"),
            "appealsCaseUrl": obj.get("appealsCaseUrl"),
            "bankruptcyCaseUrl": obj.get("bankruptcyCaseUrl")
        })
        return _obj



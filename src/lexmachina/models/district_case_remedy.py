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
from typing import Optional, Set
from typing_extensions import Self

class DistrictCaseRemedy(BaseModel):
    """
    DistrictCaseRemedy
    """ # noqa: E501
    name: StrictStr
    type: StrictStr
    judgment_source: StrictStr = Field(alias="judgmentSource")
    awarded_to_party_ids: List[StrictInt] = Field(alias="awardedToPartyIds")
    against_party_ids: List[StrictInt] = Field(alias="againstPartyIds")
    docket_entry_filed: date = Field(alias="docketEntryFiled")
    negated: Optional[date] = None
    reinstated: Optional[date] = None
    __properties: ClassVar[List[str]] = ["name", "type", "judgmentSource", "awardedToPartyIds", "againstPartyIds", "docketEntryFiled", "negated", "reinstated"]

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
        """Create an instance of DistrictCaseRemedy from a JSON string"""
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
        # set to None if negated (nullable) is None
        # and model_fields_set contains the field
        if self.negated is None and "negated" in self.model_fields_set:
            _dict['negated'] = None

        # set to None if reinstated (nullable) is None
        # and model_fields_set contains the field
        if self.reinstated is None and "reinstated" in self.model_fields_set:
            _dict['reinstated'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DistrictCaseRemedy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "judgmentSource": obj.get("judgmentSource"),
            "awardedToPartyIds": obj.get("awardedToPartyIds"),
            "againstPartyIds": obj.get("againstPartyIds"),
            "docketEntryFiled": obj.get("docketEntryFiled"),
            "negated": obj.get("negated"),
            "reinstated": obj.get("reinstated")
        })
        return _obj



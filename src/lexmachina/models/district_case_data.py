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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from lexmachina.models.appeals_case import AppealsCase
from lexmachina.models.attorney import Attorney
from lexmachina.models.case_event import CaseEvent
from lexmachina.models.case_resolution import CaseResolution
from lexmachina.models.case_status import CaseStatus
from lexmachina.models.complaint_summary import ComplaintSummary
from lexmachina.models.district_case_damages_by_status import DistrictCaseDamagesByStatus
from lexmachina.models.district_case_dates import DistrictCaseDates
from lexmachina.models.district_case_findings_by_status import DistrictCaseFindingsByStatus
from lexmachina.models.district_case_remedies_by_status import DistrictCaseRemediesByStatus
from lexmachina.models.docket import Docket
from lexmachina.models.federal_judge import FederalJudge
from lexmachina.models.law_firm import LawFirm
from lexmachina.models.magistrate_judge import MagistrateJudge
from lexmachina.models.multi_district_litigation import MultiDistrictLitigation
from lexmachina.models.orders import Orders
from lexmachina.models.party import Party
from lexmachina.models.patent import Patent
from typing import Optional, Set
from typing_extensions import Self

class DistrictCaseData(BaseModel):
    """
    A single case from a federal district court case and relevant metadata.
    """ # noqa: E501
    district_case_id: StrictInt = Field(alias="districtCaseId")
    title: StrictStr
    court: StrictStr
    case_no: StrictStr = Field(alias="caseNo")
    status: CaseStatus
    case_type: List[StrictStr] = Field(alias="caseType")
    case_tags: List[StrictStr] = Field(alias="caseTags")
    dates: DistrictCaseDates
    resolution: Optional[CaseResolution] = None
    events: List[CaseEvent]
    judges: List[FederalJudge]
    magistrate_judges: List[MagistrateJudge] = Field(alias="magistrateJudges")
    remedies: DistrictCaseRemediesByStatus
    findings: DistrictCaseFindingsByStatus
    law_firms: List[LawFirm] = Field(alias="lawFirms")
    attorneys: List[Attorney]
    parties: List[Party]
    damages: DistrictCaseDamagesByStatus
    patents: List[Patent]
    orders: Orders
    mdl: MultiDistrictLitigation
    appeals_cases: List[AppealsCase] = Field(alias="appealsCases")
    docket: Docket
    complaint_summary: Optional[ComplaintSummary] = Field(alias="complaintSummary")
    __properties: ClassVar[List[str]] = ["districtCaseId", "title", "court", "caseNo", "status", "caseType", "caseTags", "dates", "resolution", "events", "judges", "magistrateJudges", "remedies", "findings", "lawFirms", "attorneys", "parties", "damages", "patents", "orders", "mdl", "appealsCases", "docket", "complaintSummary"]

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
        """Create an instance of DistrictCaseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dates
        if self.dates:
            _dict['dates'] = self.dates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resolution
        if self.resolution:
            _dict['resolution'] = self.resolution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item_events in self.events:
                if _item_events:
                    _items.append(_item_events.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in judges (list)
        _items = []
        if self.judges:
            for _item_judges in self.judges:
                if _item_judges:
                    _items.append(_item_judges.to_dict())
            _dict['judges'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in magistrate_judges (list)
        _items = []
        if self.magistrate_judges:
            for _item_magistrate_judges in self.magistrate_judges:
                if _item_magistrate_judges:
                    _items.append(_item_magistrate_judges.to_dict())
            _dict['magistrateJudges'] = _items
        # override the default output from pydantic by calling `to_dict()` of remedies
        if self.remedies:
            _dict['remedies'] = self.remedies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of findings
        if self.findings:
            _dict['findings'] = self.findings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in law_firms (list)
        _items = []
        if self.law_firms:
            for _item_law_firms in self.law_firms:
                if _item_law_firms:
                    _items.append(_item_law_firms.to_dict())
            _dict['lawFirms'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attorneys (list)
        _items = []
        if self.attorneys:
            for _item_attorneys in self.attorneys:
                if _item_attorneys:
                    _items.append(_item_attorneys.to_dict())
            _dict['attorneys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parties (list)
        _items = []
        if self.parties:
            for _item_parties in self.parties:
                if _item_parties:
                    _items.append(_item_parties.to_dict())
            _dict['parties'] = _items
        # override the default output from pydantic by calling `to_dict()` of damages
        if self.damages:
            _dict['damages'] = self.damages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in patents (list)
        _items = []
        if self.patents:
            for _item_patents in self.patents:
                if _item_patents:
                    _items.append(_item_patents.to_dict())
            _dict['patents'] = _items
        # override the default output from pydantic by calling `to_dict()` of orders
        if self.orders:
            _dict['orders'] = self.orders.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mdl
        if self.mdl:
            _dict['mdl'] = self.mdl.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in appeals_cases (list)
        _items = []
        if self.appeals_cases:
            for _item_appeals_cases in self.appeals_cases:
                if _item_appeals_cases:
                    _items.append(_item_appeals_cases.to_dict())
            _dict['appealsCases'] = _items
        # override the default output from pydantic by calling `to_dict()` of docket
        if self.docket:
            _dict['docket'] = self.docket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of complaint_summary
        if self.complaint_summary:
            _dict['complaintSummary'] = self.complaint_summary.to_dict()
        # set to None if resolution (nullable) is None
        # and model_fields_set contains the field
        if self.resolution is None and "resolution" in self.model_fields_set:
            _dict['resolution'] = None

        # set to None if complaint_summary (nullable) is None
        # and model_fields_set contains the field
        if self.complaint_summary is None and "complaint_summary" in self.model_fields_set:
            _dict['complaintSummary'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DistrictCaseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "districtCaseId": obj.get("districtCaseId"),
            "title": obj.get("title"),
            "court": obj.get("court"),
            "caseNo": obj.get("caseNo"),
            "status": obj.get("status"),
            "caseType": obj.get("caseType"),
            "caseTags": obj.get("caseTags"),
            "dates": DistrictCaseDates.from_dict(obj["dates"]) if obj.get("dates") is not None else None,
            "resolution": CaseResolution.from_dict(obj["resolution"]) if obj.get("resolution") is not None else None,
            "events": [CaseEvent.from_dict(_item) for _item in obj["events"]] if obj.get("events") is not None else None,
            "judges": [FederalJudge.from_dict(_item) for _item in obj["judges"]] if obj.get("judges") is not None else None,
            "magistrateJudges": [MagistrateJudge.from_dict(_item) for _item in obj["magistrateJudges"]] if obj.get("magistrateJudges") is not None else None,
            "remedies": DistrictCaseRemediesByStatus.from_dict(obj["remedies"]) if obj.get("remedies") is not None else None,
            "findings": DistrictCaseFindingsByStatus.from_dict(obj["findings"]) if obj.get("findings") is not None else None,
            "lawFirms": [LawFirm.from_dict(_item) for _item in obj["lawFirms"]] if obj.get("lawFirms") is not None else None,
            "attorneys": [Attorney.from_dict(_item) for _item in obj["attorneys"]] if obj.get("attorneys") is not None else None,
            "parties": [Party.from_dict(_item) for _item in obj["parties"]] if obj.get("parties") is not None else None,
            "damages": DistrictCaseDamagesByStatus.from_dict(obj["damages"]) if obj.get("damages") is not None else None,
            "patents": [Patent.from_dict(_item) for _item in obj["patents"]] if obj.get("patents") is not None else None,
            "orders": Orders.from_dict(obj["orders"]) if obj.get("orders") is not None else None,
            "mdl": MultiDistrictLitigation.from_dict(obj["mdl"]) if obj.get("mdl") is not None else None,
            "appealsCases": [AppealsCase.from_dict(_item) for _item in obj["appealsCases"]] if obj.get("appealsCases") is not None else None,
            "docket": Docket.from_dict(obj["docket"]) if obj.get("docket") is not None else None,
            "complaintSummary": ComplaintSummary.from_dict(obj["complaintSummary"]) if obj.get("complaintSummary") is not None else None
        })
        return _obj



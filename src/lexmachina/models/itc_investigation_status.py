# coding: utf-8

"""
    Lex Machina API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 20250318
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ITCInvestigationStatus(str, Enum):
    """
    ITCInvestigationStatus
    """

    """
    allowed enum values
    """
    ACTIVE = 'Active'
    TERMINATED = 'Terminated'
    COMPLETED = 'Completed'
    PENDING_BEFORE_THE_ALJ = 'Pending before the ALJ'
    PENDING_BEFORE_THE_COMMISSION = 'Pending before the Commission'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ITCInvestigationStatus from a JSON string"""
        return cls(json.loads(json_str))



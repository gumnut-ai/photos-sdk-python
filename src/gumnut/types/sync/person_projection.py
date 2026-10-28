# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from ..person_response import PersonResponse
from .person_projection_key import PersonProjectionKey

__all__ = ["PersonProjection"]


class PersonProjection(BaseModel):
    key: PersonProjectionKey
    """Stable key matching this projection value"""

    kind: Literal["person"]

    value: PersonResponse
    """Fully materialized current domain value"""

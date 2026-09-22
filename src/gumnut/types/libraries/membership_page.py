# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .membership_response import MembershipResponse

__all__ = ["MembershipPage"]


class MembershipPage(BaseModel):
    data: List[MembershipResponse]
    """Non-owner membership records in newest-first order."""

    has_more: bool
    """Whether another page exists.

    Pass the last item's ID as `starting_after_id` and repeat the same `state`
    filter.
    """

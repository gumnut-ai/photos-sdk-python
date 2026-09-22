# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.user_summary import UserSummary

__all__ = ["InvitationResponse"]


class InvitationResponse(BaseModel):
    id: str
    """Stable invitation identifier."""

    created_at: datetime
    """When this invitation was issued."""

    created_by: UserSummary
    """Account that created this invitation."""

    disabled_at: Optional[datetime] = None
    """When the owner disabled this invitation, or null."""

    expires_at: datetime
    """Exclusive expiration instant."""

    joiner_count: int
    """
    Number of accounts that have redeemed this invitation, including departed
    members.
    """

    library_id: str
    """ID of the target library."""

    max_joiners: int
    """Fixed maximum number of distinct redemptions."""

    remaining_places: int
    """Places remaining for new accounts; never negative."""

    role: Literal["viewer", "collaborator"]
    """Role offered to admitted members."""

    state: Literal["active", "exhausted", "expired", "disabled"]
    """
    Derived invitation state, with disablement taking precedence over expiration and
    exhaustion.
    """

    updated_at: datetime
    """When this invitation last changed."""

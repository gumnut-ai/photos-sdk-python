# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.user_summary import UserSummary

__all__ = ["MembershipResponse"]


class MembershipResponse(BaseModel):
    id: str
    """Stable membership record identifier."""

    created_at: datetime
    """When this record was created."""

    ended_at: Optional[datetime] = None
    """Most recent departure or removal instant, or null while active."""

    joined_at: datetime
    """Most recent admission instant."""

    last_removed_at: Optional[datetime] = None
    """Retained owner-removal cutoff for readmission, or null."""

    library_id: str
    """Library this membership belongs to."""

    role: Literal["viewer", "collaborator"]
    """Current or last assigned role."""

    state: Literal["active", "left", "removed"]
    """A member's library access state.

    active grants the assigned role. left means the member departed; removed means
    the owner revoked access. left and removed grant no access.
    """

    updated_at: datetime
    """When this record last changed."""

    user: UserSummary
    """Member account summary."""

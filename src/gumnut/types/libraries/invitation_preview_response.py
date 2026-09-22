# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.user_summary import UserSummary

__all__ = ["InvitationPreviewResponse", "Library"]


class Library(BaseModel):
    """Library attribution without content or storage details."""

    id: str
    """Library identifier."""

    name: str
    """Library name."""

    owner: UserSummary
    """Owning account summary."""


class InvitationPreviewResponse(BaseModel):
    current_role: Optional[Literal["owner", "viewer", "collaborator"]] = None
    """Existing active role, or null when the account has no current access."""

    eligibility: Literal["joinable", "already_member", "expired", "disabled", "exhausted", "new_invitation_required"]
    """Current eligibility; preview does not reserve a place."""

    expires_at: datetime
    """Invitation expiration instant."""

    invitation_id: str
    """Previewed invitation identifier."""

    library: Library
    """Library attribution without content or storage details."""

    offered_role: Literal["viewer", "collaborator"]
    """Role offered if this account joins."""

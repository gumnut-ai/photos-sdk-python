# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["InvitationListParams"]


class InvitationListParams(TypedDict, total=False):
    library_id: Optional[str]
    """
    Optional owner-library filter; omit to list invitations across all libraries you
    own.
    """

    limit: int
    """Maximum records per page."""

    starting_after_id: Optional[str]
    """Continue after this invitation ID from the previous page."""

    state: Literal["active", "exhausted", "expired", "disabled", "all"]
    """Return only invitations in this state, or all states."""

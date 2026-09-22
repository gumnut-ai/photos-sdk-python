# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    limit: int
    """Maximum records per page."""

    starting_after_id: Optional[str]
    """Continue after this membership ID from the previous page."""

    state: Literal["active", "left", "removed", "all"]
    """Return only memberships in this state, or all states."""

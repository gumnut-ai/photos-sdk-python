# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemberUpdateParams"]


class MemberUpdateParams(TypedDict, total=False):
    library_id: Required[str]
    """Library identifier."""

    role: Required[Literal["viewer", "collaborator"]]
    """New role for an active member."""

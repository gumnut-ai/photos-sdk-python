# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvitationCreateParams"]


class InvitationCreateParams(TypedDict, total=False):
    expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Absolute expiration instant with a timezone offset; must be in the future."""

    library_id: Required[str]
    """ID of the single library this invitation targets."""

    max_joiners: Required[int]
    """Maximum number of distinct accounts that can redeem this invitation."""

    role: Required[Literal["viewer", "collaborator"]]
    """Role offered to admitted members."""

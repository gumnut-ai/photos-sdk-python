# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["StackListStacksParams"]


class StackListStacksParams(TypedDict, total=False):
    ids: Optional[SequenceNotStr[str]]
    """Look up specific stacks by ID (max 200; each ID has the `asset_stack_` prefix).

    Accepts multiple `ids=` query params or a single comma-delimited value (e.g.,
    `ids=asset_stack_1,asset_stack_2`).
    """

    library_id: Optional[str]
    """Library to list stacks from.

    Optional if the user has a single library; required when they have multiple. Use
    `list_libraries` to enumerate.
    """

    limit: int
    """Maximum number of stacks to return per page (1–200). Defaults to 20."""

    origin: Optional[Literal["auto_burst", "user"]]
    """Return only stacks with this provenance."""

    primary_asset_id: Optional[str]
    """Return only the stack that pins this asset (with `asset_` prefix) as its cover."""

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last stack in the previous response's `data` to fetch the
    next page. Omit for the first page.
    """

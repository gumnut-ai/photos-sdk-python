# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["BodyListParams"]


class BodyListParams(TypedDict, total=False):
    asset_id: Optional[str]
    """Return only bodies in this asset."""

    ids: Optional[SequenceNotStr[str]]
    """Look up specific bodies by ID (max 200).

    IDs use the `body_` prefix. Accepts multiple `ids=` query params or a single
    comma-delimited value (e.g., `ids=body_1,body_2`).
    """

    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported value: `candidates` (adds each body's `candidates`, the named people
    who may be the person in it). Accepts multiple `include=` query params or a
    single comma-delimited value. Unknown values return 422.
    """

    library_id: Optional[str]
    """Library to list from.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

    limit: int
    """Maximum number of bodies per page (1–200). Defaults to 20."""

    person_id: Optional[str]
    """Return only bodies linked to this person."""

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last body in the previous response's `data` to fetch the
    next page. Omit for the first page.
    """

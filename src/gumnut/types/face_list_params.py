# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["FaceListParams"]


class FaceListParams(TypedDict, total=False):
    asset_id: Optional[str]
    """Return only faces detected in this asset.

    Useful for 'show me all the faces in this photo'.
    """

    ids: Optional[SequenceNotStr[str]]
    """Look up specific faces by ID (max 100). IDs use the `face_` prefix."""

    library_id: Optional[str]
    """Library to list from.

    Optional if the user has a single library; required when they have multiple.
    """

    limit: int
    """Maximum number of faces per page (1–200). Defaults to 20."""

    person_id: Optional[str]
    """Return only faces currently assigned to this person.

    Useful for reviewing or curating a person's face cluster.
    """

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last face in the previous response's `data` to fetch the
    next page. Omit for the first page.
    """

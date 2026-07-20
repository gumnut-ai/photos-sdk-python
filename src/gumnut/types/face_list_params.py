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
    """Look up specific faces by ID (max 200).

    IDs use the `face_` prefix. Accepts multiple `ids=` query params or a single
    comma-delimited value (e.g., `ids=face_1,face_2`).
    """

    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported values: `cluster_assignment` (adds the nested `cluster_assignment`
    object — `distance_to_person` and a top-K `candidates` list of nearby Persons).
    Accepts multiple `include=` query params or a single comma-delimited value
    (e.g., `include=cluster_assignment`).
    """

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

# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["FaceRetrieveParams"]


class FaceRetrieveParams(TypedDict, total=False):
    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported values: `cluster_assignment` (adds the nested `cluster_assignment`
    object). Accepts multiple `include=` query params or a single comma-delimited
    value.
    """

    library_id: Optional[str]
    """Library the face belongs to.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

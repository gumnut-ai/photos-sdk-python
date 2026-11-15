# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["BodyRetrieveParams"]


class BodyRetrieveParams(TypedDict, total=False):
    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported value: `candidates` (adds each body's `candidates`, the named people
    who may be the person in it). Accepts multiple `include=` query params or a
    single comma-delimited value. Unknown values return 422.
    """

    library_id: Optional[str]
    """Library the body belongs to.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

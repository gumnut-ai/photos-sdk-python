# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PersonRetrieveParams"]


class PersonRetrieveParams(TypedDict, total=False):
    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported values: `cluster_metrics` (adds the nested `cluster_metrics` object
    when the person has a populated centroid). Accepts multiple `include=` query
    params or a single comma-delimited value.
    """

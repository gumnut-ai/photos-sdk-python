# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PersonListParams"]


class PersonListParams(TypedDict, total=False):
    album_id: Optional[str]
    """Include only people associated with this album ID"""

    asset_id: Optional[str]
    """Include only people associated with this asset ID"""

    has_name: Optional[bool]
    """
    Filter by whether the person has a name assigned (true = named only, false =
    unnamed only)
    """

    ids: Optional[SequenceNotStr[str]]
    """Filter by specific person IDs (max 100)"""

    library_id: Optional[str]
    """Library ID (required if user has multiple libraries)"""

    limit: int
    """Max number of people to return (1-200)"""

    name: Optional[str]
    """Filter by name using case-insensitive substring matching"""

    starting_after_id: Optional[str]
    """Person ID to start listing people after"""

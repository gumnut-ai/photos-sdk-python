# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    album_id: Optional[str]
    """Filter by assets in a specific album"""

    ids: Optional[SequenceNotStr[str]]
    """Filter by specific asset IDs (max 100)"""

    library_id: Optional[str]
    """Library to list assets from (optional)"""

    limit: int

    person_id: Optional[str]
    """Filter by assets associated with a specific person ID"""

    starting_after_id: Optional[str]
    """Asset ID to start listing assets after"""

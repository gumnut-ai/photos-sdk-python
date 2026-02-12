# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AlbumAssetListParams"]


class AlbumAssetListParams(TypedDict, total=False):
    album_id: Optional[str]
    """Filter by album ID"""

    asset_id: Optional[str]
    """Filter by asset ID"""

    ids: Optional[SequenceNotStr[str]]
    """Filter by specific album-asset IDs (max 100)"""

    library_id: Optional[str]
    """Library ID (required if user has multiple libraries)"""

    limit: int
    """Max number of results to return"""

    starting_after_id: Optional[str]
    """Album-asset ID to start listing after"""

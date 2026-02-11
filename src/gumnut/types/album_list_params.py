# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AlbumListParams"]


class AlbumListParams(TypedDict, total=False):
    asset_id: Optional[str]
    """Filter albums containing this asset ID (optional)"""

    ids: Optional[SequenceNotStr[str]]
    """Filter by specific album IDs (max 100)"""

    library_id: Optional[str]
    """Library to list albums from (optional)"""

    limit: int
    """Max number of albums to return"""

    starting_after_id: Optional[str]
    """Album ID to start listing albums after"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AlbumListParams"]


class AlbumListParams(TypedDict, total=False):
    asset_id: Optional[str]
    """Return only albums that contain this asset.

    Useful for answering 'which albums is this photo in?' without calling
    `list_album_assets`.
    """

    ids: Optional[SequenceNotStr[str]]
    """Look up specific albums by ID (max 100; each ID has the `album_` prefix).

    Use for bulk fetch when IDs are already known.
    """

    library_id: Optional[str]
    """Library to list albums from.

    Optional if the user has a single library; required when they have multiple. Use
    `list_libraries` to enumerate.
    """

    limit: int
    """Maximum number of albums to return per page (1–200). Defaults to 20."""

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last album in the previous response's `data` to fetch the
    next page. Omit for the first page.
    """

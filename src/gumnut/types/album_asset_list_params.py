# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AlbumAssetListParams"]


class AlbumAssetListParams(TypedDict, total=False):
    album_id: Optional[str]
    """Return only link records for this album ID.

    Equivalent to 'list the assets in this album' — in most cases prefer
    `list_assets` with `album_id` to get the asset metadata directly instead of the
    lightweight link records.
    """

    asset_id: Optional[str]
    """Return only link records for this asset ID.

    Equivalent to 'which albums contain this asset' — in most cases prefer
    `list_albums` with `asset_id` to get the album metadata directly.
    """

    ids: Optional[SequenceNotStr[str]]
    """Look up specific album-asset link records by ID (max 100).

    The ID has the `album_asset_` prefix.
    """

    library_id: Optional[str]
    """Library to list from.

    Optional if the user has a single library; required when they have multiple.
    """

    limit: int
    """Maximum number of link records per page (1–200). Defaults to 20."""

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last album-asset in the previous response's `data` to fetch
    the next page. Omit for the first page.
    """

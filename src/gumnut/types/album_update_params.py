# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AlbumUpdateParams"]


class AlbumUpdateParams(TypedDict, total=False):
    album_cover_asset_id: Optional[str]
    """Asset ID (with `asset_` prefix) to use as the album cover.

    Must be a live asset already in the album — get IDs from `list_album_assets`.
    Pass `null` to clear the explicit cover. Omit to leave unchanged.
    """

    description: Optional[str]
    """New free-form description for the album. Omit to leave unchanged."""

    name: Optional[str]
    """New display name for the album. Omit to leave unchanged."""

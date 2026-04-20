# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AlbumCreateParams"]


class AlbumCreateParams(TypedDict, total=False):
    description: Optional[str]
    """Optional free-form description shown alongside the album name."""

    library_id: Optional[str]
    """Library to create the album in.

    Optional if the user has a single library; required when they have multiple. Use
    `list_libraries` to enumerate.
    """

    name: Optional[str]
    """Display name for the new album.

    Optional; callers that need to name an album can set it here or via
    `update_album` after creation.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlbumAssetProjectionKeyParam"]


class AlbumAssetProjectionKeyParam(TypedDict, total=False):
    album_id: Required[str]
    """Album identifier in the bound library"""

    asset_id: Required[str]
    """Asset identifier in the bound library"""

    kind: Required[Literal["album_asset"]]

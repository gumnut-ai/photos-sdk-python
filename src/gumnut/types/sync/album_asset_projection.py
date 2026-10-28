# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from ..album_asset_response import AlbumAssetResponse
from .album_asset_projection_key import AlbumAssetProjectionKey

__all__ = ["AlbumAssetProjection"]


class AlbumAssetProjection(BaseModel):
    key: AlbumAssetProjectionKey
    """Stable album and asset pair key"""

    kind: Literal["album_asset"]

    value: AlbumAssetResponse
    """Fully materialized current domain value"""

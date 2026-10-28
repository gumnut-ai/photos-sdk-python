# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AlbumAssetProjectionKey"]


class AlbumAssetProjectionKey(BaseModel):
    album_id: str
    """Album identifier in the bound library"""

    asset_id: str
    """Asset identifier in the bound library"""

    kind: Literal["album_asset"]

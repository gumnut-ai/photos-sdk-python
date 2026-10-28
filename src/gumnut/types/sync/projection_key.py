# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .entity_projection_key import EntityProjectionKey
from .album_asset_projection_key import AlbumAssetProjectionKey

__all__ = ["ProjectionKey"]

ProjectionKey: TypeAlias = Union[EntityProjectionKey, AlbumAssetProjectionKey]

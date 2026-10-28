# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .entity_projection_key_param import EntityProjectionKeyParam
from .album_asset_projection_key_param import AlbumAssetProjectionKeyParam

__all__ = ["ProjectionKeyParam"]

ProjectionKeyParam: TypeAlias = Union[EntityProjectionKeyParam, AlbumAssetProjectionKeyParam]

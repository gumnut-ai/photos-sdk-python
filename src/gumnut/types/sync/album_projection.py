# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from ..album_response import AlbumResponse
from .album_projection_key import AlbumProjectionKey

__all__ = ["AlbumProjection"]


class AlbumProjection(BaseModel):
    key: AlbumProjectionKey
    """Stable key matching this projection value"""

    kind: Literal["album"]

    value: AlbumResponse
    """Fully materialized current domain value"""

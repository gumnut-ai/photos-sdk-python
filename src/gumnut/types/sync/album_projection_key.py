# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AlbumProjectionKey"]


class AlbumProjectionKey(BaseModel):
    id: str
    """Stable entity identifier; current_user must name the authenticated principal"""

    kind: Literal["album"]

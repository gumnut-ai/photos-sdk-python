# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EntityProjectionKey"]


class EntityProjectionKey(BaseModel):
    id: str
    """Stable entity identifier; current_user must name the authenticated principal"""

    kind: Literal["current_user", "asset", "person", "face", "stack", "album"]

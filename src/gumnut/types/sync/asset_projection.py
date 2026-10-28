# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from ..asset_response import AssetResponse
from .asset_projection_key import AssetProjectionKey

__all__ = ["AssetProjection"]


class AssetProjection(BaseModel):
    key: AssetProjectionKey
    """Stable key matching this projection value"""

    kind: Literal["asset"]

    value: AssetResponse
    """Fully materialized current domain value"""

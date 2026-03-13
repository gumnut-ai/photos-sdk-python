# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .asset_response import AssetResponse

__all__ = ["SearchResultItem"]


class SearchResultItem(BaseModel):
    asset: AssetResponse
    """Represents a photo or video asset with metadata and access URLs."""

    distance: Optional[float] = None

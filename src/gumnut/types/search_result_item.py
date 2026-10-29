# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .asset_response import AssetResponse

__all__ = ["SearchResultItem"]


class SearchResultItem(BaseModel):
    asset: AssetResponse
    """The matching asset."""

    distance: Optional[float] = None
    """
    Similarity distance between the asset's visual content and the search text or
    image (lower is closer), for attribution only; don't rely on it for result
    order. Null when the asset matched without a visual match, such as through
    metadata text only.
    """

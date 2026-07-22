# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .asset_response import AssetResponse

__all__ = ["SearchResultItem"]


class SearchResultItem(BaseModel):
    asset: AssetResponse
    """The matching asset."""

    distance: Optional[float] = None
    """Best available dense-stage cosine distance (lower is more similar).

    This is attribution only: results are ordered by fused rank, not distance. Null
    for sparse-only and structured-filter-only matches.
    """

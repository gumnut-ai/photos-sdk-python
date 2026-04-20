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
    Semantic distance from `query` (0.0 = identical, 1.0 = unrelated); lower is more
    similar — inverted from the usual 'similarity score' convention. Null when no
    semantic `query` was provided (structured-filter-only search).
    """

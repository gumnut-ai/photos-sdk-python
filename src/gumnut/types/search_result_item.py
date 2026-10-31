# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .asset_response import AssetResponse

__all__ = ["SearchResultItem"]


class SearchResultItem(BaseModel):
    asset: AssetResponse
    """The matching asset."""

    distance: Optional[float] = None
    """Deprecated.

    Use `match_strength` to judge how closely a text search result matches.
    Similarity distance between the asset's visual content and the search text or
    image (lower is closer), for attribution only; don't rely on it for result
    order. Null when the asset matched without a visual match, such as through
    metadata text only.
    """

    match_strength: Optional[Literal["best", "possible"]] = None
    """How closely the asset matches the search text.

    `best` results are strong matches and come first; `possible` results follow and
    are often unrelated. Null when this search did not judge the result, such as an
    image search.
    """

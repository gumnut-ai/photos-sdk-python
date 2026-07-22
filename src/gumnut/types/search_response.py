# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .search_result_item import SearchResultItem

__all__ = ["SearchResponse", "Debug", "DebugDenseImage", "DebugDenseText", "DebugFused", "DebugSparse"]


class DebugDenseImage(BaseModel):
    asset_id: str

    distance: float

    rank: int


class DebugDenseText(BaseModel):
    asset_id: str

    distance: float

    rank: int


class DebugFused(BaseModel):
    asset_id: str

    rank: int

    score: float

    dense_image_rank: Optional[int] = None

    dense_text_rank: Optional[int] = None

    sparse_rank: Optional[int] = None


class DebugSparse(BaseModel):
    asset_id: str

    matched_categories: List[str]

    rank: int

    score: float


class Debug(BaseModel):
    """Opt-in per-stage ranks and scores for evaluation attribution."""

    dense_image: List[DebugDenseImage]

    dense_text: List[DebugDenseText]

    fused: List[DebugFused]

    sparse: List[DebugSparse]


class SearchResponse(BaseModel):
    data: List[SearchResultItem]
    """
    For text or image search, matching assets are ordered by Reciprocal Rank Fusion
    across the available dense and sparse stages. Structured-filter-only searches
    retain newest-first capture-date ordering.
    """

    debug: Optional[Debug] = None
    """Opt-in per-stage ranks and scores for evaluation attribution."""

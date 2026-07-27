# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .search_result_item import SearchResultItem

__all__ = [
    "SearchResponse",
    "Debug",
    "DebugDenseImage",
    "DebugDenseText",
    "DebugFused",
    "DebugReranked",
    "DebugReranker",
    "DebugSparse",
]


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


class DebugReranked(BaseModel):
    asset_id: str

    fused_rank: int

    rank: int

    score: Optional[float] = None


class DebugReranker(BaseModel):
    attempted: bool

    duration_ms: float

    fallback_reason: Optional[str] = None

    api_model_revision: str = FieldInfo(alias="model_revision")

    outcome: str


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

    reranked: List[DebugReranked]

    reranker: DebugReranker

    selected_ordering: str

    sparse: List[DebugSparse]


class SearchResponse(BaseModel):
    data: List[SearchResultItem]
    """
    Text-query matches use the configured reranker over the first 50 Reciprocal Rank
    Fusion candidates, with fail-open RRF ordering. Image-only matches use RRF
    across available stages. Structured-filter-only searches retain newest-first
    capture-date ordering.
    """

    debug: Optional[Debug] = None
    """Opt-in per-stage ranks and scores for evaluation attribution."""

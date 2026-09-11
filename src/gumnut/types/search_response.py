# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .search_result_item import SearchResultItem

__all__ = ["SearchResponse"]


class SearchResponse(BaseModel):
    data: List[SearchResultItem]
    """
    Text-query matches use the configured reranker over the first 50 Reciprocal Rank
    Fusion candidates, with fail-open RRF ordering. Image-only matches use RRF
    across available stages. Structured-filter-only searches retain newest-first
    capture-date ordering.
    """

    has_more: bool
    """Whether another page remains in this search's result population.

    For content searches, this refers to the bounded ranked candidate population,
    not every potentially matching asset in the library. While true, increment
    `page` and repeat the same search criteria, filters, and `limit`.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .search_result_item import SearchResultItem

__all__ = ["SearchResponse"]


class SearchResponse(BaseModel):
    data: List[SearchResultItem]
    """
    Matching assets ordered by semantic distance (closest first) when `query` is
    set.
    """

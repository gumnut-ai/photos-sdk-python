# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .search_result_item import SearchResultItem

__all__ = ["SearchResponse"]


class SearchResponse(BaseModel):
    data: List[SearchResultItem]
    """Matching assets for this page.

    Content searches are ordered by relevance; structured-filter-only searches are
    ordered newest-first by capture date. A text `query` search can return fewer
    than `limit` results, or none. When the first page of a text `query` search is
    empty, nothing within the given filters closely matches that wording: rephrase
    or broaden the `query`, or change the filters, rather than requesting another
    page.
    """

    has_more: bool
    """Whether another page of results remains for this search.

    For a content search, false means this search has no more results to return, not
    that every matching asset in the library was returned. This can be false after a
    short or empty page. While true, increment `page` and repeat the same search
    criteria, filters, and `limit`.
    """

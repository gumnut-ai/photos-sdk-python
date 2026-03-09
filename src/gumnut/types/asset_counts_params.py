# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetCountsParams"]


class AssetCountsParams(TypedDict, total=False):
    album_id: Optional[str]
    """Filter by assets in a specific album"""

    group_by: str
    """Time period to group counts by. Currently only 'month' is supported."""

    library_id: Optional[str]
    """Library to count assets in (optional)"""

    limit: int
    """Maximum number of time buckets to return"""

    local_datetime_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets with local_datetime after this value (ISO 8601).

    Naive values compare directly against local_datetime; timezone-aware values are
    converted to UTC and compared against local_datetime adjusted by its stored
    offset.
    """

    local_datetime_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets with local_datetime before this value (ISO 8601).

    Naive values compare directly against local_datetime; timezone-aware values are
    converted to UTC and compared against local_datetime adjusted by its stored
    offset. Use the last time_bucket from a previous response to paginate.
    """

    person_id: Optional[str]
    """Filter by assets associated with a specific person ID"""

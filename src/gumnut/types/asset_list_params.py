# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    album_id: Optional[str]
    """Filter by assets in a specific album"""

    ids: Optional[SequenceNotStr[str]]
    """Filter by specific asset IDs (max 100)"""

    library_id: Optional[str]
    """Library to list assets from (optional)"""

    limit: int

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
    offset.
    """

    person_id: Optional[str]
    """Filter by assets associated with a specific person ID"""

    starting_after_id: Optional[str]
    """Asset ID to start listing assets after"""

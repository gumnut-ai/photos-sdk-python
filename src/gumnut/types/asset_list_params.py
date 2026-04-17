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
    """Max number of assets to return (1-200)"""

    local_datetime_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets with local_datetime after this value (ISO 8601).

    Naive values compare directly against local_datetime. Timezone-aware values:
    assets with a known offset are compared in UTC (local_datetime - offset); assets
    without an offset fall back to wall-clock comparison against local_datetime.
    """

    local_datetime_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets with local_datetime before this value (ISO 8601).

    Naive values compare directly against local_datetime. Timezone-aware values:
    assets with a known offset are compared in UTC (local_datetime - offset); assets
    without an offset fall back to wall-clock comparison against local_datetime.
    """

    person_id: Optional[str]
    """Filter by assets associated with a specific person ID"""

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last asset from the previous page to get the next page.
    """

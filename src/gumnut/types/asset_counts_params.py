# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetCountsParams"]


class AssetCountsParams(TypedDict, total=False):
    album_id: Optional[str]
    """Return only assets in this album — the album's `album_` ID, not its name."""

    group_by: Literal["month"]
    """Time period to group counts by.

    Only `month` is supported; other values return 422.
    """

    library_id: Optional[str]
    """Library to count assets in (optional)"""

    limit: int
    """Maximum number of time buckets to return (1-200)"""

    local_datetime_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly after this instant (ISO 8601; exclusive).

    Convert a relative or natural-language date phrase ('in 2023') into an explicit
    bound before sending. `local_datetime` is the photo's wall-clock time in the
    device's own timezone. Naive values compare directly against `local_datetime`.
    Timezone-aware values: assets with a known offset are compared in UTC
    (`local_datetime - offset`); assets without an offset fall back to wall-clock
    comparison against `local_datetime`.
    """

    local_datetime_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly before this instant (ISO 8601; exclusive).

    Same conversion requirement and awareness/offset semantics as
    `local_datetime_after`.
    """

    person_id: Optional[str]
    """Filter by assets associated with a specific person ID"""

    state: Literal["live", "trashed", "all"]
    """
    Which set of assets to count: `live` (default — excludes trashed assets),
    `trashed` (only trashed assets), or `all` (both live and trashed).
    """

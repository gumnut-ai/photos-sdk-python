# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AssetCountsParams"]


class AssetCountsParams(TypedDict, total=False):
    album_filter: Literal["all", "in_album", "not_in_album"]
    """
    Filter by album membership in general, rather than by membership of one specific
    album. This filter is independent of `album_id`, but combining `not_in_album`
    with `album_id` is contradictory and returns 422. Defaults to `all`.
    """

    album_id: Optional[str]
    """Return only assets in this album — the album's `album_` ID, not its name."""

    group_by: Literal["month"]
    """Time period to group counts by.

    Only `month` is supported; other values return 422.
    """

    library_id: Optional[str]
    """Library to count assets in.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

    limit: int
    """Maximum number of time buckets to return per page (1–200). Defaults to 20."""

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

    media_type: Optional[Literal["image", "video"]]
    """Filter to one media class (`image` or `video`).

    Omit to include both images and videos.
    """

    person_id: Optional[str]
    """Deprecated compatibility alias for one `person_ids` value.

    Do not combine it with `person_ids`.
    """

    person_ids: Optional[SequenceNotStr[str]]
    """
    Filter to assets containing faces belonging to ALL of these people
    (intersection, not union). Accepts up to 200 IDs across repeated `person_ids=`
    query params or comma-delimited values. Person IDs are carried by the entries of
    an asset's `people` field (returned with `include=people`).
    """

    state: Literal["live", "trashed", "all"]
    """
    Which set of assets to count: `live` (default — excludes trashed assets),
    `trashed` (only trashed assets), or `all` (both live and trashed).
    """

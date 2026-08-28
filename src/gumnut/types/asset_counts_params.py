# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
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

    group_by: Literal["day", "week", "month", "year"]
    """Calendar period to use for each count bucket."""

    library_id: Optional[str]
    """Library to count assets in.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

    limit: int
    """Maximum number of time buckets to return per page (1–200). Defaults to 20."""

    local_datetime_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Only include assets captured strictly after this local wall-clock datetime (ISO
    8601; exclusive). Asset counts accept timezone-naive values only; a `Z` suffix
    or timezone offset returns 422. Repeat this bound unchanged on every pagination
    page.
    """

    local_datetime_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Only include assets captured strictly before this local wall-clock datetime (ISO
    8601; exclusive). Asset counts accept timezone-naive values only; a `Z` suffix
    or timezone offset returns 422. Repeat this bound unchanged on every pagination
    page.
    """

    media_type: Optional[Literal["image", "video"]]
    """Filter to one media class (`image` or `video`).

    Omit to include both images and videos.
    """

    order: Literal["asc", "desc"]
    """
    Sort direction for capture-date buckets: `desc` returns newest buckets first;
    `asc` returns oldest buckets first.
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

    ratings: Optional[Iterable[int]]
    """Return assets whose effective rating is one of these exact values.

    Values must be integers from `0` through `5`; `5` is a favorite. `0` matches
    every unrated form: an explicit zero, a null or legacy out-of-range effective
    rating, or an asset with no metadata. Accepts repeated `ratings=` parameters or
    one comma-delimited value. Omit the parameter for no rating filter.
    """

    starting_after_bucket: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Cursor for time-bucket pagination.

    Pass the last returned `time_bucket` unchanged; buckets after it in the
    requested `order` are returned. Omit for the first page.
    """

    state: Literal["live", "trashed", "all"]
    """
    Which set of assets to count: `live` (default — excludes trashed assets),
    `trashed` (only trashed assets), or `all` (both live and trashed).
    """

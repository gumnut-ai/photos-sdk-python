# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import FileTypes, SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SearchSearchAssetsParams"]


class SearchSearchAssetsParams(TypedDict, total=False):
    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported values: `metadata` (camera/EXIF/GPS and location names), `faces`,
    `people`, `metrics` (ML quality scores), `file_data` (a group token populating
    the nested `file_data` object with the file/provenance scalars
    `device_asset_id`, `device_id`, `file_created_at`, `file_modified_at`,
    `checksum`, `checksum_sha1`, `file_size_bytes`), and `variants` (the
    non-thumbnail `asset_urls` size variants; without it `asset_urls` carries only
    its lean rung — `thumbnail`, or `thumbnail_image` for a video with an extracted
    still, or `original` for a still-less video — so callers that render
    non-thumbnail variants must pass it). Accepts multiple `include=` query params
    or a single comma-delimited value (e.g. `include=faces,people`). Unknown values
    return 422. When omitted, only the lean core is returned (`id`, `mime_type`,
    `local_datetime`, dimensions, `description`, `thumbhash`, `asset_urls`) and each
    data field above is null/absent until you request it.
    """

    album_ids: Optional[SequenceNotStr[str]]
    """Filter to assets in ALL of these album IDs (intersection, not union).

    Accepts multiple `album_ids=` form fields or a single comma-delimited value
    (e.g., `album_123,album_abc`). Get album IDs from `list_albums`. Plural on this
    tool; the sibling `list_assets` uses `album_id` (singular).
    """

    captured_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter to only include assets captured after this date (ISO format)."""

    captured_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter to only include assets captured before this date (ISO format)."""

    center: Optional[str]
    """
    Center point of a radius location filter: two comma-separated decimal-degree
    numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.
    """

    image: Optional[FileTypes]
    """Image file for an independent dense-image retrieval stage.

    When text is also provided, the stage ranks are fused rather than blending their
    embeddings.
    """

    include_debug: bool
    """Include per-stage dense/sparse ranks and scores plus fused attribution.

    Intended for debugging and evaluation; omitted from normal responses.
    """

    library_id: Optional[str]
    """Library to search assets from (optional)"""

    limit: int
    """Number of results per page (1-200)"""

    page: int
    """Page number"""

    person_ids: Optional[SequenceNotStr[str]]
    """Filter to assets containing ALL of these person IDs (intersection, not union).

    Accepts multiple `person_ids=` form fields or a single comma-delimited value
    (e.g., `person_123,person_abc`). Get person IDs from `list_people`.
    """

    query: Optional[str]
    """The text query to search for.

    If you want to search for a specific person or set of people, use the person_ids
    parameter instead.If you want to search for a photos taken during a specific
    date range, use the captured_before and captured_after parameters instead.
    """

    radius: Optional[float]
    """
    Radius of the `center` location filter, in meters (greater than 0, at most
    50,000).
    """

    threshold: float
    """Deprecated compatibility parameter.

    Accepted and validated but ignored because rank-fused results have no meaningful
    cosine-distance cutoff.
    """

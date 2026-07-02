# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    album_id: Optional[str]
    """Return only assets that are in the album with this ID.

    Equivalent to calling `list_album_assets` with `album_id` and then fetching each
    asset — prefer this param when you need the full asset metadata in one call.
    """

    bbox: Optional[str]
    """
    Bounding-box (map viewport) location filter: four comma-separated decimal-degree
    numbers `min_longitude,min_latitude,max_longitude,max_latitude`
    (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. Mutually exclusive with
    `center`/`radius`. A box whose `min_longitude` exceeds `max_longitude`
    (antimeridian-crossing) is accepted but matches nothing — split it client-side.
    """

    center: Optional[str]
    """
    Center point of a radius location filter: two comma-separated decimal-degree
    numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.
    Mutually exclusive with `bbox`.
    """

    ids: Optional[SequenceNotStr[str]]
    """Look up specific assets by ID (max 100; each ID has the `asset_` prefix).

    Accepts multiple `ids=` query params or a single comma-delimited value (e.g.,
    `ids=asset_1,asset_2`). Combines with other filters (album_id, person_id,
    datetime range) using AND logic — the result is the intersection.
    """

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

    library_id: Optional[str]
    """Library to list assets from.

    Optional if the user has a single library; required when they have multiple. Use
    `list_libraries` to enumerate available libraries.
    """

    limit: int
    """Maximum number of assets to return per page (1–200). Defaults to 20."""

    local_datetime_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly after this instant (ISO 8601; exclusive).

    `local_datetime` is the photo's wall-clock time in the device's own timezone.
    Naive values compare directly against `local_datetime`. Timezone-aware values:
    assets with a known offset are compared in UTC (`local_datetime - offset`);
    assets without an offset fall back to wall-clock comparison against
    `local_datetime`. Equivalent in purpose to `captured_after` on `search_assets`
    (naming inconsistency is tracked as a follow-up).
    """

    local_datetime_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly before this instant (ISO 8601; exclusive).

    Same awareness/offset semantics as `local_datetime_after`. Equivalent in purpose
    to `captured_before` on `search_assets` (naming inconsistency is tracked as a
    follow-up).
    """

    person_id: Optional[str]
    """Return only assets containing a face belonging to this person.

    Singular on this tool; the sibling `search_assets` uses `person_ids` (plural,
    ALL-of).
    """

    radius: Optional[float]
    """
    Radius of the `center` location filter, in meters (greater than 0, at most
    50000).
    """

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last asset in the previous response's `data` to fetch the
    next page. Omit for the first page. `list_assets` uses cursor pagination; the
    sibling `search_assets` uses 1-indexed `page` numbers (naming inconsistency is
    tracked as a follow-up).
    """

    state: Literal["live", "trashed", "all"]
    """
    Which set of assets to read from: `live` (default — only assets that are not
    trashed), `trashed` (only trashed assets, ordered by most recently trashed), or
    `all` (both live and trashed, ordered by capture time like `live`).
    """

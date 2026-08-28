# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
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
    `checksum`, `checksum_sha1`, `file_size_bytes`), and `variants` (every
    `asset_urls` rung beyond the lean one. Without it `asset_urls` carries only its
    lean rung — `thumbnail` for an image, or `thumbnail_image` for a video — so
    callers that render non-thumbnail variants or download the current rendering
    must pass it). Accepts multiple `include=` query params or a single
    comma-delimited value (e.g. `include=faces,people`). Unknown values return 422.
    When omitted, only the lean core is returned (`id`, `mime_type`,
    `local_datetime`, dimensions, `description`, `thumbhash`, `asset_urls`, `kind`,
    `current_version_id`) and each data field above is null/absent until you request
    it.
    """

    album_id: Optional[str]
    """Return only assets in this album — the album's `album_` ID, not its name."""

    bbox: Optional[str]
    """
    Bounding-box (map viewport) location filter: four comma-separated decimal-degree
    numbers `min_longitude,min_latitude,max_longitude,max_latitude`
    (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
    `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
    band running east from `min_longitude` over ±180° to `max_longitude`, so there
    is no need to split it client-side. Longitude order is therefore significant —
    transposed corners read as a crossing viewport, not as an error. A viewport 360°
    or wider must be sent as the full range `-180,...,180,...`, which the wrapped
    form cannot express.
    """

    center: Optional[str]
    """
    Center point of a radius location filter: two comma-separated decimal-degree
    numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.
    Mutually exclusive with `bbox`.
    """

    image: Optional[FileTypes]
    """Image file for an independent dense-image retrieval stage.

    When text is also provided, the stage ranks are fused rather than blending their
    embeddings.
    """

    library_id: Optional[str]
    """Library to search.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

    limit: int
    """Maximum number of results per page (1–200). Defaults to 20."""

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

    page: int
    """1-indexed page number; increment it to fetch subsequent pages.

    `search_assets` pages by number rather than by cursor. A search with a content
    criterion ranks a fixed top-200 candidate population by relevance, so pages
    beyond that population are empty. A structured-filter-only search (album,
    people, date range — no content criterion) returns the full matching set
    newest-first, paginated without that cap.
    """

    person_ids: Optional[SequenceNotStr[str]]
    """Filter to assets containing ALL of these person IDs (intersection, not union).

    Accepts multiple `person_ids=` form fields or a single comma-delimited value
    (e.g., `person_123,person_abc`). Person IDs are carried by the entries of an
    asset's `people` field (returned with `include=people`).
    """

    query: Optional[str]
    """
    Natural-language search text, matched against image embeddings and authoritative
    metadata. Album and people names belong in `album_id` and `person_ids`, and date
    ranges in `local_datetime_before`/`local_datetime_after`, not here.
    """

    radius: Optional[float]
    """
    Radius of the `center` location filter, in meters (greater than 0, at most
    50,000). Supply with `center`. Mutually exclusive with `bbox`.
    """

    ratings: Optional[Iterable[int]]
    """Return assets whose effective rating is one of these exact values.

    Values must be integers from `0` through `5`; `5` is a favorite. `0` matches
    every unrated form: an explicit zero, a null or legacy out-of-range effective
    rating, or an asset with no metadata. Accepts repeated `ratings=` parameters or
    one comma-delimited value. Omit the parameter for no rating filter.
    """

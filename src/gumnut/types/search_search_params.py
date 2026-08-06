# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SearchSearchParams"]


class SearchSearchParams(TypedDict, total=False):
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
    """

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

    Accepts multiple `person_ids=` query params or a single comma-delimited value
    (e.g., `person_123,person_abc`). Person IDs are carried by the entries of an
    asset's `people` field (returned with `include=people`).
    """

    query: Optional[str]
    """Natural-language search text.

    It runs independently through dense visual retrieval and authoritative-metadata
    full-text retrieval, then the ranked lists are fused. Concrete visual concepts
    work well in the dense stage, while exact metadata terms can match through
    full-text search.

    Resolve album and people names to IDs and pass them as `album_id` and
    `person_ids`; convert date phrases like 'in 2023' into ISO 8601 bounds on
    `local_datetime_after`/`local_datetime_before` (here, `2023-01-01` and
    `2024-01-01`). None of those belong in `query`.
    """

    radius: Optional[float]
    """
    Radius of the `center` location filter, in meters (greater than 0, at most
    50,000).
    """

    threshold: float
    """Deprecated compatibility parameter.

    Accepted and validated during the transition window but ignored:
    relevance-ranked results have no similarity-distance cutoff.
    """

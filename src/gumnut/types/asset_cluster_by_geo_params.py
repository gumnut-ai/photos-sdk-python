# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AssetClusterByGeoParams"]


class AssetClusterByGeoParams(TypedDict, total=False):
    bbox: Required[str]
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

    cell_size: Required[float]
    """Grid cell edge in decimal degrees — the clustering granularity.

    Larger values give coarser clusters; the client maps map-zoom to `cell_size`.
    Must be at least 0.0001 (~11 m).
    """

    album_id: Optional[str]
    """Return only assets in this album — the album's `album_` ID, not its name."""

    library_id: Optional[str]
    """Library to cluster assets from.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

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

    person_ids: Optional[SequenceNotStr[str]]
    """
    Cluster only assets containing faces belonging to ALL of these people
    (intersection, not union). Accepts up to 200 IDs across repeated `person_ids=`
    query params or comma-delimited values. Person IDs are carried by the entries of
    an asset's `people` field (returned with `include=people`).
    """

    state: Literal["live", "trashed", "all"]
    """
    Which set of assets to cluster: `live` (default — excludes trashed assets),
    `trashed` (only trashed assets), or `all` (both).
    """

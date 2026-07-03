# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetClusterByGeoParams"]


class AssetClusterByGeoParams(TypedDict, total=False):
    bbox: Required[str]
    """
    Map viewport as four comma-separated decimal-degree numbers
    `min_longitude,min_latitude,max_longitude,max_latitude` (west,south,east,north),
    e.g. `-77.1,38.9,-77.0,39.0`. A box whose `min_longitude` exceeds
    `max_longitude` (antimeridian-crossing) returns no cells — split it client-side.
    """

    cell_size: Required[float]
    """Grid cell edge in decimal degrees — the clustering granularity.

    Larger values give coarser clusters; the client maps map-zoom to `cell_size`.
    Must be at least 0.0001 (~11 m).
    """

    album_id: Optional[str]
    """Return only assets that are in the album with this ID."""

    library_id: Optional[str]
    """Library to cluster assets from.

    Optional if the user has a single library; required when they have multiple.
    """

    local_datetime_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly after this instant (ISO 8601; exclusive).

    Same awareness/offset semantics as on `list_assets`.
    """

    local_datetime_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly before this instant (ISO 8601; exclusive).

    Same awareness/offset semantics as on `list_assets`.
    """

    person_id: Optional[str]
    """Return only assets containing a face belonging to this person."""

    state: Literal["live", "trashed", "all"]
    """
    Which set of assets to cluster: `live` (default — excludes trashed assets),
    `trashed` (only trashed assets), or `all` (both).
    """

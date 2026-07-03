# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AssetClusterByGeoResponse", "Data"]


class Data(BaseModel):
    count: int
    """Number of assets in this grid cell."""

    latitude: float
    """
    Cluster centroid latitude in decimal degrees — the average latitude of the
    cell's members.
    """

    longitude: float
    """
    Cluster centroid longitude in decimal degrees — the average longitude of the
    cell's members.
    """

    representative_asset_id: str
    """
    ID of a cover asset for the cell — the most recently captured geotagged asset in
    it (ties broken by descending id).
    """


class AssetClusterByGeoResponse(BaseModel):
    data: List[Data]
    """Non-empty grid cells within the requested viewport.

    Not paginated: the list is capped at 1000 cells and a denser viewport returns
    422 instead — coarsen `cell_size` or zoom in.
    """

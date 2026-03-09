# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["AssetCountResponse", "Data"]


class Data(BaseModel):
    count: int
    """Number of assets in this time period"""

    time_bucket: datetime
    """Start of the time period"""


class AssetCountResponse(BaseModel):
    data: List[Data]

    has_more: bool

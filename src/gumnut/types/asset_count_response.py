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
    """Time bucket and count pairs, ordered by time bucket descending"""

    has_more: bool
    """True if there are more time buckets.

    To fetch the next page, pass the last `time_bucket` value as
    `local_datetime_before` (exclusive — buckets starting before that value are
    returned).
    """

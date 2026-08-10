# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetUpdateAssetParams"]


class AssetUpdateAssetParams(TypedDict, total=False):
    description: Optional[str]
    """User-set description for the asset.

    Pass `null` to remove a previously-set value; the effective response may still
    contain a description from another metadata source. Omit to leave unchanged.
    Distinct from the AI-generated `description` field on the response — this writes
    to `metadata.description`.
    """

    latitude: Optional[float]
    """GPS latitude in decimal degrees, `[-90, 90]`.

    Must be set together with `longitude`. Pass `null` (along with `longitude=null`)
    to remove a previously-set value; omit to leave unchanged.
    """

    longitude: Optional[float]
    """GPS longitude in decimal degrees, `[-180, 180]`.

    Must be set together with `latitude`. Pass `null` (along with `latitude=null`)
    to remove a previously-set value; omit to leave unchanged.
    """

    original_datetime: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the asset was originally captured.

    Timezone-aware values preserve their UTC offset; timezone-naive values have no
    offset. Pass `null` to remove a previously-set value; the effective response may
    still contain a datetime from another metadata source. Omit to leave unchanged.
    """

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

    Pass `null` to remove a previously-set value (the response then falls back to
    the description embedded in the file, if any). Omit to leave unchanged. Distinct
    from the AI-generated `description` field on the response — this writes to
    `metadata.description`.
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

    Aware values store the offset from `utcoffset()` alongside; naive values store
    NULL offset. Pass `null` to remove a previously-set value — the response then
    falls back to the datetime embedded in the file when present, otherwise to the
    file's upload timestamp. Omit to leave unchanged.
    """

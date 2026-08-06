# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AssetCheckExistenceParams"]


class AssetCheckExistenceParams(TypedDict, total=False):
    library_id: Optional[str]
    """Library to check assets in.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

    checksum_sha1s: Optional[SequenceNotStr[str]]
    """List of base64-encoded SHA-1 checksums to check for existence"""

    checksums: Optional[SequenceNotStr[str]]
    """List of base64-encoded SHA-256 checksums to check for existence"""

    device_asset_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="deviceAssetIds")]
    """List of device asset IDs to check for existence (requires deviceId)"""

    device_id: Annotated[Optional[str], PropertyInfo(alias="deviceId")]
    """Device ID to filter assets by (required with deviceAssetIds)"""

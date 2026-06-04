# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileDataResponse"]


class FileDataResponse(BaseModel):
    """File/provenance scalars describing the uploaded *file* (not its content).

    Returned only when requested via ``include=file_data``; the whole object is
    ``null`` otherwise. When present, every field carries its real value —
    ``checksum_sha1`` is the lone exception (``null`` for legacy rows that never
    had a SHA-1). This nested object is the home for the file/provenance group.
    """

    checksum: str
    """
    Base64-encoded SHA-256 hash of the asset contents for duplicate detection and
    integrity.
    """

    device_asset_id: str
    """Original asset identifier from the device that uploaded this asset."""

    device_id: str
    """Identifier of the device that uploaded this asset."""

    file_created_at: datetime
    """When the file was created on the uploading device."""

    file_modified_at: datetime
    """When the file was last modified on the uploading device."""

    file_size_bytes: int
    """File size of the asset in bytes."""

    checksum_sha1: Optional[str] = None
    """Base64-encoded SHA-1 hash for Immich client compatibility.

    `null` for older assets that have no SHA-1.
    """

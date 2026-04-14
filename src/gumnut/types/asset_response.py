# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .exif_response import ExifResponse
from .face_response import FaceResponse
from .person_response import PersonResponse

__all__ = ["AssetResponse", "AssetURLs"]


class AssetURLs(BaseModel):
    """A single image variant with its URL, MIME type, and target width."""

    mimetype: str
    """MIME type of the served image"""

    url: str
    """URL to fetch this image variant"""

    width: Optional[int] = None
    """Target width in pixels (null if unknown)"""


class AssetResponse(BaseModel):
    """Represents a photo or video asset with metadata and access URLs."""

    id: str
    """Unique asset identifier with 'asset\\__' prefix"""

    checksum: str
    """
    Base64-encoded SHA-256 hash of the asset contents for duplicate detection and
    integrity
    """

    created_at: datetime
    """When this asset record was created in the database"""

    device_asset_id: str
    """Original asset identifier from the device that uploaded this asset"""

    device_id: str
    """Identifier of the device that uploaded this asset"""

    file_created_at: datetime
    """When the file was created on the uploading device"""

    file_modified_at: datetime
    """When the file was last modified on the uploading device"""

    local_datetime: datetime
    """When the photo/video was taken, in the device's local timezone"""

    mime_type: str
    """MIME type of the file (e.g., 'image/jpeg', 'video/mp4')"""

    original_file_name: str
    """Original filename when the asset was uploaded"""

    updated_at: datetime
    """When this asset record was last updated"""

    asset_urls: Optional[Dict[str, AssetURLs]] = None
    """
    Named asset variants: 'original', 'thumbnail', 'preview', 'fullsize' for images;
    'original' only for videos
    """

    checksum_sha1: Optional[str] = None
    """Base64-encoded SHA-1 hash for Immich client compatibility.

    May be null for older assets.
    """

    description: Optional[str] = None
    """AI-generated description of the asset's content, quality, and composition.

    null means description generation has not yet run; empty string means the model
    refused to describe the asset. Distinct from exif.description (camera-embedded
    EXIF metadata).
    """

    exif: Optional[ExifResponse] = None
    """EXIF metadata extracted from image and video files."""

    faces: Optional[List[FaceResponse]] = None
    """All faces detected in this asset"""

    file_size_bytes: Optional[int] = None
    """File size of the asset in bytes"""

    height: Optional[int] = None
    """Height of the asset in pixels"""

    metrics: Optional[Dict[str, Optional[float]]] = None
    """ML-generated quality scores and other metrics"""

    people: Optional[List[PersonResponse]] = None
    """All unique people identified in this asset (deduplicated from faces)"""

    width: Optional[int] = None
    """Width of the asset in pixels"""

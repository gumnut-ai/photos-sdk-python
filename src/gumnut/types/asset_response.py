# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .exif_response import ExifResponse
from .face_response import FaceResponse
from .person_response import PersonResponse

__all__ = ["AssetResponse", "AssetURLs", "Metadata"]


class AssetURLs(BaseModel):
    """A single image variant with its URL, MIME type, and target width."""

    mimetype: str
    """MIME type of the served image"""

    url: str
    """URL to fetch this image variant"""

    width: Optional[int] = None
    """Target width in pixels (null if unknown)"""


class Metadata(BaseModel):
    """Metadata for an asset — camera/EXIF fields, GPS, and location names."""

    asset_id: str
    """ID of the asset this metadata belongs to"""

    created_at: datetime
    """When this metadata record was created"""

    updated_at: datetime
    """When this metadata record was last updated"""

    altitude: Optional[float] = None
    """GPS altitude in meters"""

    auto_stack_id: Optional[str] = None
    """Identifier for automatic photo stacking"""

    city: Optional[str] = None
    """City name"""

    country: Optional[str] = None
    """Country name"""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code (e.g., 'US', 'JP')"""

    description: Optional[str] = None
    """Image description or caption"""

    digitized_datetime: Optional[datetime] = None
    """When the photo was digitized, with timezone offset if available"""

    exposure_bias: Optional[float] = None
    """Exposure compensation in EV (e.g., -1.0, +0.5)"""

    exposure_time: Optional[float] = None
    """Shutter speed in seconds (e.g., 0.001 for 1/1000s)"""

    f_number: Optional[float] = None
    """Aperture f-stop value (e.g., 2.8, 5.6)"""

    focal_length: Optional[float] = None
    """Focal length in millimeters"""

    fps: Optional[float] = None
    """Frame rate for video files"""

    iso: Optional[int] = None
    """ISO sensitivity value (e.g., 100, 800, 3200)"""

    latitude: Optional[float] = None
    """GPS latitude in decimal degrees"""

    lens_model: Optional[str] = None
    """Lens model used (e.g., 'EF 24-70mm f/2.8L II USM')"""

    live_photo_cid: Optional[str] = None
    """Live photo content identifier"""

    longitude: Optional[float] = None
    """GPS longitude in decimal degrees"""

    make: Optional[str] = None
    """Camera manufacturer (e.g., 'Canon', 'Nikon')"""

    model: Optional[str] = None
    """Camera model (e.g., 'EOS 5D Mark IV')"""

    modified_datetime: Optional[datetime] = None
    """When the file was last modified, with timezone offset if available"""

    orientation: Optional[int] = None
    """
    Image orientation value (1-8) indicating rotation/flip: 1=normal, 2=mirror
    horizontal, 3=rotate 180°, 4=mirror vertical, 5=mirror horizontal+rotate 90° CW,
    6=rotate 90° CW, 7=mirror horizontal+rotate 90° CCW, 8=rotate 90° CCW
    """

    original_datetime: Optional[datetime] = None
    """When the photo was originally taken, with timezone offset if available"""

    place_name: Optional[str] = None
    """Landmark or point-of-interest name"""

    projection_type: Optional[str] = None
    """Projection type (e.g., for 360° photos)"""

    rating: Optional[int] = None
    """User or camera rating (typically 1-5 stars)"""

    state: Optional[str] = None
    """State/province name"""

    sublocation: Optional[str] = None
    """Neighborhood or district"""

    timezone: Optional[str] = None
    """IANA timezone identifier (e.g., 'America/Los_Angeles')"""


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

    metadata: Optional[Metadata] = None
    """Metadata for an asset — camera/EXIF fields, GPS, and location names."""

    metrics: Optional[Dict[str, Optional[float]]] = None
    """ML-generated quality scores and other metrics"""

    people: Optional[List[PersonResponse]] = None
    """All unique people identified in this asset (deduplicated from faces)"""

    width: Optional[int] = None
    """Width of the asset in pixels"""

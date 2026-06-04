# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .face_response import FaceResponse
from .person_response import PersonResponse
from .metadata_response import MetadataResponse
from .file_data_response import FileDataResponse
from .shared.asset_variant import AssetVariant

__all__ = ["AssetResponse"]


class AssetResponse(BaseModel):
    """Represents a photo or video asset with metadata and access URLs."""

    id: str
    """Unique asset identifier with 'asset\\__' prefix"""

    created_at: datetime
    """When this asset record was created in the database"""

    local_datetime: datetime
    """When the photo/video was taken, in the device's local timezone"""

    mime_type: str
    """MIME type of the file (e.g., 'image/jpeg', 'video/mp4')"""

    original_file_name: str
    """Original filename when the asset was uploaded"""

    updated_at: datetime
    """When this asset record was last updated"""

    asset_urls: Optional[Dict[str, AssetVariant]] = None
    """Named asset variants.

    Images: 'original', 'thumbnail', 'preview', 'fullsize'. Videos: 'original'
    always, plus 'thumbnail_image', 'preview_image', 'fullsize_image' once a still
    has been extracted.
    """

    description: Optional[str] = None
    """AI-generated description of the asset's content, quality, and composition.

    null means description generation has not yet run; empty string means the model
    refused to describe the asset. Distinct from metadata.description
    (camera-embedded EXIF metadata).
    """

    duration: Optional[float] = None
    """Video length in seconds.

    `null` for images and for videos whose duration has not been extracted yet.
    """

    faces: Optional[List[FaceResponse]] = None
    """All faces detected in this asset.

    `null` when not requested via `include=faces`; `[]` when requested but the asset
    has no faces.
    """

    file_data: Optional[FileDataResponse] = None
    """File/provenance scalars describing the uploaded _file_ (not its content).

    Returned only when requested via `include=file_data`; the whole object is `null`
    otherwise. When present, every field carries its real value — `checksum_sha1` is
    the lone exception (`null` for legacy rows that never had a SHA-1). This nested
    object is the home for the file/provenance group.
    """

    height: Optional[int] = None
    """Height of the asset in pixels"""

    metadata: Optional[MetadataResponse] = None
    """Metadata for an asset — camera/EXIF fields, GPS, and location names."""

    metrics: Optional[Dict[str, Optional[float]]] = None
    """ML-generated quality scores and other metrics.

    `null` when not requested via `include=metrics`.
    """

    people: Optional[List[PersonResponse]] = None
    """All unique people identified in this asset (deduplicated from faces).

    `null` when not requested via `include=people`; `[]` when requested but none are
    identified.
    """

    thumbhash: Optional[str] = None
    """Base64-encoded ThumbHash placeholder (~28 chars).

    Clients decode with the `thumbhash` library (JS / Swift / Kotlin) to render an
    instant blurred preview before the CDN thumbnail arrives. `null` while
    generation is pending.
    """

    trashed_at: Optional[datetime] = None
    """When this asset was moved to trash (ISO 8601, UTC).

    `null` for live assets. Trashed assets are excluded from default list/search
    results and are purged after the configured retention window.
    """

    width: Optional[int] = None
    """Width of the asset in pixels"""

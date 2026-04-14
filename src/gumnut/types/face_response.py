# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FaceResponse", "AssetURLs"]


class AssetURLs(BaseModel):
    """A single image variant with its URL, MIME type, and target width."""

    mimetype: str
    """MIME type of the served image"""

    url: str
    """URL to fetch this image variant"""

    width: Optional[int] = None
    """Target width in pixels (null if unknown)"""


class FaceResponse(BaseModel):
    """Represents a detected face in an asset with facial recognition data."""

    id: str
    """Unique face identifier with 'face\\__' prefix"""

    asset_id: str
    """ID of the asset containing this face"""

    bounding_box: Dict[str, int]
    """Face location as {x, y, w, h} coordinates in pixels"""

    created_at: datetime
    """When this face was detected and recorded"""

    updated_at: datetime
    """When this face record was last updated"""

    asset_urls: Optional[Dict[str, AssetURLs]] = None
    """Asset variants for this face: 'thumbnail' with face crop"""

    person_id: Optional[str] = None
    """ID of the person this face belongs to (if identified)"""

    timestamp_ms: Optional[int] = None
    """For video files, timestamp in milliseconds when face appears"""

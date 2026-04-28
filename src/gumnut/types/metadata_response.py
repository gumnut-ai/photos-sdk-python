# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MetadataResponse"]


class MetadataResponse(BaseModel):
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

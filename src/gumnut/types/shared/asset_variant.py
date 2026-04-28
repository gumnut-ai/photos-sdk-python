# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AssetVariant"]


class AssetVariant(BaseModel):
    """A single image variant with its URL, MIME type, and target width."""

    mimetype: str
    """MIME type of the served image"""

    url: str
    """URL to fetch this image variant"""

    width: Optional[int] = None
    """Target width in pixels (null if unknown)"""

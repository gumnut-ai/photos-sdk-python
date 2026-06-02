# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["LibraryResponse"]


class LibraryResponse(BaseModel):
    """Represents a user's photo library."""

    id: str
    """Unique library identifier with 'lib\\__' prefix"""

    asset_count: int
    """Total number of assets in this library"""

    created_at: datetime
    """When this library was created"""

    name: str
    """Display name of the library"""

    storage_used_bytes: int
    """Bytes of assets currently stored in this library"""

    updated_at: datetime
    """When this library was last updated"""

    user_id: str
    """ID of the user who owns this library"""

    description: Optional[str] = None
    """Optional description text for the library"""

    storage_limit_bytes: Optional[int] = None
    """Maximum bytes this library may store, or null if no per-library limit applies"""

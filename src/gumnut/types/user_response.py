# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserResponse"]


class UserResponse(BaseModel):
    """Represents a user account with profile information."""

    id: str
    """Unique user identifier with 'intuser\\__' prefix"""

    created_at: datetime
    """When this user account was created"""

    demo_mode_enabled: bool
    """Whether demo-mode person-name presentation is enabled. Defaults to false."""

    face_detection_available: bool
    """Whether automatic face detection can be turned on for this user.

    False when the declared home region is one where it is not offered;
    `face_detection_preference` is then false and cannot be set to true.
    """

    face_detection_preference: Optional[bool] = None
    """
    Whether automatic face detection is on for the libraries this user owns: true is
    on, false is off, null means the user has not chosen yet. Faces are currently
    detected automatically when this is true or null.
    """

    favorite_display_mode: Literal["favorite", "rating"]
    """
    The user's effective favorite/rating display mode, defaulting to `favorite` when
    they have never selected one.
    """

    is_active: bool
    """Whether this user account is currently active"""

    is_superuser: bool
    """Whether this user has superuser/admin privileges"""

    is_verified: bool
    """Whether the account is marked verified.

    An internal account flag, not proof of email verification — it can be true even
    when `email` is null
    """

    storage_limit_bytes: int
    """Maximum bytes of assets the user may store"""

    storage_used_bytes: int
    """Total bytes of assets the user is currently storing"""

    updated_at: datetime
    """When this user account was last updated"""

    email: Optional[str] = None
    """User's email address"""

    first_name: Optional[str] = None
    """User's first name"""

    home_country: Optional[str] = None
    """The user's declared home country as an ISO 3166-1 alpha-2 code (e.g.

    'US'); null until declared
    """

    home_subdivision: Optional[str] = None
    """
    The user's declared home state or province: an ISO 3166-2 code without its
    country prefix (e.g. 'CA' for US-CA); null when not declared
    """

    immich_library_id: Optional[str] = None
    """The user's stored preferred library, or null to use the default.

    Reported as stored: the library may since have been trashed, or the user's
    access to it may have changed.
    """

    last_name: Optional[str] = None
    """User's last name"""

    timezone: Optional[str] = None
    """User's home timezone as an IANA zone id (e.g.

    'America/Los_Angeles'); null until a home zone is captured
    """

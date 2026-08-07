# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExchangeResponse", "User"]


class User(BaseModel):
    """The authenticated user"""

    id: str
    """Unique Gumnut user identifier with `intuser_` prefix"""

    clerk_user_id: Optional[str] = None
    """Identifier of the linked identity-provider account"""

    email: Optional[str] = None
    """Email address reported by the OAuth provider; null if not shared"""

    first_name: Optional[str] = None
    """Given name reported by the OAuth provider; null if not shared"""

    is_active: bool
    """Whether the account is active.

    A token exchange can still succeed for an inactive account, but subsequent
    authenticated API requests are rejected with 401
    """

    is_verified: bool
    """Whether the account is marked verified.

    An internal account flag, not proof of email verification — it can be true even
    when `email` is null
    """

    last_name: Optional[str] = None
    """Family name reported by the OAuth provider; null if not shared"""


class ExchangeResponse(BaseModel):
    """Response containing JWT and user info"""

    access_token: str
    """
    JWT to send as a Bearer token in the `Authorization` header on subsequent
    requests
    """

    user: User
    """The authenticated user"""

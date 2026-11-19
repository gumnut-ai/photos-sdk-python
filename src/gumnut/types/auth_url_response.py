# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AuthURLResponse"]


class AuthURLResponse(BaseModel):
    """Response containing OAuth authorization URL"""

    url: str
    """OAuth provider authorization URL to redirect the user to for consent"""

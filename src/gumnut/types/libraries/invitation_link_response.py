# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .invitation_response import InvitationResponse

__all__ = ["InvitationLinkResponse"]


class InvitationLinkResponse(BaseModel):
    invitation: InvitationResponse
    """Active invitation whose link is being returned."""

    url: str
    """Complete browser invitation URL; its fragment contains a bearer secret."""

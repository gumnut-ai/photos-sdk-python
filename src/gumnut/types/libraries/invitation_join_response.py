# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..library_response import LibraryResponse
from .membership_response import MembershipResponse

__all__ = ["InvitationJoinResponse"]


class InvitationJoinResponse(BaseModel):
    library: LibraryResponse
    """Library context with the caller's actual role."""

    membership: Optional[MembershipResponse] = None
    """Active non-owner membership; null only when the caller owns the library."""

    outcome: Literal["joined", "already_member"]
    """Whether this request admitted the account or returned unchanged access."""

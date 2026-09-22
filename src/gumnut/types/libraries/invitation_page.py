# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .invitation_response import InvitationResponse

__all__ = ["InvitationPage"]


class InvitationPage(BaseModel):
    data: List[InvitationResponse]
    """Invitation metadata in newest-first order; secrets are omitted."""

    has_more: bool
    """Whether another page exists.

    Pass the last item's ID as `starting_after_id` and repeat the same `library_id`
    and `state` filters.
    """

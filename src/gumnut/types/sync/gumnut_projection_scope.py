# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..library_response import LibraryResponse

__all__ = ["GumnutProjectionScope"]


class GumnutProjectionScope(BaseModel):
    library: LibraryResponse
    """Current actual library owner, caller role, counts, limits, and profile"""

    library_id: str
    """Current bound library identifier"""

    policy_fingerprint: str
    """
    Opaque source eligibility policy fingerprint; a changed value requires coverage
    rebuild
    """

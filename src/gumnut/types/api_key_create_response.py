# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKeyCreateResponse"]


class APIKeyCreateResponse(BaseModel):
    """Response when creating a new API key - includes the actual key value.

    This is the only time the raw API key is exposed. After creation,
    only the hashed version is stored and the raw key cannot be retrieved.
    """

    id: str
    """Unique API key identifier with 'apikey\\__' prefix"""

    api_key: str
    """The actual API key value - store this securely as it cannot be retrieved later"""

    created_at: datetime
    """When this API key was created"""

    is_active: bool
    """Whether this API key is currently valid and can be used"""

    actions: Optional[List[Literal["read", "write", "delete", "delete_permanently"]]] = None
    """Action verbs this key's grant allows; null for legacy keys"""

    last_used_at: Optional[datetime] = None
    """When this API key was last used for authentication"""

    library_scope_mode: Optional[Literal["all_libraries", "selected_libraries"]] = None
    """Which of the owner's libraries a grant covers.

    `all_libraries` means all current and future live libraries owned by the grant's
    user. `selected_libraries` means only the libraries listed in
    `access_grant_libraries`, with no automatic expansion.
    """

    name: Optional[str] = None
    """Optional descriptive name for this API key"""

    selected_library_count: Optional[int] = None
    """
    Number of libraries a 'selected_libraries' grant covers; null unless
    library_scope_mode is 'selected_libraries'
    """

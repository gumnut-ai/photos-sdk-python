# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StackListStacksResponse"]


class StackListStacksResponse(BaseModel):
    """Represents a group of assets displayed as a single tile."""

    id: str
    """Unique stack identifier with 'asset*stack*' prefix"""

    asset_count: int
    """Number of live assets in this stack.

    Excludes trashed members, so it can drop below the number of frames originally
    grouped.
    """

    created_at: datetime
    """When this stack was created"""

    origin: Literal["auto_burst", "user"]
    """How a stack came to exist.

    `auto_burst` marks a stack the burst detector created from the time +
    EXIF-camera signal; `user` marks a stack a user created or edited (manual
    create, set-cover, add/remove, unstack). The distinction is what keeps
    re-detection from stomping a user's correction — the detection pass skips `user`
    stacks.
    """

    updated_at: datetime
    """When this stack was last updated"""

    primary_asset_id: Optional[str] = None
    """ID of the asset the user pinned as the stack's cover, or null if none is pinned.

    Null for an auto-detected burst unless a user has since pinned a cover — there
    is no server-selected default, so a client showing a stack with no pinned cover
    picks its own. A pinned cover that has been trashed keeps its ID here; it is
    cleared only once the asset is permanently deleted.
    """

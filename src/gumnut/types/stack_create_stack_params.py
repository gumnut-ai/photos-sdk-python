# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["StackCreateStackParams"]


class StackCreateStackParams(TypedDict, total=False):
    asset_ids: Required[SequenceNotStr[str]]
    """
    Asset IDs (with `asset_` prefix) to group into the new stack — at least 2
    distinct ids, all in the target library.
    """

    library_id: Optional[str]
    """Library to create the stack in.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

    primary_asset_id: Optional[str]
    """
    Asset ID (with `asset_` prefix) to pin as the stack's cover; must be one of
    `asset_ids`. Omit to leave the cover unpinned — there is no automatic pick, and
    clients choose their own display cover for an unpinned stack.
    """

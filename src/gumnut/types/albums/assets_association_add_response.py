# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["AssetsAssociationAddResponse"]


class AssetsAssociationAddResponse(BaseModel):
    added_assets: List[str]
    """Asset IDs newly added to the album by this call."""

    duplicate_assets: List[str]
    """
    Asset IDs that were already in the album and were skipped (idempotent no-op, not
    an error).
    """

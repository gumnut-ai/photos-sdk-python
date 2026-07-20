# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AssetDeleteListParams"]


class AssetDeleteListParams(TypedDict, total=False):
    ids: Required[SequenceNotStr[str]]
    """Asset IDs (each with the `asset_` prefix) to operate on.

    Up to 200 ids per request.
    """

    library_id: Optional[str]
    """Library that owns the assets.

    Optional if the user has a single library; required when they have multiple.
    """

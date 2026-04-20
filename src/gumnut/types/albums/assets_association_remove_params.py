# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AssetsAssociationRemoveParams"]


class AssetsAssociationRemoveParams(TypedDict, total=False):
    asset_ids: Required[SequenceNotStr[str]]
    """Asset IDs (with `asset_` prefix) to associate with the album.

    Get IDs from `list_assets`, `search_assets`, or `list_album_assets`.
    """

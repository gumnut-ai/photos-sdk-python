# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AssetMoveParams"]


class AssetMoveParams(TypedDict, total=False):
    asset_ids: Required[SequenceNotStr[str]]
    """Asset IDs (each with the `asset_` prefix) to move."""

    destination_library_id: Required[str]
    """Library to move the assets into.

    The caller must own it or be a collaborator on it. Must differ from
    `source_library_id`.
    """

    source_library_id: Required[str]
    """Library the assets are in now. The caller must own it."""

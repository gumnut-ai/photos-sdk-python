# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["StackAddAssetsToStackParams"]


class StackAddAssetsToStackParams(TypedDict, total=False):
    asset_ids: Required[SequenceNotStr[str]]
    """
    Asset IDs (with `asset_` prefix) to add to the stack — all in the stack's
    library.
    """

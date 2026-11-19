# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["StackRemoveAssetsParams"]


class StackRemoveAssetsParams(TypedDict, total=False):
    asset_ids: Required[SequenceNotStr[str]]
    """Asset IDs (with `asset_` prefix) to pull out of the stack.

    List assets with `stack_id` to get member IDs. Up to 200 ids per request.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StackSetCoverParams"]


class StackSetCoverParams(TypedDict, total=False):
    primary_asset_id: Required[str]
    """Asset ID (with `asset_` prefix) to pin as the stack's cover.

    Must be a live, current member of this stack — get member IDs from `list_assets`
    with `stack_id`.
    """

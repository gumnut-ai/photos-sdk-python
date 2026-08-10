# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VersionRevertParams"]


class VersionRevertParams(TypedDict, total=False):
    asset_id: Required[str]
    """Asset ID (with `asset_` prefix) to revert."""

    expected_current_version_id: Required[str]
    """Current version ID observed by the client.

    If stale, returns 409 without changes; refetch the asset before retrying.
    """

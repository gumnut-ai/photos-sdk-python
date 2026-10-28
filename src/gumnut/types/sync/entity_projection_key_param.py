# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EntityProjectionKeyParam"]


class EntityProjectionKeyParam(TypedDict, total=False):
    id: Required[str]
    """Stable entity identifier; current_user must name the authenticated principal"""

    kind: Required[Literal["current_user", "asset", "person", "face", "stack", "album"]]

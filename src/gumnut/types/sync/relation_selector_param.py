# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RelationSelectorParam"]


class RelationSelectorParam(TypedDict, total=False):
    parent_id: Required[str]
    """Parent whose current result accompanies each child page"""

    relation: Required[Literal["asset_faces", "asset_albums", "person_faces", "stack_assets", "album_assets"]]
    """Approved child relationship to enumerate"""

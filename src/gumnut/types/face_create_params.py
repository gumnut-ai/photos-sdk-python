# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FaceCreateParams", "BoundingBox"]


class FaceCreateParams(TypedDict, total=False):
    asset_id: Required[str]
    """ID of the asset (with `asset_` prefix) to draw the face box on.

    Get IDs from `list_assets` / `search_assets`. The asset must belong to the
    target library.
    """

    bounding_box: Required[BoundingBox]
    """
    Where the face is, as a box in display-space pixels matching the asset's
    reported `width`/`height`. The box must fit inside those dimensions.
    """

    library_id: Optional[str]
    """Library to create the face in.

    Optional if the user has a single library; required when they have multiple.
    """

    person_id: Optional[str]
    """Optional person ID (with `person_` prefix) to assign this face to at creation.

    Omit to leave it unassigned; assign it later via `update_face`. Get IDs from
    `list_people`; use `create_person` first if the identity doesn't exist yet.
    """


class BoundingBox(TypedDict, total=False):
    """
    Where the face is, as a box in display-space pixels matching the asset's reported `width`/`height`. The box must fit inside those dimensions.
    """

    h: Required[int]
    """Box height in pixels. `y + h` must not exceed the asset's height."""

    w: Required[int]
    """Box width in pixels. `x + w` must not exceed the asset's width."""

    x: Required[int]
    """Left edge, in pixels from the asset's left side (0-based)."""

    y: Required[int]
    """Top edge, in pixels from the asset's top side (0-based)."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BodyResponse", "Candidate"]


class Candidate(BaseModel):
    """A named person who may be the one in a body."""

    name: str
    """The person's name."""

    person_id: str
    """Person ID (with 'person\\__' prefix)."""


class BodyResponse(BaseModel):
    """A person found in an asset without a face record."""

    id: str
    """Unique body identifier with 'body\\__' prefix"""

    asset_id: str
    """ID of the asset containing this body"""

    assignment_source: Optional[Literal["automatic", "manual"]] = None
    """How a body's person was set: by automatic naming or by a person."""

    bounding_box: Dict[str, int]
    """
    Where the person is, as {x, y, w, h} in pixels: (x, y) is the box's top-left
    corner and w, h its size, on the image as displayed (EXIF orientation applied),
    so they match the asset's `width` and `height`
    """

    created_at: datetime
    """When this body was detected"""

    person_id: Optional[str] = None
    """ID of the person this body is linked to, or `null` when it has none yet."""

    updated_at: datetime
    """When this body record was last updated"""

    candidates: Optional[List[Candidate]] = None
    """
    Named people who may be the person in this body, best match first, at most 5;
    never its current person. Link one with `update_body`. Populated only when
    `list_bodies` or `get_body` is called with `include=candidates`; `null`
    otherwise. `[]` when there are none, including while the library owner's
    settings do not allow automatic face detection.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonUpdateParams"]


class PersonUpdateParams(TypedDict, total=False):
    birth_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """New birth date (ISO 8601 date). Omit to leave unchanged."""

    is_favorite: Optional[bool]
    """Mark or unmark this person as a favorite. Omit to leave unchanged."""

    is_hidden: Optional[bool]
    """Hide or unhide this person. Omit to leave unchanged."""

    name: Optional[str]
    """New display name. Omit to leave unchanged."""

    thumbnail_face_id: Optional[str]
    """New thumbnail face ID for this person.

    Omit to leave unchanged. Get face IDs from `list_faces`.
    """

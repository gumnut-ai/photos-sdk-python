# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonCreateParams"]


class PersonCreateParams(TypedDict, total=False):
    birth_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Optional birth date (ISO 8601 date, YYYY-MM-DD) for this person."""

    is_favorite: Optional[bool]
    """If true, the person is marked as a favorite. Defaults to false."""

    is_hidden: Optional[bool]
    """If true, the person is hidden from default listings. Defaults to false."""

    library_id: Optional[str]
    """Library to create the person in.

    Optional if the user has a single library; required when they have multiple.
    """

    name: Optional[str]
    """Display name for the new person (e.g., 'Alice').

    Optional — unnamed people can be named later via `update_person`.
    """

    thumbnail_face_id: Optional[str]
    """ID of the face to use as this person's thumbnail (with `face_` prefix).

    Typically set after the person has at least one associated face — get face IDs
    from `list_faces`.
    """

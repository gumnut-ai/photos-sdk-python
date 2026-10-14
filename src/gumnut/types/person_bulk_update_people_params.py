# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PersonBulkUpdatePeopleParams", "Update", "UpdateChange"]


class PersonBulkUpdatePeopleParams(TypedDict, total=False):
    updates: Required[Iterable[Update]]
    """List of per-person updates.

    Each item carries the target person id and the change to apply to it; different
    fields can be changed on different people in the same request. Up to 200 items
    per request.
    """


class UpdateChange(TypedDict, total=False):
    """The change to apply to this person.

    Same shape as the body of the single-person `update_person` endpoint — same fields, same validation; omitted fields are unchanged.
    """

    birth_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """New birth date (ISO 8601 date). Omit to leave unchanged."""

    is_favorite: bool
    """Mark or unmark this person as a favorite. Omit to leave unchanged."""

    is_hidden: bool
    """Hide or unhide this person. Omit to leave unchanged."""

    name: Optional[str]
    """New display name; must not be blank.

    Surrounding whitespace is trimmed. Omit to leave unchanged; pass `null` to clear
    the name.
    """

    thumbnail_face_id: Optional[str]
    """New thumbnail face ID for this person.

    Omit to leave unchanged. Enumerate a person's faces with `list_faces` and
    `person_id`.
    """


class Update(TypedDict, total=False):
    """One person update in a bulk request."""

    id: Required[str]
    """Person ID (with the `person_` prefix) to apply this change to."""

    change: Required[UpdateChange]
    """The change to apply to this person.

    Same shape as the body of the single-person `update_person` endpoint — same
    fields, same validation; omitted fields are unchanged.
    """

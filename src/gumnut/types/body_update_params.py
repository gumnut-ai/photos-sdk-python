# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BodyUpdateParams"]


class BodyUpdateParams(TypedDict, total=False):
    person_id: Required[Optional[str]]
    """
    Person ID (with `person_` prefix) to link this body to, or `null` to remove its
    person; the body stays, with no person.
    """

    library_id: Optional[str]
    """Library the body belongs to.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

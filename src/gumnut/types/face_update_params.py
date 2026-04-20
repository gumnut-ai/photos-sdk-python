# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FaceUpdateParams"]


class FaceUpdateParams(TypedDict, total=False):
    library_id: Optional[str]
    """Library the face belongs to.

    Optional if the user has a single library; required when they have multiple.
    """

    person_id: Optional[str]
    """Target person ID (with `person_` prefix) to assign this face to.

    Pass `null` to detach the face from its current person without deleting either.
    Get IDs from `list_people`; use `create_person` first if the target identity
    doesn't exist yet.
    """

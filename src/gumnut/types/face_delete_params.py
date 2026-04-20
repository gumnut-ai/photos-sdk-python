# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FaceDeleteParams"]


class FaceDeleteParams(TypedDict, total=False):
    library_id: Optional[str]
    """Library the face belongs to.

    Optional if the user has a single library; required when they have multiple.
    """

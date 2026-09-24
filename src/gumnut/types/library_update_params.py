# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LibraryUpdateParams"]


class LibraryUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """New free-form description for the library. Omit to leave unchanged."""

    name: Optional[str]
    """New display name for the library; must not be blank.

    Surrounding whitespace is trimmed. Omit or send `null` to leave unchanged.
    """

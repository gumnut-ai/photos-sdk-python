# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    demo_mode_enabled: bool
    """Enable demo-mode person-name presentation.

    Omit to leave unchanged; send false to disable. Explicit null is not accepted.
    """

    favorite_display_mode: Optional[Literal["favorite", "rating"]]
    """Presentation a user prefers for the favorite/rating control.

    - `favorite`: a heart — filled at the top rating, empty otherwise.
    - `rating`: a 0-5 star control.
    """

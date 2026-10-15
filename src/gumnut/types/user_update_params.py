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

    face_detection_preference: Optional[bool]
    """
    Turn automatic face detection on (true) or off (false) for the libraries the
    user owns. Omit to leave unchanged; explicit null is not accepted. The setting
    applies to photos processed from then on; face data already stored is kept.
    """

    favorite_display_mode: Optional[Literal["favorite", "rating"]]
    """Presentation a user prefers for the favorite/rating control.

    - `favorite`: a heart — filled at the top rating, empty otherwise.
    - `rating`: a 0-5 star control.
    """

    home_country: Optional[str]
    """Home country as an uppercase ISO 3166-1 alpha-2 code (e.g.

    'US'). Omit to leave unchanged; explicit null is not accepted. Changing the
    country clears `home_subdivision` unless the same request sets it.
    """

    home_subdivision: Optional[str]
    """Home state or province: an ISO 3166-2 code without its country prefix (e.g.

    'CA' for US-CA). Required when the home country is 'US'. Omit to leave
    unchanged; send `null` to clear it.
    """

    immich_library_id: Optional[str]
    """Preferred library.

    Must be a live library the caller owns or has the collaborator role in, and that
    the request's credential can access; any other id returns 404. Omit to leave
    unchanged; send `null` to clear the preference and use the default.
    """

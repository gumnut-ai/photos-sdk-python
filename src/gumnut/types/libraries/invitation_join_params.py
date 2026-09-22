# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvitationJoinParams"]


class InvitationJoinParams(TypedDict, total=False):
    secret: Required[str]
    """Opaque secret from the invitation URL fragment."""

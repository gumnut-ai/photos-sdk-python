# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from ..user_response import UserResponse
from .current_user_projection_key import CurrentUserProjectionKey

__all__ = ["CurrentUserProjection"]


class CurrentUserProjection(BaseModel):
    key: CurrentUserProjectionKey
    """Stable key matching this projection value"""

    kind: Literal["current_user"]

    value: UserResponse
    """Fully materialized current domain value"""

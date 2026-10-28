# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .face_projection_key import FaceProjectionKey
from .face_projection_value import FaceProjectionValue

__all__ = ["FaceProjection"]


class FaceProjection(BaseModel):
    key: FaceProjectionKey
    """Stable key matching this projection value"""

    kind: Literal["face"]

    value: FaceProjectionValue
    """Fully materialized current domain value"""

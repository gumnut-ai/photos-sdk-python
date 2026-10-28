# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..face_response import FaceResponse

__all__ = ["FaceProjectionValue"]


class FaceProjectionValue(BaseModel):
    coordinate_height: int
    """Original frame height in pixels"""

    coordinate_width: int
    """Original frame width in pixels"""

    face: FaceResponse
    """Eligible face in its original coordinate frame"""

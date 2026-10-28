# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .projection_key import ProjectionKey

__all__ = ["ProjectionRootResult"]


class ProjectionRootResult(BaseModel):
    key: ProjectionKey
    """Exactly one of the selected root keys"""

    status: Literal["present", "absent", "not_projected"]
    """Present, absent from this library, or excluded by profile eligibility"""

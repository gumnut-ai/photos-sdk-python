# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .projection_error_detail import ProjectionErrorDetail

__all__ = ["ProjectionErrorResponse"]


class ProjectionErrorResponse(BaseModel):
    detail: ProjectionErrorDetail
    """Structured projection failure with no partial bundle"""

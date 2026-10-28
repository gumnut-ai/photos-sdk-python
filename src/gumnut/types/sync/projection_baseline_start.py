# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .baseline_family_tokens import BaselineFamilyTokens

__all__ = ["ProjectionBaselineStart"]


class ProjectionBaselineStart(BaseModel):
    family_tokens: BaselineFamilyTokens

    source_cursor: None = None
    """Version one starts catch-up at the beginning of retained event history"""

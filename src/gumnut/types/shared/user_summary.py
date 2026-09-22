# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UserSummary"]


class UserSummary(BaseModel):
    id: str
    """User identifier"""

    display_name: Optional[str] = None
    """Public display name, when available"""

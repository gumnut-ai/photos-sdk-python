# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ProjectionEnumeration"]


class ProjectionEnumeration(BaseModel):
    complete: bool

    next_token: Optional[str] = None

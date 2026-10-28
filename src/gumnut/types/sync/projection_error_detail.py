# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ProjectionErrorDetail"]


class ProjectionErrorDetail(BaseModel):
    code: str
    """Stable machine-readable projection error code"""

    message: str
    """Safe server-owned explanation"""

    retryable: bool
    """Whether retrying a fresh read without changing input may succeed"""

    limit: Optional[Literal["roots", "projections", "bytes", "snapshot_ms"]] = None

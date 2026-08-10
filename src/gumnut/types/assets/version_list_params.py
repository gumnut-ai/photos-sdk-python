# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["VersionListParams"]


class VersionListParams(TypedDict, total=False):
    include: Optional[SequenceNotStr[str]]
    """Optional response expansion.

    The single accepted value is `variants`: without it each row's `version_urls`
    carries only its lean thumbnail rung; with it, every rung plus the signed
    exact-byte `original`. Accepts multiple `include=` query params or a single
    comma-delimited value. Unknown values return 422.
    """

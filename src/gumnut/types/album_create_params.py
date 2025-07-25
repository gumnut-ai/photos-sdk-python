# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AlbumCreateParams"]


class AlbumCreateParams(TypedDict, total=False):
    description: Optional[str]

    library_id: Optional[str]

    name: Optional[str]

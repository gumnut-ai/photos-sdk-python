# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LibraryListParams"]


class LibraryListParams(TypedDict, total=False):
    state: Literal["live", "trashed", "all"]
    """
    Which set of libraries to return: `live` (default — excludes trashed), `trashed`
    (only trashed, ordered by most recently trashed), or `all` (both).
    """

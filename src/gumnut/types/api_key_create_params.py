# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    actions: Required[List[Literal["read", "write", "delete", "delete_permanently"]]]
    """Action verbs the key may perform (at least one).

    `read` is required whenever any broader action is selected. Pass all four
    actions for a full-access key.
    """

    library_scope_mode: Required[Literal["all_libraries", "selected_libraries"]]
    """
    Which libraries the key covers: `all_libraries` (all current and future
    libraries) or `selected_libraries`.
    """

    name: Required[str]

    library_ids: Optional[SequenceNotStr[str]]
    """Libraries the key covers.

    Required (at least one) when `library_scope_mode` is `selected_libraries`; not
    allowed otherwise. Up to 200 ids.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]

    actions: Optional[List[Literal["read", "write", "delete", "delete_permanently"]]]
    """Action verbs the key may perform.

    Omit for full access. `read` is required whenever any broader action is
    selected.
    """

    library_ids: Optional[SequenceNotStr[str]]
    """Libraries the key covers.

    Required (at least one) when `library_scope_mode` is `selected_libraries`; not
    allowed otherwise. Up to 200 ids.
    """

    library_scope_mode: Optional[Literal["all_libraries", "selected_libraries"]]
    """Which of the owner's libraries a grant covers.

    `all_libraries` means all current and future live libraries owned by the grant's
    user. `selected_libraries` means only the libraries listed in
    `access_grant_libraries`, with no automatic expansion.
    """

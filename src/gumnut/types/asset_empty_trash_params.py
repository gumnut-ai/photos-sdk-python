# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AssetEmptyTrashParams"]


class AssetEmptyTrashParams(TypedDict, total=False):
    library_id: Optional[str]
    """Library whose trashed assets to permanently delete.

    Optional if the user has a single library; required when they have multiple.
    """

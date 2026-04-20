# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    album_id: Optional[str]
    """Return only assets that are in the album with this ID.

    Equivalent to calling `list_album_assets` with `album_id` and then fetching each
    asset — prefer this param when you need the full asset metadata in one call.
    """

    ids: Optional[SequenceNotStr[str]]
    """Look up specific assets by ID (max 100; each ID has the `asset_` prefix).

    Use this for bulk fetch when you already have asset IDs. Combines with other
    filters (album_id, person_id, datetime range) using AND logic — the result is
    the intersection.
    """

    library_id: Optional[str]
    """Library to list assets from.

    Optional if the user has a single library; required when they have multiple. Use
    `list_libraries` to enumerate available libraries.
    """

    limit: int
    """Maximum number of assets to return per page (1–200). Defaults to 20."""

    local_datetime_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly after this instant (ISO 8601; exclusive).

    `local_datetime` is the photo's wall-clock time in the device's own timezone.
    Naive values compare directly against `local_datetime`. Timezone-aware values:
    assets with a known offset are compared in UTC (`local_datetime - offset`);
    assets without an offset fall back to wall-clock comparison against
    `local_datetime`. Equivalent in purpose to `captured_after` on `search_assets`
    (naming inconsistency is tracked as a follow-up).
    """

    local_datetime_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly before this instant (ISO 8601; exclusive).

    Same awareness/offset semantics as `local_datetime_after`. Equivalent in purpose
    to `captured_before` on `search_assets` (naming inconsistency is tracked as a
    follow-up).
    """

    person_id: Optional[str]
    """Return only assets containing a face belonging to this person.

    Singular on this tool; the sibling `search_assets` uses `person_ids` (plural,
    ALL-of).
    """

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last asset in the previous response's `data` to fetch the
    next page. Omit for the first page. `list_assets` uses cursor pagination; the
    sibling `search_assets` uses 1-indexed `page` numbers (naming inconsistency is
    tracked as a follow-up).
    """

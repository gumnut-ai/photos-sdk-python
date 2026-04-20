# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventGetParams"]


class EventGetParams(TypedDict, total=False):
    after_cursor: Optional[str]
    """Opaque cursor from the last event of the previous page.

    Pass the `cursor` field from the last event to fetch the next page. Omit for the
    first page.
    """

    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return events created at or after this timestamp (ISO 8601).

    Set this to the previous sync's checkpoint when doing incremental sync.
    """

    created_at_lt: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return events created strictly before this timestamp (ISO 8601).

    Recommended for bounding a sync operation — capture `now` once and reuse it as
    `created_at_lt` across all pages so newly arriving events don't shift the
    window.
    """

    entity_types: Optional[str]
    """Comma-separated list of entity types to include (e.g., `asset,album`).

    Valid values: `asset`, `album`, `person`, `face`, `album_asset`, `exif`. Omit to
    receive events for all types.
    """

    library_id: Optional[str]
    """Library to stream events from.

    Optional if the user has a single library; required when they have multiple. Use
    `list_libraries` to enumerate.
    """

    limit: int
    """Maximum number of events to return per page (1–200). Defaults to 20."""

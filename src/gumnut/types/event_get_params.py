# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventGetParams"]


class EventGetParams(TypedDict, total=False):
    after_cursor: Optional[str]
    """Cursor from the last event to paginate from.

    Pass the `cursor` field from the last event to get the next page.
    """

    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return events created at or after this timestamp (ISO 8601 format)"""

    created_at_lt: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return events created before this timestamp (ISO 8601 format).

    Recommended for bounding sync operations.
    """

    entity_types: Optional[str]
    """Comma-separated list of entity types to include (e.g., 'asset,album').

    Valid types: asset, album, person, face, album_asset, exif. Default: all types.
    """

    library_id: Optional[str]
    """Library to list events from. If not provided, uses the user's default library."""

    limit: int
    """Maximum number of events to return (1-500)"""

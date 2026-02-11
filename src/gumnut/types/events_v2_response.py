# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["EventsV2Response", "Data"]


class Data(BaseModel):
    """Lightweight event record for v2 sync endpoint."""

    created_at: datetime
    """When the event was recorded"""

    cursor: str
    """Opaque cursor for pagination. Pass as after_cursor to get the next page."""

    entity_id: str
    """ID of the entity that changed"""

    entity_type: str
    """Type of entity that changed (e.g., 'asset', 'album', 'person')"""

    event_type: str
    """Semantic event type (e.g., 'asset_created', 'album_deleted')"""


class EventsV2Response(BaseModel):
    """Response containing a page of v2 events."""

    data: List[Data]
    """List of events, ordered by event ID (monotonically increasing)"""

    has_more: bool
    """True if there are more events after this page.

    Use the last event's cursor to fetch the next page.
    """

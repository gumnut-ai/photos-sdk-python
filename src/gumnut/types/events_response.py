# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EventsResponse", "Data"]


class Data(BaseModel):
    """Lightweight event record for sync endpoint."""

    created_at: datetime
    """When the writer's transaction started.

    For display only: it is not the feed order and not a sync checkpoint.
    """

    cursor: str
    """Opaque position of this event.

    Resuming with it as `after_cursor` returns the events after it; prefer the
    page's `next_cursor`.
    """

    entity_id: str
    """ID of the entity that changed"""

    entity_type: str
    """Type of entity that changed (e.g., 'asset', 'album', 'person')"""

    event_type: str
    """Semantic event type (e.g., 'asset_created', 'album_deleted')"""

    payload: Optional[Dict[str, object]] = None
    """
    Optional extra context for the event (e.g., foreign keys for junction table
    deletions)
    """


class EventsResponse(BaseModel):
    """Response containing a page of events."""

    as_of: str
    """Opaque bound this read stopped at.

    Pass as `as_of` to the other reads in the same sync, such as other entity types,
    so they all stop at the same point.
    """

    data: List[Data]
    """Events in feed order, which is not commit order."""

    has_more: bool
    """
    True if more events are ready now: pass `next_cursor` as `after_cursor`,
    repeating `library_id`, `entity_types`, and `created_at_gte`, to fetch the next
    page. False means the client is caught up, not that the feed is closed.
    """

    next_cursor: Optional[str] = None
    """Store after applying this page and pass as `after_cursor` to continue.

    While `has_more` is true it also bounds the read to events ready when it began.
    Null only when the request had no cursor and returned no events.
    """

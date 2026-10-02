# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EventGetParams"]


class EventGetParams(TypedDict, total=False):
    after_cursor: Optional[str]
    """Opaque cursor to resume after: the previous page's `next_cursor`.

    Omit for a first sync.
    """

    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only return events created at or after this timestamp (ISO 8601).

    A display filter, not a sync checkpoint: `created_at` is when the writer's
    transaction started, so a later-committing event can carry an earlier timestamp.
    """

    created_at_lt: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Ignored.

    Reads are bounded by `next_cursor`; a timestamp bound could skip events.
    """

    entity_types: Optional[SequenceNotStr[str]]
    """Entity types to include (e.g., `asset`, `album`).

    Valid values: `asset`, `album`, `person`, `face`, `album_asset`, `metadata`,
    `stack`. Accepts multiple `entity_types=` query params or a single
    comma-delimited value (e.g., `entity_types=asset,album`). Omit to receive events
    for all types.
    """

    library_id: Optional[str]
    """Library to stream events from.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

    limit: int
    """Maximum number of events to return per page (1–200). Defaults to 20."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import FileTypes, SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SearchSearchAssetsParams"]


class SearchSearchAssetsParams(TypedDict, total=False):
    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported values: `metadata` (camera/EXIF/GPS and location names), `faces`,
    `people`, `metrics` (ML quality scores), and `file_data` (a group token gating
    the file/provenance scalars `device_asset_id`, `device_id`, `file_created_at`,
    `file_modified_at`, `checksum`, `checksum_sha1`, `file_size_bytes`). Accepts
    multiple `include=` query params or a single comma-delimited value (e.g.
    `include=faces,people`). Unknown values return 422. When omitted, all fields are
    returned (transition default).
    """

    captured_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter to only include assets captured after this date (ISO format)."""

    captured_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter to only include assets captured before this date (ISO format)."""

    image: Optional[FileTypes]
    """Image file to search for similar assets. Can be combined with text query."""

    library_id: Optional[str]
    """Library to search assets from (optional)"""

    limit: int
    """Number of results per page (1-200)"""

    page: int
    """Page number"""

    person_ids: Optional[SequenceNotStr[str]]
    """Filter to assets containing ALL of these person IDs (intersection, not union).

    Accepts multiple `person_ids=` form fields or a single comma-delimited value
    (e.g., `person_123,person_abc`). Get person IDs from `list_people`.
    """

    query: Optional[str]
    """The text query to search for.

    If you want to search for a specific person or set of people, use the person_ids
    parameter instead.If you want to search for a photos taken during a specific
    date range, use the captured_before and captured_after parameters instead.
    """

    threshold: float
    """Similarity threshold (lower means more similar)"""

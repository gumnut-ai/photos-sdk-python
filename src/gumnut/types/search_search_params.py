# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SearchSearchParams"]


class SearchSearchParams(TypedDict, total=False):
    captured_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly after this instant (ISO 8601; exclusive).

    Equivalent in purpose to `local_datetime_after` on `list_assets` (naming
    inconsistency is tracked as a follow-up).
    """

    captured_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only include assets captured strictly before this instant (ISO 8601; exclusive).

    Equivalent in purpose to `local_datetime_before` on `list_assets` (naming
    inconsistency is tracked as a follow-up).
    """

    library_id: Optional[str]
    """Library to search.

    Optional if the user has a single library; required when they have multiple. Use
    `list_libraries` to enumerate available libraries.
    """

    limit: int
    """Maximum number of results per page (1–200). Defaults to 20."""

    page: int
    """1-indexed page number.

    `search_assets` uses page-number pagination; the sibling `list_assets` uses
    cursor pagination via `starting_after_id`. Increment `page` to fetch subsequent
    pages.
    """

    person_ids: Optional[SequenceNotStr[str]]
    """Filter to assets containing ALL of these person IDs (intersection, not union).

    Accepts multiple `person_ids=` query params or a single comma-delimited value
    (e.g., `person_123,person_abc`). Get person IDs from `list_people`. Plural on
    this tool; the sibling `list_assets` uses `person_id` (singular).
    """

    query: Optional[str]
    """Natural-language description of the image content to search for.

    Matched against CLIP image embeddings, so it works best with concrete visual
    concepts: subjects, scenes, objects, settings ('beach sunset', 'birthday cake',
    'mountain hike').

    Prefer structured params when available: use `person_ids` for people (not names
    in `query`) and `captured_before`/`captured_after` for dates (not phrases like
    'in 2023' in `query`).
    """

    threshold: float
    """
    Maximum semantic distance for a result to be included (0.0 = identical, 1.0 =
    unrelated). Lower values return fewer, more confident matches; higher values
    return more results with looser matching. Default 0.8 is moderate — try 0.6 for
    high-precision queries, 0.9 for exploratory searches. **Note:** this is inverted
    from the usual 'similarity score' convention where higher means more similar.
    """

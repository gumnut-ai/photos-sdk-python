# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["PersonListParams"]


class PersonListParams(TypedDict, total=False):
    album_id: Optional[str]
    """
    Return only people who appear in at least one asset of this album, by a face or
    a body linked to them. Useful for 'who is in this album?'.
    """

    asset_id: Optional[str]
    """Return only people in this asset, by a face or a body linked to them.

    Useful for 'who is in this photo?'.
    """

    ids: Optional[SequenceNotStr[str]]
    """Look up specific people by ID (max 200; each ID has the `person_` prefix).

    Accepts multiple `ids=` query params or a single comma-delimited value (e.g.,
    `ids=person_1,person_2`). When set, `name_filter` defaults to `all` and
    `include_hidden` defaults to `true` so unnamed and hidden people are included in
    the lookup.
    """

    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported values: `cluster_metrics` (adds the nested `cluster_metrics` object —
    `pairwise_p90`, `pairwise_mean`, `face_count` — for each Person with a populated
    centroid). Accepts multiple `include=` query params or a single comma-delimited
    value. Unknown values return 422.
    """

    include_hidden: Optional[bool]
    """Include people marked hidden (`is_hidden`).

    Defaults to `false`, or to `true` when `ids` is provided, so lookups by ID still
    return hidden people.
    """

    library_id: Optional[str]
    """Library to list from.

    Optional if the user has a single live (non-trashed) library; required when they
    have multiple.
    """

    limit: int
    """Maximum number of people to return per page (1–200). Defaults to 20."""

    name: Optional[str]
    """Filter by name using case-insensitive substring matching.

    Use this to resolve a user-supplied name like 'Alice' into a `person_id` for the
    `person_ids` filter of an asset list or search.
    """

    name_filter: Optional[Literal["named", "unnamed", "all"]]
    """Filter by name nullness.

    Defaults to `named` (non-null names), or `all` when `ids` is provided.
    """

    sort: Literal["created_at_desc", "created_at_asc", "name_asc", "name_desc", "asset_count_desc", "asset_count_asc"]
    """Sort by when the person was added, their name, or how many assets they appear
    in.

    Use `created_at_desc` (default) for newest people first or `created_at_asc` for
    oldest first. Use `name_asc` for A–Z or `name_desc` for Z–A. Name sorting is
    locale-aware and places unnamed people last. With either name sort, omit
    `name_filter` or use `named` or `all`. Use `asset_count_desc` for the most
    photos and videos first or `asset_count_asc` for the fewest.
    """

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last person in the previous response's `data` to fetch the
    next page. Omit for the first page.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["PersonListParams"]


class PersonListParams(TypedDict, total=False):
    album_id: Optional[str]
    """Return only people who appear in at least one asset of this album.

    Useful for 'who is in this album?'.
    """

    asset_id: Optional[str]
    """Return only people who have at least one face in this asset.

    Useful for 'who is in this photo?'.
    """

    ids: Optional[SequenceNotStr[str]]
    """Look up specific people by ID (max 100; each ID has the `person_` prefix).

    Accepts multiple `ids=` query params or a single comma-delimited value (e.g.,
    `ids=person_1,person_2`). When set, `name_filter` defaults to `all` so unnamed
    clusters are included in the lookup.
    """

    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported values: `cluster_metrics` (adds the nested `cluster_metrics` object —
    `pairwise_p90`, `pairwise_mean`, `face_count` — for each Person with a populated
    centroid). Accepts multiple `include=` query params or a single comma-delimited
    value. Unknown values return 422.
    """

    library_id: Optional[str]
    """Library to list from.

    Optional if the user has a single library; required when they have multiple.
    """

    limit: int
    """Maximum number of people to return per page (1–200). Defaults to 20."""

    name: Optional[str]
    """Filter by name using case-insensitive substring matching.

    Use this to resolve a user-supplied name like 'Alice' into a `person_id`, then
    pass that ID into `search_assets.person_ids` or `list_assets.person_id`.
    """

    name_filter: Optional[Literal["named", "unnamed", "all"]]
    """
    Filter by name status: `named` returns only people with a name; `unnamed`
    returns only nameless face clusters awaiting a name; `all` returns both.
    Defaults to `named` (or `all` when `ids` is provided).
    """

    sort: Literal["created_at_desc", "created_at_asc", "name_asc", "name_desc", "asset_count_desc", "asset_count_asc"]
    """
    Sort order for results: `created_at_desc` (newest people first; default) /
    `created_at_asc`, `name_asc` / `name_desc` (alphabetical by name, locale-aware;
    unnamed people always sort last), or `asset_count_desc` / `asset_count_asc` (by
    number of photos the person appears in). Name sorts cannot be combined with
    `name_filter=unnamed`.
    """

    starting_after_id: Optional[str]
    """Cursor for pagination.

    Pass the `id` of the last person in the previous response's `data` to fetch the
    next page. Omit for the first page.
    """

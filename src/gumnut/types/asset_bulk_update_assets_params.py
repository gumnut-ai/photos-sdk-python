# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetBulkUpdateAssetsParams", "Update", "UpdateChange"]


class AssetBulkUpdateAssetsParams(TypedDict, total=False):
    updates: Required[Iterable[Update]]
    """List of per-asset updates.

    Each item carries the target asset id and the change to apply to it; different
    fields can be changed on different assets in the same request. Up to 100 items
    per request.
    """


class UpdateChange(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """The change to apply to this asset.

    Same shape as the body of the single-asset `update_asset` endpoint — same fields, same validation, same null-clears-the-override semantics.
    """

    description: Optional[str]
    """User-set description for the asset.

    Pass `null` to remove a previously-set value (the response then falls back to
    the description embedded in the file, if any). Omit to leave unchanged. Distinct
    from the AI-generated `description` field on the response — this writes to
    `metadata.description`.
    """

    latitude: Optional[float]
    """GPS latitude in decimal degrees, `[-90, 90]`.

    Must be set together with `longitude`. Pass `null` (along with `longitude=null`)
    to remove a previously-set value; omit to leave unchanged.
    """

    longitude: Optional[float]
    """GPS longitude in decimal degrees, `[-180, 180]`.

    Must be set together with `latitude`. Pass `null` (along with `latitude=null`)
    to remove a previously-set value; omit to leave unchanged.
    """

    original_datetime: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """When the asset was originally captured.

    Aware values store the offset from `utcoffset()` alongside; naive values store
    NULL offset. Pass `null` to remove a previously-set value — the response then
    falls back to the datetime embedded in the file when present, otherwise to the
    file's upload timestamp. Omit to leave unchanged.
    """


class Update(TypedDict, total=False):
    """One item in a bulk-update request.

    Names the target asset and carries the per-asset change to apply. The
    ``change`` object is exactly the body shape that the single-asset
    ``PATCH /api/assets/{asset_id}`` endpoint accepts; the wrapper exists so
    operation-level metadata (``id``, future ``if_match`` / idempotency-key
    fields) stays in a namespace disjoint from the entity-field changes.
    """

    id: Required[str]
    """Asset ID (with the `asset_` prefix) to apply this change to.

    Obtain from `list_assets`, `search_assets`, or `list_album_assets`.
    """

    change: Required[UpdateChange]
    """The change to apply to this asset.

    Same shape as the body of the single-asset `update_asset` endpoint — same
    fields, same validation, same null-clears-the-override semantics.
    """

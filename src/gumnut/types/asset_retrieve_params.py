# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AssetRetrieveParams"]


class AssetRetrieveParams(TypedDict, total=False):
    include: Optional[SequenceNotStr[str]]
    """Opt-in expansion fields.

    Supported values: `metadata` (camera/EXIF/GPS and location names), `faces`,
    `people`, `metrics` (ML quality scores), and `file_data` (a group token gating
    the file/provenance scalars `device_asset_id`, `device_id`, `file_created_at`,
    `file_modified_at`, `checksum`, `checksum_sha1`, `file_size_bytes`). Accepts
    multiple `include=` query params or a single comma-delimited value (e.g.
    `include=faces,people`). Unknown values return 422. When omitted, only the lean
    core is returned (`id`, `mime_type`, `local_datetime`, dimensions,
    `description`, `thumbhash`, `asset_urls`) and each value above is null/absent
    until you request it.
    """

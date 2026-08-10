# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..shared.asset_variant import AssetVariant

__all__ = ["VersionListResponse", "VersionListResponseItem"]


class VersionListResponseItem(BaseModel):
    """One rendering in an asset's retained version chain."""

    id: str
    """Unique version identifier with 'asset*version*' prefix"""

    checksum: Optional[str] = None
    """
    Base64-encoded SHA-256 hash of this rendering's stored bytes, for comparing a
    locally computed hash against the chain (e.g. when reconciling an ambiguous
    create failure). Not unique: identical bytes may legitimately appear at
    different positions or on other assets. Transitionally null for roots written
    during the column's rollout window, until a follow-up backfill lands.
    """

    file_size_bytes: int
    """Byte size of this rendering's stored bytes."""

    height: int
    """Height of this rendering in pixels"""

    kind: str
    """
    What produced this rendering: `original` (the upload), `edit` (a client-baked
    edit), or `external:<service>`. The namespace is open — treat an unrecognized
    kind as opaque rather than failing.
    """

    mime_type: str
    """MIME type of this rendering's bytes (e.g., 'image/jpeg')"""

    position: int
    """
    Zero-based index in the chain: 0 is the uploaded original, the highest is the
    current rendering.
    """

    width: int
    """Width of this rendering in pixels"""

    params: Optional[Dict[str, object]] = None
    """How this rendering was produced (e.g.

    an edit recipe). Opaque to the server; the schema is defined by whichever
    producer sets `kind`. `null` only for the original.
    """

    version_urls: Optional[Dict[str, AssetVariant]] = None
    """
    URLs for this rendering, shaped like an asset's `asset_urls`: the lean
    `thumbnail`/`thumbnail_image` rung by default; `include=variants` adds the
    remaining rungs and `original`, this rendering's exact stored bytes.
    """


VersionListResponse: TypeAlias = List[VersionListResponseItem]

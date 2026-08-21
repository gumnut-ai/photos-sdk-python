# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import FileTypes, SequenceNotStr

__all__ = ["VersionAppendParams"]


class VersionAppendParams(TypedDict, total=False):
    file: Required[FileTypes]
    """
    JPEG or PNG bytes with all edits and orientation already applied to the pixels,
    at most 100 MiB. The metadata-finalized file must also remain within that limit.
    The part's `Content-Type` declares the expected format; the format detected from
    the bytes is authoritative, and a concrete declared type that disagrees with it
    returns 422.
    """

    kind: Required[str]
    """
    What produced this rendering: `edit` for an edit rendered by the client, or
    `external:<service>` for an external producer. `original` is reserved for the
    uploaded position-0 version.
    """

    params: Required[str]
    """JSON object describing how the rendering was produced (e.g.

    an edit recipe), serialized as a string. Opaque to the server; the schema is
    defined by whichever producer sets `kind`. Malformed JSON, a non-object, or an
    over-large object returns 422.
    """

    include: Optional[SequenceNotStr[str]]
    """Optional response expansion.

    The single accepted value is `variants`: without it each row's `version_urls`
    carries only its lean thumbnail rung; with it, every rung plus the signed
    exact-byte `original`. Accepts multiple `include=` query params or a single
    comma-delimited value. Unknown values return 422.
    """

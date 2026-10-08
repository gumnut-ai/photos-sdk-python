# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AssetMoveResponse", "Data"]


class Data(BaseModel):
    asset_id: str
    """Requested asset ID."""

    outcome: Literal["moved", "already_in_destination", "failed"]
    """What a move request did with one asset.

    - `moved`: the asset is now in the destination library.
    - `already_in_destination`: the asset was already in the destination library, so
      nothing changed. This is a success.
    - `failed`: the asset was not moved; `failure` says why.
    """

    failure: Optional[Literal["unavailable", "changed_source", "duplicate", "quota", "busy"]] = None
    """Why an asset was not moved.

    - `unavailable`: the asset does not exist, is in the trash, or is not
      accessible.
    - `changed_source`: the asset is no longer in the source library.
    - `duplicate`: the destination library already holds an asset with the same
      original file, possibly in its trash.
    - `quota`: the destination library has no storage room for the asset.
    - `busy`: another operation is changing the asset. Retry the request.
    """


class AssetMoveResponse(BaseModel):
    data: List[Data]
    """One result per distinct requested asset ID, in request order."""

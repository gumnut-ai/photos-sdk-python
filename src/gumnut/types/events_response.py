# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .exif_response import ExifResponse
from .face_response import FaceResponse
from .album_response import AlbumResponse
from .asset_response import AssetResponse
from .person_response import PersonResponse
from .album_asset_response import AlbumAssetResponse

__all__ = [
    "EventsResponse",
    "Data",
    "DataAssetEventPayload",
    "DataAlbumEventPayload",
    "DataPersonEventPayload",
    "DataFaceEventPayload",
    "DataAlbumAssetEventPayload",
    "DataExifEventPayload",
]


class DataAssetEventPayload(BaseModel):
    """Event payload for asset entities."""

    data: AssetResponse
    """Full asset data"""

    entity_type: Optional[Literal["asset"]] = None


class DataAlbumEventPayload(BaseModel):
    """Event payload for album entities."""

    data: AlbumResponse
    """Full album data"""

    entity_type: Optional[Literal["album"]] = None


class DataPersonEventPayload(BaseModel):
    """Event payload for person entities."""

    data: PersonResponse
    """Full person data"""

    entity_type: Optional[Literal["person"]] = None


class DataFaceEventPayload(BaseModel):
    """Event payload for face entities."""

    data: FaceResponse
    """Full face data"""

    entity_type: Optional[Literal["face"]] = None


class DataAlbumAssetEventPayload(BaseModel):
    """Event payload for album_asset entities."""

    data: AlbumAssetResponse
    """Full album_asset data"""

    entity_type: Optional[Literal["album_asset"]] = None


class DataExifEventPayload(BaseModel):
    """Event payload for exif entities."""

    data: ExifResponse
    """Full exif data"""

    entity_type: Optional[Literal["exif"]] = None


Data: TypeAlias = Annotated[
    Union[
        DataAssetEventPayload,
        DataAlbumEventPayload,
        DataPersonEventPayload,
        DataFaceEventPayload,
        DataAlbumAssetEventPayload,
        DataExifEventPayload,
    ],
    PropertyInfo(discriminator="entity_type"),
]


class EventsResponse(BaseModel):
    """Response containing events."""

    data: List[Data]
    """
    List of events, ordered by entity type priority, then updated_at, then entity_id
    """

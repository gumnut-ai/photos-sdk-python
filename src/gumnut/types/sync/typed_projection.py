# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .face_projection import FaceProjection
from .album_projection import AlbumProjection
from .asset_projection import AssetProjection
from .stack_projection import StackProjection
from .person_projection import PersonProjection
from .album_asset_projection import AlbumAssetProjection
from .current_user_projection import CurrentUserProjection

__all__ = ["TypedProjection"]

TypedProjection: TypeAlias = Annotated[
    Union[
        CurrentUserProjection,
        AssetProjection,
        PersonProjection,
        FaceProjection,
        StackProjection,
        AlbumProjection,
        AlbumAssetProjection,
    ],
    PropertyInfo(discriminator="kind"),
]

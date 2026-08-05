# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["AssetCreateParams"]


class AssetCreateParams(TypedDict, total=False):
    asset_data: Required[FileTypes]
    """The image or video file, sent as a binary multipart part with a filename.

    The file's MIME type is derived from the filename extension and must be an image
    or video type; files with an unrecognized or non-media extension are rejected
    with 422. The filename is stored as the asset's original file name (maximum 1024
    characters). The API imposes no fixed per-file size limit; uploads are
    constrained only by the storage caps.
    """

    device_asset_id: Required[str]
    """
    Identifier of this asset on the uploading device, chosen by the client (for
    example, the device's local asset ID). Stored verbatim and usable for
    device-based existence checks; plays no part in upload-time duplicate detection.
    """

    device_id: Required[str]
    """Identifier of the uploading device or client, chosen by the client.

    Paired with `device_asset_id` for device-based existence checks.
    """

    file_created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """When the file was created on the uploading device, as an ISO 8601 datetime.

    Also serves as the fallback for the asset's local capture time when the file's
    embedded metadata carries no usable timestamp.
    """

    file_modified_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    When the file was last modified on the uploading device, as an ISO 8601
    datetime.
    """

    library_id: Optional[str]
    """Library to upload into.

    For an all-library credential, omit to use the account's sole live library or
    create a fresh default when there are no live libraries; pass explicitly when
    the account has multiple live libraries. For a selected-library credential, omit
    to use its sole selected library; pass explicitly when it selects multiple
    libraries.
    """

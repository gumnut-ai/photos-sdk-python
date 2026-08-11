# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    library_id: Optional[str]
    """Restrict results to tasks owned by this library.

    When omitted, returns tasks across every library the authenticated user owns.
    """

    limit: int
    """Maximum number of tasks to return."""

    status: Optional[Literal["pending", "started", "success", "failure"]]
    """Return only tasks currently in this execution status."""

    task_type: Optional[
        Literal[
            "image_quality",
            "embedding",
            "face_detection",
            "face_clustering",
            "asset_description",
            "asset_storage_cleanup",
            "asset_version_storage_cleanup",
            "reverse_geocoding",
            "video_thumbnail_extract",
            "video_metadata_extract",
            "thumbhash",
            "display_proxy_generation",
            "burst_detection",
        ]
    ]
    """Return only tasks of this type."""

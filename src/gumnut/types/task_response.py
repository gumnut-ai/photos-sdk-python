# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaskResponse"]


class TaskResponse(BaseModel):
    """A background processing task and its current execution state."""

    id: str
    """Unique task identifier with `btask_` prefix"""

    asset_id: Optional[str] = None
    """
    ID of the asset this task processes; null for library-scoped tasks such as face
    clustering
    """

    celery_task_id: str
    """Deprecated alternate task identifier. Use `id` instead."""

    completed_at: Optional[str] = None
    """When the task finished, whether successfully or not (ISO 8601); null until then"""

    created_at: str
    """
    When the task record was created (ISO 8601); dispatch to the task queue follows
    separately, after the creating transaction commits
    """

    error_message: Optional[str] = None
    """
    Error detail from the most recent failed or retried attempt; not cleared by a
    later success, so it can be non-null on a task that failed transiently and then
    succeeded. Null if no attempt has failed
    """

    outcome: Optional[str] = None
    """Stable outcome code whose meaning depends on `task_type`.

    For a successful `face_detection` task: `ran` means detection ran, possibly
    finding no faces; `skipped_photo_location` means automatic detection is not
    offered at the photo's location; `skipped_location_unread` means the photo has
    no location and its file's metadata has not been read; `skipped_owner_off` means
    the library owner had not turned detection on when the photo was processed;
    `skipped_owner_region` means detection is not offered in the owner's home
    region. Turning detection on later does not process earlier photos. Null for
    other task types, tasks that have not succeeded, and skips with no explanation,
    such as files that are not images. Each task reports its own run. Codes may be
    added for any task type; treat an unrecognized code as no explanation.
    """

    result: Optional[str] = None
    """Result summary produced by a completed task; null until success"""

    retry_count: int
    """Retry and rescue bookkeeping value for this task.

    Zero before any automatic retry or stuck-task rescue; not guaranteed to be a
    cumulative delivery count
    """

    started_at: Optional[str] = None
    """
    When a worker most recently began executing the task, or when the stuck-task
    reaper rescued it back to pending (ISO 8601). Because a rescue can re-enqueue a
    task no worker ever picked up, a non-null value does not prove a worker has run
    the task
    """

    status: Literal["pending", "started", "success", "failure"]
    """
    Status of a background task execution: `pending` (created and awaiting
    processing), `started` (picked up by a worker and not yet in a terminal state —
    the task may be executing or awaiting an automatic retry after a transient
    failure), `success` (completed successfully), or `failure` (failed and will not
    be retried).
    """

    task_type: Literal[
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
        "product_update_subscription",
        "person_metrics_refresh",
        "quality_scoring",
        "face_template_removal",
    ]
    """
    Kind of background processing a task performs: `image_quality` (historical only
    — scored an image's technical quality; this task type is retired and no longer
    dispatched, the value appears only on old task rows), `embedding` (compute the
    content embedding that powers search), `face_detection` (detect faces in an
    asset), `face_clustering` (group a library's detected faces into people),
    `asset_description` (generate a natural-language description of an asset),
    `asset_storage_cleanup` (remove stored files left behind by a permanently
    deleted asset), `asset_version_storage_cleanup` (remove stored files of a
    superseded asset version), `reverse_geocoding` (resolve an asset's GPS
    coordinates to a place name), `video_thumbnail_extract` (extract a thumbnail
    image from a video), `video_metadata_extract` (recover a video's capture time,
    GPS location, and camera details from the file's own metadata), `thumbhash`
    (compute the blurred placeholder shown while a thumbnail loads),
    `display_proxy_generation` (generate a browser-displayable rendition of an
    original the image CDN cannot transform, such as an oversized or
    over-dimensioned file), `burst_detection` (detect rapid-fire shots of the same
    moment and stack them), `product_update_subscription` (enroll an explicitly
    opted-in new user in product-update email delivery), `person_metrics_refresh`
    (recompute the face-matching summary of one person after their faces change),
    `quality_scoring` (rate an image's photographic quality), or
    `face_template_removal` (historical only — removed the stored face templates of
    every library an owner owns; this task type is retired and no longer
    dispatched).
    """

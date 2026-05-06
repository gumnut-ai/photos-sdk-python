# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import date, datetime

from .._models import BaseModel
from .shared.asset_variant import AssetVariant
from .cluster_metrics_response import ClusterMetricsResponse

__all__ = ["PersonResponse"]


class PersonResponse(BaseModel):
    """Represents a person identified through face clustering and recognition."""

    id: str
    """Unique person identifier with 'person\\__' prefix"""

    created_at: datetime
    """When this person record was created"""

    is_favorite: bool
    """Whether this person is marked as a favorite"""

    is_hidden: bool
    """Whether this person should be hidden from the UI"""

    updated_at: datetime
    """When this person record was last updated"""

    asset_count: Optional[int] = None
    """Number of unique photos this person appears in, or null if not computed"""

    asset_urls: Optional[Dict[str, AssetVariant]] = None
    """Asset variants from this person's thumbnail face.

    May be null when embedded in an AssetResponse; use /api/people endpoints for
    full person data.
    """

    birth_date: Optional[date] = None
    """Optional birth date of this person"""

    cluster_metrics: Optional[ClusterMetricsResponse] = None
    """
    Cohesion metrics for a Person's face cluster — surfaced via
    `include=cluster_metrics` on the people endpoints. These describe how tight the
    cluster is in embedding space (lower = more cohesive) and drive both the
    production face-assignment cohesion gate and the operator-facing face cleanup
    dashboard.
    """

    name: Optional[str] = None
    """Optional name assigned to this person"""

    thumbnail_face_id: Optional[str] = None
    """ID of the face resource used as this person's thumbnail"""

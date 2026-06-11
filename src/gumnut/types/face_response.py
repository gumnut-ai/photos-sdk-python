# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.asset_variant import AssetVariant
from .cluster_assignment_response import ClusterAssignmentResponse

__all__ = ["FaceResponse"]


class FaceResponse(BaseModel):
    """Represents a detected face in an asset with facial recognition data."""

    id: str
    """Unique face identifier with 'face\\__' prefix"""

    asset_id: str
    """ID of the asset containing this face"""

    bounding_box: Dict[str, int]
    """Face location as {x, y, w, h} coordinates in pixels"""

    created_at: datetime
    """When this face was detected and recorded"""

    source: Literal["automatic", "manual"]
    """
    How this face was added: 'automatic' for detector-found faces, 'manual' for
    user-drawn face boxes.
    """

    updated_at: datetime
    """When this face record was last updated"""

    asset_urls: Optional[Dict[str, AssetVariant]] = None
    """Asset variants for this face: 'thumbnail' with face crop"""

    cluster_assignment: Optional[ClusterAssignmentResponse] = None
    """
    Per-face cluster-assignment diagnostics: how well the face fits its
    currently-assigned Person, and which other Persons are nearby in embedding
    space. Surfaced via `include=cluster_assignment` on the faces endpoints — used
    by the operator-facing face cleanup dashboard to triage mis-clustered faces.
    """

    confidence: Optional[float] = None
    """
    Detector confidence on a 0-1 scale; higher is more confident among faces
    detected under the same configuration (values are not comparable across detector
    generations). Null on legacy faces without a stored score and on manually added
    faces.
    """

    person_id: Optional[str] = None
    """ID of the person this face belongs to (if identified)"""

    timestamp_ms: Optional[int] = None
    """For video files, timestamp in milliseconds when face appears"""

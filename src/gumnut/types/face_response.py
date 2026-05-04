# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.asset_variant import AssetVariant

__all__ = ["FaceResponse", "ClusterAssignment", "ClusterAssignmentCandidate"]


class ClusterAssignmentCandidate(BaseModel):
    """
    A Person whose centroid is close enough to a given face's embedding
    that it would be considered for assignment — surfaced under
    ``ClusterAssignmentResponse.candidates``.
    """

    distance: float
    """
    Cosine distance from the face's embedding to this Person's centroid (lower =
    closer).
    """

    person_id: str
    """Person ID (with 'person\\__' prefix) of the candidate."""

    name: Optional[str] = None
    """Display name of the candidate Person, or null for unnamed clusters.

    Candidates surface the same Persons production assignment considers, which
    includes unnamed clusters.
    """


class ClusterAssignment(BaseModel):
    """
    Per-face cluster-assignment diagnostics: how well the face fits its
    currently-assigned Person, and which other Persons are nearby in
    embedding space. Surfaced via ``include=cluster_assignment`` on the
    faces endpoints — used by the operator-facing face cleanup dashboard
    to triage mis-clustered faces.
    """

    candidates: Optional[List[ClusterAssignmentCandidate]] = None
    """
    Persons in the same library that pass the same gate shape as production face
    assignment, surfaced with deliberately relaxed thresholds so the list is a
    superset of what the automated path would admit. Sorted ascending by distance.
    Excludes the face's currently-assigned Person (its distance is in
    `distance_to_person`). Empty when no eligible Persons pass the gate.
    """

    distance_to_person: Optional[float] = None
    """
    Cosine distance from the face's embedding to its currently-assigned Person's
    centroid. Lower = better fit. Null when the face is unassigned or when the
    assigned Person has no centroid.
    """


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

    updated_at: datetime
    """When this face record was last updated"""

    asset_urls: Optional[Dict[str, AssetVariant]] = None
    """Asset variants for this face: 'thumbnail' with face crop"""

    cluster_assignment: Optional[ClusterAssignment] = None
    """
    Per-face cluster-assignment diagnostics: how well the face fits its
    currently-assigned Person, and which other Persons are nearby in embedding
    space. Surfaced via `include=cluster_assignment` on the faces endpoints — used
    by the operator-facing face cleanup dashboard to triage mis-clustered faces.
    """

    person_id: Optional[str] = None
    """ID of the person this face belongs to (if identified)"""

    timestamp_ms: Optional[int] = None
    """For video files, timestamp in milliseconds when face appears"""

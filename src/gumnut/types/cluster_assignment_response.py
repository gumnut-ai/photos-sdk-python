# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ClusterAssignmentResponse", "Candidate"]


class Candidate(BaseModel):
    """A nearby named Person returned under `ClusterAssignmentResponse.candidates`."""

    distance: float
    """
    Cosine distance from the face's embedding to this Person's centroid (lower =
    closer).
    """

    person_id: str
    """Person ID (with 'person\\__' prefix) of the candidate."""

    name: Optional[str] = None
    """Display name of the named candidate Person."""


class ClusterAssignmentResponse(BaseModel):
    """
    Per-face cluster-assignment diagnostics: how well the face fits its
    currently-assigned Person, and which other named Persons are nearby in
    embedding space. Surfaced via `include=cluster_assignment` on the
    faces endpoints.
    """

    candidates: Optional[List[Candidate]] = None
    """Eligible nearby named Persons in the same library, sorted ascending by distance.

    Excludes the face's currently-assigned Person (its distance is in
    `distance_to_person`) and people marked hidden (`is_hidden`). Empty when there
    are no eligible nearby Persons, or when the library owner's settings do not
    allow automatic face detection.
    """

    distance_to_person: Optional[float] = None
    """
    Cosine distance from the face's embedding to its currently-assigned Person's
    centroid. Lower = better fit. Null when the face is unassigned, when the
    assigned Person has no centroid, or when the library owner's settings do not
    allow automatic face detection.
    """

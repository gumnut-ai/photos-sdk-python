# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ClusterAssignmentResponse", "Candidate"]


class Candidate(BaseModel):
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


class ClusterAssignmentResponse(BaseModel):
    """
    Per-face cluster-assignment diagnostics: how well the face fits its
    currently-assigned Person, and which other Persons are nearby in
    embedding space. Surfaced via ``include=cluster_assignment`` on the
    faces endpoints — used by the operator-facing face cleanup dashboard
    to triage mis-clustered faces.
    """

    candidates: Optional[List[Candidate]] = None
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

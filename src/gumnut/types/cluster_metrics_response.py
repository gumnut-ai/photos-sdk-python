# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ClusterMetricsResponse"]


class ClusterMetricsResponse(BaseModel):
    """
    Cohesion metrics for a Person's face cluster — surfaced via
    ``include=cluster_metrics`` on the people endpoints. These describe how
    tight the cluster is in embedding space (lower = more cohesive) and
    drive both the production face-assignment cohesion gate and the
    operator-facing face cleanup dashboard.
    """

    face_count: int
    """Number of faces that fed into the centroid and pairwise metrics.

    This is the cluster-membership count, **not** the same as `asset_count` —
    `face_count` counts every face row, while `asset_count` counts distinct assets
    (one asset can contribute multiple faces of the same person).
    """

    pairwise_mean: float
    """Mean pairwise cosine distance between faces in this person's cluster."""

    pairwise_p90: float
    """90th-percentile pairwise cosine distance between faces in this person's cluster.

    Lower = more cohesive cluster; loose clusters (higher pairwise_p90) are gated
    out of the face-assignment path to prevent further drift.
    """

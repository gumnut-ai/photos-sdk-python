# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .typed_projection import TypedProjection
from .projection_enumeration import ProjectionEnumeration
from .projection_root_result import ProjectionRootResult
from .gumnut_projection_scope import GumnutProjectionScope
from .projection_baseline_start import ProjectionBaselineStart

__all__ = ["ProjectionReadResponse"]


class ProjectionReadResponse(BaseModel):
    baseline_start: Optional[ProjectionBaselineStart] = None
    """Finite family bounds and safe event start, only in baseline_begin"""

    enumeration: Optional[ProjectionEnumeration] = None
    """Accepted prefix frontier, only in baseline_page or relation_page"""

    profile_hash: str
    """Lowercase SHA-256 of the canonical complete semantic manifest"""

    projections: List[TypedProjection]
    """
    Deduplicated complete closure sorted by kind and key; includes the principal in
    content reads, empty in baseline_begin
    """

    roots: List[ProjectionRootResult]
    """Exact selected root results, sorted by kind and stable key"""

    scope: GumnutProjectionScope
    """Current library scope captured with the content"""

    semantic_schema_version: Literal[1]
    """Projection bundle semantic schema version"""

    snapshot_id: str
    """Diagnostic read identifier; cannot retrieve an old snapshot"""

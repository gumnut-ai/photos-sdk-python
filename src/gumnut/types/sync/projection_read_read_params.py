# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .projection_key_param import ProjectionKeyParam
from .relation_selector_param import RelationSelectorParam
from .projection_profile_param import ProjectionProfileParam

__all__ = [
    "ProjectionReadReadParams",
    "RootsProjectionReadRequest",
    "BaselineBeginRequest",
    "BaselinePageRequest",
    "RelationPageRequest",
]


class RootsProjectionReadRequest(TypedDict, total=False):
    keys: Required[Iterable[ProjectionKeyParam]]
    """Nonempty unique root selection; exceeding capacity returns 413"""

    library_id: Required[str]
    """Explicit live library binding for every root and dependency"""

    mode: Required[Literal["roots"]]
    """Read exactly the explicit roots and their required dependencies"""

    profile: Required[ProjectionProfileParam]
    """Versioned source semantics to project"""


class BaselineBeginRequest(TypedDict, total=False):
    library_id: Required[str]
    """Explicit live library binding for every root and dependency"""

    mode: Required[Literal["baseline_begin"]]
    """Capture finite family bounds and safe event start"""

    profile: Required[ProjectionProfileParam]
    """Versioned source semantics to project"""


class BaselinePageRequest(TypedDict, total=False):
    enumeration_token: Required[str]
    """Signed finite selection; never an authorization or snapshot handle"""

    library_id: Required[str]
    """Explicit live library binding for every root and dependency"""

    mode: Required[Literal["baseline_page"]]
    """Continue one baseline family's finite selection"""

    profile: Required[ProjectionProfileParam]
    """Versioned source semantics to project"""


class RelationPageRequest(TypedDict, total=False):
    enumeration_token: Required[Optional[str]]
    """Null starts a finite relation scan; otherwise continue its signed selection"""

    library_id: Required[str]
    """Explicit live library binding for every root and dependency"""

    mode: Required[Literal["relation_page"]]
    """Enumerate finite current children with their parent"""

    profile: Required[ProjectionProfileParam]
    """Versioned source semantics to project"""

    selector: Required[RelationSelectorParam]
    """Bound relationship and parent identity"""


ProjectionReadReadParams: TypeAlias = Union[
    RootsProjectionReadRequest, BaselineBeginRequest, BaselinePageRequest, RelationPageRequest
]

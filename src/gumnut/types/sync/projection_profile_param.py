# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProjectionProfileParam"]


class ProjectionProfileParam(TypedDict, total=False):
    name: Required[Literal["gumnut-library"]]
    """Immutable Gumnut domain contract name"""

    version: Required[Literal[1]]
    """Immutable contract version"""

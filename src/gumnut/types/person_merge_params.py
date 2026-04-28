# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PersonMergeParams"]


class PersonMergeParams(TypedDict, total=False):
    source_person_ids: Required[SequenceNotStr[str]]
    """IDs of the people to merge into the primary person.

    These people will be deleted after their faces are moved.
    """

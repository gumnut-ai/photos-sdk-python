# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["FeedbackSubmitParams"]


class FeedbackSubmitParams(TypedDict, total=False):
    feedback_type: Required[Literal["bug", "missing_capability", "confusing_behavior", "suggestion", "other"]]

    message: Required[str]

    task_completed: Optional[bool]

    tool_names: Optional[SequenceNotStr[str]]
